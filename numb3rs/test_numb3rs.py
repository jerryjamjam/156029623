import pytest
from numb3rs import validate

def test_validate_valid():
    assert validate("255.0.0.0") == True

def test_validate_invalid():
    assert validate("260.0.0.0") == False

def test_validate_nope():
    assert validate("250.260.260.260") == False
