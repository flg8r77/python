from working import convert
import pytest

def test_incorrect_format():
    with pytest.raises(ValueError):
        assert convert("10 AM - 5 PM")

def test_incorrect_hrs():
    with pytest.raises(ValueError):
        assert convert("13 PM to 17 PM")

def test_incorrect_mins():
    with pytest.raises(ValueError):
        assert convert("1:60 PM to 5:80 PM")

def test_correct_inputs():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("11:30 AM to 4:01 PM") == "11:30 to 16:01"