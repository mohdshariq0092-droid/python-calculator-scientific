from calculator.scientific import power, sqrt
import pytest

@pytest.mark.sanity
def test_power():
    assert power(2, 3) == 8

@pytest.mark.sanity
def test_sqrt():
    assert sqrt(9) == 3


@pytest.mark.regression
def test_power_reg():
    print("Regression test case")
    assert power(3, 2) == 8

