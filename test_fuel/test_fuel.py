from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
