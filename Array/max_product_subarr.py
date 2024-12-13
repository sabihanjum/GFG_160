"""Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the output fits in a 32-bit integer."""

# User function Template for python3
class Solution:

    # Function to find maximum product subarray
    def maxProduct(self, arr):
        n = len(arr)
        maxProd = float('-inf')

        # LeftToRight to store product from left to right
        leftToRight = 1

        # RightToLeft to store product from right to left
        rightToLeft = 1

        for i in range(n):
            if leftToRight == 0:
                leftToRight = 1
            if rightToLeft == 0:
                rightToLeft = 1

            # Calculate product from index left to right
            leftToRight *= arr[i]

            # Calculate product from index right to left
            j = n - i - 1
            rightToLeft *= arr[j]

            # Update max product
            maxProd = max(leftToRight, rightToLeft, maxProd)

        return maxProd
