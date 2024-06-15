"""
    You are given an array prices where prices[i] 
    is the price of a given stock on the ith day.

    You want to maximize your profit by choosing 
    a single day to buy one stock and choosing a 
    different day in the future to sell that stock.

    Return the maximum profit you can achieve from 
    this transaction. 

    If you cannot achieve any profit, return 0.
"""

"""
    O(n) time complexity
    O(n) space alocation
"""

def maxProfit(prices):
    profit = 0
    buy = prices[0]

    for value in prices[1:]:
        if value > buy:
            profit = max(profit, value - buy)
        else:
            buy = value

    return profit


if __name__== "__main__":
    prices = [7,1,5,3,6,4]
    maxProfit(prices)

