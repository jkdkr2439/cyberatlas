"""Test the staged repository in a clean checkout without external source books."""
from pathlib import Path
import json, os, subprocess, sys, tempfile

ROOT=Path(__file__).resolve().parents[1]

def command(args,cwd=ROOT,env=None):
    result=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True,encoding='utf-8',timeout=300)
    if result.returncode:
        raise RuntimeError(result.stdout+'\n'+result.stderr)
    return result

def verify():
    names=command(['git','ls-files','-z']).stdout.split('\0')
    names=[name for name in names if name]
    if not names:raise RuntimeError('No staged repository files')
    forbidden=[name for name in names if Path(name).suffix.lower() in {'.pdf','.docx'}]
    if forbidden:raise RuntimeError('Source documents staged: '+str(forbidden))
    with tempfile.TemporaryDirectory(prefix='cyber-atlas-checkout-') as temporary:
        checkout=Path(temporary).resolve()
        assert checkout.parent==Path(tempfile.gettempdir()).resolve()
        assert checkout.name.startswith('cyber-atlas-checkout-')
        command(['git','checkout-index','--all','--prefix',checkout.as_posix()+'/'])
        pdf_payloads=[name for name in names if (checkout/name).read_bytes().startswith(b'%PDF-')]
        if pdf_payloads:raise RuntimeError('PDF payload staged under another extension: '+str(pdf_payloads))
        graph_result=json.loads(command([sys.executable,'graph.py','validate'],cwd=checkout).stdout)
        env={**os.environ,'CYBER_ATLAS_EXTERNAL_SOURCE_CHECKS':'0','PYTHONIOENCODING':'utf-8'}
        tests=command([sys.executable,'-m','unittest','test_graph','validate','test_hygiene','-q'],cwd=checkout,env=env)
        print(tests.stderr.strip())
        print(json.dumps({'staged_files':len(names),'pdf_files':0,'docx_files':0,
                          'graph_revision':graph_result['revision'],'clean_checkout':'passed',
                          'external_source_books':'not required; source-hash comparison explicitly skipped'},ensure_ascii=False))

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');sys.stderr.reconfigure(encoding='utf-8')
    verify()
