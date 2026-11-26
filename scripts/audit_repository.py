"""Offline repository hygiene scan. Reports locations and rule names, never values.

Heuristics are a backstop, not proof that arbitrary credentials cannot exist.
No network calls or credential validation are performed.
"""
from pathlib import Path
import argparse
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
RULES = {
    'absolute_local_path': re.compile(r'(?i)(?<![A-Za-z])[A-Z]:[\\/](?![\\/]?\$)|/(?:Users|home)/[\w.-]+/|file:/{3}'),
    'private_key': re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----'),
    'provider_token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-(?:proj-|ant-)?[A-Za-z0-9_-]{24,}|xox[baprs]-[A-Za-z0-9-]{20,}|AKIA[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{35})\b'),
    'jwt': re.compile(r'\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b'),
    'credential_url': re.compile(r'(?i)\b(?:https?|postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis)://[^\s/:@]+:[^\s/@]+@'),
    'literal_credential': re.compile(r'''(?i)["']?\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|password|passwd|secret[_-]?key)\b["']?\s*[:=]\s*["'][A-Za-z0-9_+/=.!@#$%^&*-]{16,}["']'''),
}
FORBIDDEN_SUFFIXES = {'.pdf', '.docx', '.pem', '.key', '.p12', '.pfx', '.jks', '.keystore'}

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def read_objects(ids):
    if not ids:
        return {}
    batch = subprocess.run(['git', 'cat-file', '--batch'], input=b'\n'.join(ids)+b'\n',
                           cwd=ROOT, capture_output=True, check=True).stdout
    offset = 0
    objects = {}
    for oid in ids:
        end = batch.index(b'\n', offset)
        header = batch[offset:end].split()
        size = int(header[2]); start = end + 1
        objects[oid] = (header[1], batch[start:start + size])
        offset = start + size + 1
    return objects

def scan_content(data, location):
    if data.startswith(b'%PDF-'):
        return [{'location': location, 'line': 1, 'rule': 'pdf_payload'}]
    text = data.decode('utf-8', errors='replace')
    return [{'location': location, 'line': text.count('\n', 0, match.start()) + 1, 'rule': rule}
            for rule, pattern in RULES.items() for match in pattern.finditer(text)]

def scan(history=False, staged=False):
    findings = []
    names = git('ls-files', '-z', *([] if staged else ['--cached', '--others', '--exclude-standard'])).decode('utf-8').strip('\0').split('\0')
    staged_ids = {}
    if staged:
        for entry in git('ls-files', '--stage', '-z').split(b'\0'):
            if not entry:
                continue
            metadata, name = entry.split(b'\t', 1)
            _, oid, stage = metadata.split()
            if stage != b'0':
                raise ValueError('Resolve merge conflicts before scanning the index')
            staged_ids[name.decode('utf-8')] = oid
        staged_objects = read_objects(list(dict.fromkeys(staged_ids.values())))
    for name in filter(None, names):
        path = Path(name)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or (path.name.startswith('.env') and path.name != '.env.example'):
            findings.append({'location': name, 'rule': 'forbidden_file'})
        if staged:
            raw = staged_objects[staged_ids[name]][1]
        elif (ROOT / name).is_file():
            raw = (ROOT / name).read_bytes()
        else:
            continue
        findings.extend(scan_content(raw, name))
    blobs = 0
    if history:
        objects = git('rev-list', '--objects', '--all').splitlines()
        ids = [line.split(b' ', 1)[0] for line in objects]
        for oid, (kind, raw) in read_objects(ids).items():
            if kind == b'blob':
                blobs += 1
                findings.extend(scan_content(raw, 'git-blob:' + oid.decode()))
            elif kind in (b'commit', b'tag'):
                findings.extend(scan_content(raw, 'git-metadata:' + oid.decode()))
    return {'tracked_files': len(names), 'history_blobs_scanned': blobs, 'findings': findings,
            'scope': 'tracked working files' if not staged else 'staged files',
            'limitations': 'Pattern scan only; no external credential validation or guarantee of absence.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', action='store_true')
    parser.add_argument('--staged', action='store_true')
    args = parser.parse_args()
    report = scan(args.history, args.staged)
    print(json.dumps(report, ensure_ascii=True, indent=2))
    raise SystemExit(bool(report['findings']))
