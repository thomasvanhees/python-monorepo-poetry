"""Foo module."""

from xyz_lib_b.bar import foo


def bar():
    """Use foo to generate bar."""
    return "hi!"


def foo2():
    """Foo2."""
    return foo()
