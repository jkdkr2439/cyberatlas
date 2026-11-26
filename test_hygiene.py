"""Regression tests for portable source references and redacted scan output."""
from pathlib import Path
import json
import os
import tempfile
import struct
import zlib
import unittest
from unittest.mock import patch
from scripts.audit_repository import scan_content, PNG_SIGNATURE
from source_config import external_source, source_ref

ROOT = Path(__file__).resolve().parent

class HygieneTests(unittest.TestCase):
    @staticmethod
    def png(chunks):
        return PNG_SIGNATURE + b''.join(struct.pack('>I', len(payload)) + kind + payload +
            struct.pack('>I', zlib.crc32(kind + payload)) for kind, payload in chunks + [(b'IEND', b'')])

    def test_png_pixels_are_not_treated_as_text(self):
        fake_path = ('Z:' + '/' + 'Users/example/private').encode()
        self.assertEqual(scan_content(self.png([(b'IDAT', fake_path)]), 'fixture'), [])
        findings = scan_content(self.png([(b'tEXt', b'Comment\0' + fake_path)]), 'fixture')
        self.assertEqual(findings[0]['rule'], 'absolute_local_path')
        self.assertTrue(findings[0]['location'].endswith(':png-metadata'))

    def test_compressed_png_metadata_is_scanned(self):
        fake_token = ('gh' + 'p_' + 'a' * 36).encode()
        for kind, payload in [(b'zTXt', b'Comment\0\0' + zlib.compress(fake_token)),
                              (b'iTXt', b'Comment\0\1\0\0\0' + zlib.compress(fake_token))]:
            with self.subTest(kind=kind):
                findings = scan_content(self.png([(kind, payload)]), 'fixture')
                self.assertEqual(findings[0]['rule'], 'provider_token')
                self.assertNotIn(fake_token.decode(), json.dumps(findings))

    def test_invalid_png_metadata_does_not_silently_pass(self):
        findings = scan_content(PNG_SIGNATURE + b'incomplete', 'fixture')
        self.assertEqual(findings[0]['rule'], 'unreadable_png_metadata')

    def test_sensitive_patterns_report_locations_not_values(self):
        samples = {
            'absolute_local_path': 'Z:' + '/' + 'Users/example/private/file.txt',
            'provider_token': 'gh' + 'p_' + 'a' * 36,
            'private_key': '-----BEGIN ' + 'PRIVATE KEY-----',
            'credential_url': 'https:' + '//user:secret@example.invalid',
            'literal_credential': 'api_key = ' + repr('placeholder' * 3),
            'jwt': 'eyJ' + 'a' * 14 + '.' + 'b' * 20 + '.' + 'c' * 20,
        }
        for rule, value in samples.items():
            with self.subTest(rule=rule):
                findings = scan_content(value.encode(), 'fixture')
                self.assertIn(rule, [f['rule'] for f in findings])
                self.assertNotIn(value, json.dumps(findings))

    def test_public_references_and_hashes_are_not_credentials(self):
        text = 'https://example.invalid/spec\n' + source_ref('book') + '\n' + 'a' * 64
        self.assertEqual(scan_content(text.encode(), 'fixture'), [])

    def test_external_paths_are_opt_in_and_not_source_identifiers(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertIsNone(external_source('book'))
            with self.assertRaisesRegex(ValueError, 'CYBER_ATLAS_SOURCE_BOOK'):
                external_source('book', required=True)
            with tempfile.TemporaryDirectory() as directory:
                document = Path(directory) / 'source.md'
                document.write_text('fixture', encoding='utf-8')
                with patch.dict(os.environ, {'CYBER_ATLAS_SOURCE_BOOK': str(document)}):
                    self.assertEqual(external_source('book'), document)
                    self.assertEqual(source_ref('book'), 'urn:cyber-atlas:source:book')

    def test_all_snapshot_and_seed_sources_are_portable(self):
        records = [json.loads((ROOT / 'data/source_index.json').read_text(encoding='utf-8')),
                   json.loads((ROOT / 'data/atlas.json').read_text(encoding='utf-8'))]
        records += [{'sources': json.loads(path.read_text(encoding='utf-8'))}
                    for path in (ROOT / 'graph/revisions').glob('*/sources.json')]
        for record in records:
            for source in record['sources']:
                if source['id'] in ('book', 'metric', 'lens'):
                    for key in ('url', 'location'):
                        self.assertEqual(source[key], source_ref(source['id']))
        self.assertEqual(records[0]['book'], source_ref('book'))

if __name__ == '__main__':
    unittest.main()
