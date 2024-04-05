def max_profit(prices):
    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    if max_profit < 0:
        return 0
    else:
        return max_profit


prices = [1,2,3,4,5]
print(max_profit(prices))