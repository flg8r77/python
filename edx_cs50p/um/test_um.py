from um import count

def test_um_standalone():
    assert count("Hello um world, my name is um uh hmm, I forgot") == 2

def test_um_substring():
    assert count("This is so um Yummy") == 1

def test_um_none():
    assert count("Hello people of earth") == 0

def test_um_caseinsensitive():
    assert count("Hello um world, my name is UM UM uh hmm, well I forgot") == 3