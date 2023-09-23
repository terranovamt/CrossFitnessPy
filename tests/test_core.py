from srcs.core import func, add, main

def test_answer():
    assert func(3) == 4
    assert func(2) == 3
    assert func(1) == 2
    assert add(1,2) == 3


def test_main():
    assert main() == 0
