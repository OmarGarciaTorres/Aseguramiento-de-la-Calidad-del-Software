from example import greet

def test_greet():
    assert greet("CI Pipeline") == "Hello, CI Pipeline!"
