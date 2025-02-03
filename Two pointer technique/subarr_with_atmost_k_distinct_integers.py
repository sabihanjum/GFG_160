"""You are given an array arr[] of positive integers and an integer k, find the number of subarrays in arr[] where the count of distinct integers is at most k.

Note: A subarray is a contiguous part of an array."""

from collections import defaultdict

class Solution:
    def atMostK(self, arr, k):
        # Code here
        res = 0
        n = len(arr)
        
        freq = defaultdict(int)
        
        i = 0
        j = 0
        
        for j in range(n):
            freq[arr[j]] += 1
            
            if freq[arr[j]] == 1:
                k -= 1
                
            while k < 0:
                freq[arr[i]] -= 1
                if freq[arr[i]] == 0:
                    k += 1
                i += 1
            res += (j-i+1)
        return res