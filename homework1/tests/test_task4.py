import pytest
import src.task4 as task4

#test parameters
@pytest.mark.parametrize("price, discount, expected", [
    (100, 10, 90.0),
    (50.0, 20, 40.0),
    (200, 0, 200),
    (500, 100, 0)
])

#confirming price
def test_calculate_discount_valid(price, discount, expected):
    assert task4.calculate_discount(price, discount) == expected

#value error check
def test_invalid_discount():
    with pytest.raises(ValueError):
        task4.calculate_discount(100, -5)
    with pytest.raises(ValueError):
        task4.calculate_discount(100, 150)

#type error check
def test_invalid_type():
    with pytest.raises(TypeError):
        task4.calculate_discount("100", 10)
    