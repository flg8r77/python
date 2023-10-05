from plates import is_valid


def test_validlength():
    assert is_valid("FLORIDA") == False
    assert is_valid("FLORID") == True
    assert is_valid("FL") == True
    assert is_valid("F") == False

def test_firsttwochars():
    assert is_valid("F16") == False
    assert is_valid("FX16") == True

def test_alphanumonly():
    assert is_valid("fx-16") == False
    assert is_valid("FX.16") == False

def test_numbercheck():
    assert is_valid("FX016") == False
    assert is_valid("FX160") == True
    assert is_valid("fx16xf") == Falsete