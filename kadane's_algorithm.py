"""Given an integer array arr[]. You need to find the maximum sum of a subarray."""
#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        res = arr[0]
        maxEnding = arr[0]
        for i in range(1, len(arr)):
            #find the maximum sum ending atindex i by either extending
            #the maximum sum aubarray end at index i - 1 or by
            #starting a new subarray from index i
            maxEnding = max(maxEnding + arr[i], arr[i])
            
            #update res if mximum subarray sum ending at index i > res
            res = max(res, maxEnding)
        return res