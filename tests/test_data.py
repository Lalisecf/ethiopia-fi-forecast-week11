from pathlib import Path

def test_readme_exists():
    assert Path("README.md").exists()

def test_requirements_exists():
    assert Path("requirements.txt").exists()

def test_notebooks_folder_exists():
    assert Path("notebooks").exists()