import math
import pytest
from calculator import calc

@pytest.mark.parametrize(
    "a,b,expected",
    [(1, 2, 3), (-1, 2, 1), (2.5, 0.5, 3.0)]
)
def test_add(a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(5, 2, 3), (2, 5, -3), (2.5, 0.5, 2.0)]
)
def test_subtract(a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(3, 4, 12), (-2, 5, -10), (2.5, 0.5, 1.25)]
)
def test_multiply(a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [(10, 2, 5.0), (7, 2, 3.5), (-9, 3, -3.0)]
)
def test_divide(a, b, expected):
    assert math.isclose(calc.divide(a, b), expected, rel_tol=1e-9)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(1, 0)
