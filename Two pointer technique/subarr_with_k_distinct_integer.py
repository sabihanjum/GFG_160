"""You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is exactly k.

Note: A subarray is a contiguous part of an array."""

from collections import defaultdict
class Solution:
    def atMost(self, arr, k):
        n = len(arr)
        res = 0
        dist = 0
            
        freq = defaultdict(int)
            
        l = 0
        r = 0
            
        for r in range(n):
            freq[arr[r]] += 1
            if freq[arr[r]] == 1:
                dist += 1
                    
            while dist > k:
                freq[arr[l]] -= 1
                if freq[arr[l]] == 0:
                    dist -= 1
                l += 1
                    
            res += (r-l+1)
        return res
    def exactlyK(self, arr, k):
        # Code here
        return self.atMost(arr, k) - self.atMost(arr, k-1)