"""购物车金额计算。"""
from decimal import Decimal


def line_total(unit_price, quantity):
    """单行小计。"""
    return Decimal(str(unit_price)) * quantity


def apply_discount(subtotal, percent):
    """按百分比打折，percent 为 0-100 的折扣幅度。

    BUG: 没有校验 percent 范围，percent>100 会得到负数金额；
    percent 为负数时反而加价。
    """
    return subtotal * (Decimal(100) - Decimal(str(percent))) / Decimal(100)


def cart_total(items, discount_percent=0):
    """计算购物车总额。

    items: [{"unitPrice": 9.9, "quantity": 2}, ...]
    BUG: quantity 为负数时不报错，可以把总额算成负的。
    """
    subtotal = Decimal(0)
    for item in items:
        subtotal += line_total(item["unitPrice"], item["quantity"])
    return apply_discount(subtotal, discount_percent)
