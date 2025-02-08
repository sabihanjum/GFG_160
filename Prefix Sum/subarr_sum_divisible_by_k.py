"""You are given an integer array arr[] and a value k. The task is to find the count of all sub-arrays whose sum is divisible by k."""

#{ 
# Driver Code Starts
# Initial Template for Python 3
from collections import defaultdict


# } Driver Code Ends
class Solution:
    # Function to count the number of subarrays with a sum that is divisible by K
    def subCount(self, arr, k):
        # Your code goes here
        n = len(arr)
        res = 0
        sum = 0
        
        prefIdx = defaultdict(int)
        
        for i in range(n):
            sum = (sum+arr[i])%k
            res = res+prefIdx[sum]
            if sum == 0:
                res += 1
            prefIdx[sum] += 1
        return res

