from seasons import get_dob
import pytest

def test_exit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"Hello-oo-oo")
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_dob()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == "Invalid date"

def test_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _:"1970-01-01")
    i = input("Date of Birth (YYYY-MM-DD): ")
    assert get_dob() == [1970, 1, 1]