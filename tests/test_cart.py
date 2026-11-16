from decimal import Decimal
import sys, os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cart import cart_total, apply_discount


def test_simple_total():
    assert cart_total([{"unitPrice": 10, "quantity": 2}]) == Decimal(20)


def test_discount():
    assert cart_total([{"unitPrice": 100, "quantity": 1}], 10) == Decimal(90)


def test_empty_cart():
    assert cart_total([]) == Decimal(0)


def test_discount_upper_bound():
    assert cart_total([{"unitPrice": 100, "quantity": 1}], 100) == Decimal(0)


def test_discount_zero():
    assert cart_total([{"unitPrice": 100, "quantity": 1}], 0) == Decimal(100)


def test_discount_over_100_raises():
    with pytest.raises(ValueError):
        apply_discount(Decimal(100), 101)


def test_discount_negative_raises():
    with pytest.raises(ValueError):
        apply_discount(Decimal(100), -1)


def test_negative_quantity_raises():
    with pytest.raises(ValueError):
        cart_total([{"unitPrice": 10, "quantity": -1}])
