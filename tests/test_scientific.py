from calculator.scientific import power, sqrt

def test_power():
    assert power(2, 3) == 8

def test_sqrt():
    assert sqrt(9) == 3
