"""Automated testing for mendi."""

from mendi import __version__


def test_version():
    """Check the version of mendi."""
    assert __version__.startswith("0.1")
