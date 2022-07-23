# You are given an integer array prices where prices[i] is the price of a
# given stock on the ith day. On each day, you may decide to buy and/or sell
# the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

def max_profit(prices):
    i = 0
    credit = 0
    buy_price = 0
    stock = False
    while i < len(prices) - 1:
        curr = prices[i]
        nxt = prices[i + 1]
        if curr < nxt and not stock:
            stock = True
            credit -= prices[i]
            buy_price = prices[i]
            i += 1
            continue
        elif buy_price < curr > nxt and stock:
            stock = False
            buy_price = curr
            credit += buy_price
            i += 1
            continue
        i += 1
    if stock:
        buy_price = nxt
        credit += buy_price
    return credit


assert max_profit([6, 1, 3, 2, 4, 7]) == 7
assert max_profit([7, 1, 5, 3, 6, 4]) == 7
assert max_profit([1, 2, 3, 4, 5]) == 4
assert max_profit([1, 2]) == 1
