from twttr import shorten

def test_shorten_upper():
    assert shorten("HELLO THERE BUDDY!") == "HLL THR BDDY!"

def test_shorten_lower():
    assert shorten("hello there buddy!") == "hll thr bddy!"

def test_shorten_mixed():
    assert shorten("HELLO! there BUDDY") == "HLL! thr BDDY"

def test_shorten_numbers():
    assert shorten("Hello there my 42 friends!") == "Hll thr my 42 frnds!"
