"""Given an array arr[] denoting heights of N towers and a positive integer K.
For each tower, you must perform exactly one of the following operations exactly once.
Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.
You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers."""

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)  # Length of the array
        arr.sort()  # Sort the array
        
        # If we increase all heights by k or decrease all
        # heights by k, the result will be arr[n - 1] - arr[0]
        res = arr[n - 1] - arr[0]

        # For all indices 1 to n-1, increment arr[0..i-1] by k
        # and decrement arr[i..n-1] by k
        for i in range(1, len(arr)):
            # Impossible to decrement height of ith tower by k,
            # continue to the next tower
            if arr[i] - k < 0:
                continue
            
            # Minimum height after modification
            minH = min(arr[0] + k, arr[i] - k)

            # Maximum height after modification
            maxH = max(arr[i - 1] + k, arr[n - 1] - k)

            # Store the minimum difference as result
            res = min(res, maxH - minH)

        return res
