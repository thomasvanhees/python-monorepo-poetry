from xyz_lib_b import __version__
from xyz_lib_c import __version__ as __version2__


def test_version():
    assert __version__ == "0.1.0"


def test_version2():
    assert __version2__ == "0.1.0"
