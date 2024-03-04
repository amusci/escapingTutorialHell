"""

Create a function that calculates the profit margin given cost_price and sales_price.

Return the result as a percentage formatted string, and rounded to one decimal.

To calculate profit margin you subtract the cost from the sales price, then divide by sales price.

"""


def profit_margin(cost_price, sales_price):
    ans = round(((sales_price - cost_price) / sales_price)* 100,1)
    return '{}%'.format(str(ans))