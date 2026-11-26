"""Regression tests for portable source references and redacted scan output."""
from pathlib import Path
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from scripts.audit_repository import scan_content
from source_config import external_source, source_ref

ROOT = Path(__file__).resolve().parent

class HygieneTests(unittest.TestCase):
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
