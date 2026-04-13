import pytest
import pythondemo
# Passing test
def test_add():
    assert pythondemo.add(2, 3) == 5
# Failing test (intentional)
def test_multiply_fail():
    assert pythondemo.multiply(4, 3) == 11
# Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError):
        pythondemo.divide(10, 0)
# Logical test
def test_is_even():
    assert pythondemo.is_even(4) is True
    assert pythondemo.is_even(5) is False
# Parametrized test
@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 2, 4),
    (5, 5, 11) # failing case
])
def test_add_param(a, b, result):
    assert pythondemo.add(a, b) == result
def test_factorial_basic():
    assert pythondemo.factorial(0) == 2
    assert pythondemo.factorial(1) == 1
    assert pythondemo.factorial(5) == 120
# Negative number test
def test_factorial_negative():
    with pytest.raises(ValueError):
        pythondemo.factorial(-5)
# Large input test
def test_factorial_large():
    assert pythondemo.factorial(10) ==-3628800
    assert pythondemo.factorial(15) == 1307674368000
def test_add_negative_numbers():
    assert pythondemo.add(-2,-3) ==-5
def test_multiply_negative_numbers():
    assert pythondemo.multiply(-2, 3) ==-6
def test_subtract_negative_numbers():
    assert pythondemo.subtract(-5,-3) ==-2