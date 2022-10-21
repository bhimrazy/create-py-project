import os
import tempfile

from create_py_project import __version__
from create_py_project.utils import generate_project


def test_version():
    """Assert the version of the package."""
    assert __version__ == "0.1.0"


def test_generate_project():
    """Test generate project function"""
    with tempfile.TemporaryDirectory() as tmpdirname:
        project_name = "MyNewApp"
        template = "template-vannila"
        generate_project(name=project_name, template=template, dest=tmpdirname)
        assert os.path.isdir(os.path.join(tmpdirname, project_name))
