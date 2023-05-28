from pathlib import Path
import pytest

from src.pwproxy.run import Run

pytest_plugins = "pytester"


def test_run(pytester: pytest.Pytester, tmp_path: Path):
    path = pytester.makepyfile("""
    
    
    """)

    Run.run(path)
    assert False
