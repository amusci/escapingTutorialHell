"""
You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
and the starting inventory. Return the total profit made, rounded to the nearest dollar.
"""


def profit(info):
    sum = round((info["sell_price"] - info["cost_price"]) * info["inventory"])
    return sum