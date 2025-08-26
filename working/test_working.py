import pytest
import sys
from working import main

def test_main_output(monkeypatch, capfd):
    monkeypatch.setattr('builtins.input', lambda _: "8:00 PM to 8:00 AM")

    main()
    out, err = capfd.readouterr()
    assert out.strip() == "20:00 to 08:00"

def test_main_to(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "8 AM 5 PM")
    with pytest.raises(ValueError):
        main()

def test_main_range(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "13 AM 13 PM")
    with pytest.raises(ValueError):
        main()

