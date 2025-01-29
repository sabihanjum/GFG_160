"""Given an array of distinct positive numbers, the task is to calculate the minimum number of subsets (or subsequences) from the array such that each subset contains consecutive numbers."""

class Solution:
    def numOfSubset(self, arr):
        # Your code goes here
        s = set(arr)
        count = 0
        for i in range(len(arr)):
            if arr[i]-1 not in s:
                count += 1
        return count