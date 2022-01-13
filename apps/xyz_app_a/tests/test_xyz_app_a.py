from xyz_app_a import __version__
from xyz_app_a.new_module import f


def test_version():
    assert __version__ == "0.1.0"


def test_f():
    assert f() == "hi!"
