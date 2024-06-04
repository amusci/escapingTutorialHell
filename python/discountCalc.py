def dis(price, discount):

    before_change = price * (discount / 100)
    final = price - before_change
    return round(final, 2)