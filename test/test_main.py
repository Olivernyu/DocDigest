from mypackage import main


def test_hello_world():
    assert main.hello_world() == "Hello, World!"


def test_math():
    assert 2 + 2 == 4
