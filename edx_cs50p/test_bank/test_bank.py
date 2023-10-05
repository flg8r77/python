from bank import value

def test_greeting_hello():
    assert value("hello friend") == 0
    assert value("Hello friend") == 0

def test_greeting_h():
    assert value("how are you?") == 20
    assert value("How are you?") == 20

def test_greeting_allelse():
    assert value("what's up!") == 100
    assert value("What's up!") == 100
    
