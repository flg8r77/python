from numb3rs import validate

def test_incomplete_octets():
    assert validate("1") == False
    assert validate("1.1") == False
    assert validate("1.1.1") == False

def test_octet_outofrange():
    assert validate("1.1.1.256") == False
    assert validate("1.1.256.1") == False
    assert validate("1.256.1.1") == False
    assert validate("256.1.1.1") == False

def test_garbage():
    assert validate("Garbage Input") == False

def test_valid_IP():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.190") == True

