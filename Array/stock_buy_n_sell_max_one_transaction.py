"""Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold."""

class Solution:
    def maximumProfit(self, prices):
        minSoFar = prices[0]
        res = 0
        
        #update the minimum value seen so far
        #if we see smaller
        for i in range(1, len(prices)):
            minSoFar = min(minSoFar, prices[i])
            
            #update results if we get more profit
            res = max(res, prices[i] - minSoFar)
        return res