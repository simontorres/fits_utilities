from __future__ import absolute_import


def test_sample():
    assert 1 == 1

def test_import():
    try:
        from fits_utilities.hselect import HeaderSelect
        from fits_utilities.imhead import ImageHeader
    except ImportError:
        return False
