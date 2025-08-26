import pytest
from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("Goodbye") == "Gdby"
    assert shorten("") == ""
    assert shorten("aeiouAEIOU") == ""
    assert shorten("Python3") == "Pythn3"
    assert shorten("Python!") == "Pythn!"




