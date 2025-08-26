import pytest
import sys
from um import main
from um import count

def test_main_output(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: "hey, ummm")

    main()
    out, err = capfd.readouterr()
    assert out.strip() == "0"

def test_count():
    assert count("Um") == 1
    


