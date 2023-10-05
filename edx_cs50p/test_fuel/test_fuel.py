
import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("2/4") == 50

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("cat/3")
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("5/3")

def test_convert_zerodivisionerror():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_guage():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"