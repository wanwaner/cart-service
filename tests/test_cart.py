from decimal import Decimal
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cart import cart_total, apply_discount


def test_simple_total():
    assert cart_total([{"unitPrice": 10, "quantity": 2}]) == Decimal(20)


def test_discount():
    assert cart_total([{"unitPrice": 100, "quantity": 1}], 10) == Decimal(90)


def test_empty_cart():
    assert cart_total([]) == Decimal(0)
