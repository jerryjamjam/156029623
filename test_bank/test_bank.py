import bank
import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
def test_value_nothello():
    assert value("hi") == 20
    assert value("Hi") == 20

def test_value_else():
    assert value("test") == 100
    assert value("Test") == 100

