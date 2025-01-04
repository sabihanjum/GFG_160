"""Given an unsorted array of integers, find the number of continuous subarrays having sum exactly equal to a given number k."""

class Solution:
    def countSubarrays(self, arr, k):
        #Dictionary to store prefix sums frequencies
        prefixSums = {}
        res = 0
        currSum = 0
        
        for val in arr:
            #add curr element to sum so far
            currSum += val
            
            #if currSum is equal to desired sum, then a new subarray is found
            if currSum == k:
                res += 1
                
            #check if the difference exist in the prefixSums dictionary
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
                
            #Add currSums to the dictionary of prefix sum
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        return res


