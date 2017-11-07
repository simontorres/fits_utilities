from __future__ import absolute_import


def test_sample():
    assert 1 == 1

def test_import():
    try:
        from utils.hselect import HeaderSelect
        from utils.imhead import ImageHeader
    except ImportError:
        return False
