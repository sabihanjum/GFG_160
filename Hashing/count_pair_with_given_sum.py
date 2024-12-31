"""Given an array arr[] and an integer target. You have to find numbers of pairs in array arr[] which sums up to given target."""

class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        freq = {}
        cnt = 0
        
        for i in range(len(arr)):
            #check if the compliment target - arr[i] is exist in map
            #if yes, increment the count
            if (target - arr[i]) in freq:
                cnt += freq[target-arr[i]]
                
            #increment the frequency of arr[i]
            freq[arr[i]] = freq.get(arr[i], 0) + 1
        return cnt