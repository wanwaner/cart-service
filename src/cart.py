"""购物车金额计算。"""
from decimal import Decimal


def line_total(unit_price, quantity):
    """单行小计。"""
    return Decimal(str(unit_price)) * quantity


def apply_discount(subtotal, percent):
    """按百分比打折，percent 为 0-100 的折扣幅度。

    percent 超出 [0, 100] 时抛 ValueError，避免出现负数金额或反向加价。
    """
    percent = Decimal(str(percent))
    if percent < 0 or percent > 100:
        raise ValueError("percent 必须在 [0, 100] 范围内")
    return subtotal * (Decimal(100) - percent) / Decimal(100)


def cart_total(items, discount_percent=0):
    """计算购物车总额。

    items: [{"unitPrice": 9.9, "quantity": 2}, ...]
    quantity 为负数时抛 ValueError，避免总额被算成负数。
    """
    subtotal = Decimal(0)
    for item in items:
        quantity = item["quantity"]
        if quantity < 0:
            raise ValueError("quantity 不能为负数")
        subtotal += line_total(item["unitPrice"], quantity)
    return apply_discount(subtotal, discount_percent)
