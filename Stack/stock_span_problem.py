"""The stock span problem is a financial problem where we have a series of daily price quotes for a stock and we need to calculate the span of stock price for all days. The span arr[i] of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day."""

class Solution:
    def calculateSpan(arr):

        n = len(arr)
        span = [0] * n  
        stk = []

        # Process each day's price
        for i in range(n):

            # Remove elements from the stack while the current
            # price is greater than or equal to stack's top price
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()

            # If stack is empty, all elements to the left are smaller
            # Else, top of the stack is the last greater element's index
            if not stk:
                span[i] = (i + 1)
            else:
                span[i] = (i - stk[-1])

            # Push the current index to the stack
            stk.append(i)

        return span