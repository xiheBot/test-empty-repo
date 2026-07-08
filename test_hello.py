from hello import greet


def test_greet_default():
    assert greet() == "👋 Hello, World!"


def test_greet_custom():
    assert greet("xiheBot") == "👋 Hello, xiheBot!"


def test_greet_chinese():
    assert greet("世界") == "👋 Hello, 世界!"
