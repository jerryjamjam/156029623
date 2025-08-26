import pytest
from seasons import birth_date_conversion, word_conversion
from datetime import date

birthday = date(1999, 1, 1)
today = date(2000, 1, 1)

def test_birth_date_conversion():
    minutes = birth_date_conversion(birthday, today)
    assert minutes == 525600

word = 525600
def test_word_conversion():
    word = word_conversion(525600)
    assert word == "Five hundred twenty-five thousand, six hundred"
