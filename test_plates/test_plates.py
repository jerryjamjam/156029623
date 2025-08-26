
import plates
from plates import is_valid



def test_is_valid_platelessthan2():
    assert is_valid("a") == False

def test_is_valid_zerofirst():
    assert is_valid("ABC012") == False

def test_is_valid_alnum():
    assert is_valid("ABC!23") == False

def test_is_valid_0indexisalpha():
    assert is_valid("111111") == False

def test_is_valid_numplacement():
    assert is_valid("AB12CD") == False

