# You are given an integer array prices where prices[i] is the price of a
# given stock on the ith day. On each day, you may decide to buy and/or sell
# the stock. You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

def buy(price):
    pass


def max_profit(prices):
    i = 0
    credit = 0
    buy_price = 0
    stock = False
    while i < len(prices) - 1:
        curr = prices[i]
        next = prices[i + 1]
        if curr < next and not stock:
            stock = True
            credit -= prices[i]
            buy_price = prices[i]
            i += 1
            continue
        elif prices[i] > buy_price > prices[i + 1] and stock:
            stock = False
            credit += prices[i]
            buy_price = prices[i]
            i += 1
            continue
        i += 1
    return credit

print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([1,2,3,4,5]))

# Input: prices = [7,1,5,3,6,4] Output: 7
