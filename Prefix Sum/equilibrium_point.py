"""Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements before that index is the same as the sum of elements after it. Return -1 if no such point exists. """

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        n = len(arr)
        total_sum = sum(arr)
        left_sum = 0
        for i in range(n):
            total_sum -= arr[i]  #total sum is now right sum
    
            if left_sum == total_sum:
                return i
            
            left_sum += arr[i]
            
        return -1