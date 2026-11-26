"""Optional external documents: resolve locally, never serialize their paths."""
from pathlib import Path
import os

SOURCE_IDS = ('book', 'metric', 'lens')

def source_ref(source_id):
    if source_id not in SOURCE_IDS:
        raise ValueError('Unknown external source ID')
    return 'urn:cyber-atlas:source:' + source_id

def external_source(source_id, required=False):
    source_ref(source_id)
    variable = 'CYBER_ATLAS_SOURCE_' + source_id.upper()
    value = os.environ.get(variable)
    path = Path(value).expanduser() if value else None
    if path is not None and path.is_file():
        return path
    if required:
        raise ValueError('Set ' + variable + ' to an existing external source file; it is not bundled.')
    return None
