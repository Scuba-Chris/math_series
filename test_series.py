from series import fibonacci, lucas, sum_series

def test_zero():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_one():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_two():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual

def test_zero_lucas():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_one_lucas():
    expected = 1
    actual = lucas(1)
    assert expected == actual

def test_two_lucas():
    expected = 3
    actual = lucas(2)
    assert expected == actual

def test_3_lucas():
    expected = 29
    actual = lucas(7)
    assert expected == actual