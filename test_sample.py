def func(a, b):
    return a + b

def test_func():
    assert 3 == func(1, 2)
    assert 4 == func(1, 3)
    assert 4 == func(1, 5)    