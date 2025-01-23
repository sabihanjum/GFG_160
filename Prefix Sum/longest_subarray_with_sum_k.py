"""Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0."""

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        mp = {}
        res = 0
        prefSum = 0
        for i in range(len(arr)):
            prefSum += arr[i]
            
            #check if the entire prefixsum to k
            if prefSum == k:
                res = i + 1
                
            #if prefSum -k exist in the map then there exist such
            #subarray from (index of previos prefix + 1) to i
            elif (prefSum - k) in mp:
                res = max(res, i - mp[prefSum - k])
            #store only first occurrence index of prefSum
            if prefSum not in mp:
                mp[prefSum] = i
                
        return res