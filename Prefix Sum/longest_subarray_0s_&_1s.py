"""Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s."""

class Solution:
    def maxLen(self, arr):
        # code here
        mp = {}
        prefSum = 0
        res = 0
        
        #Traverse throught the given array
        for i in range(len(arr)):
            #Add current element to 1
            #If current element is zero n -1
            prefSum += -1 if arr[i] == 0 else 1
            
            #to handle sum = 0 at last index
            if prefSum == 0:
                res = i + 1
                
            #if sum is seen before then update result with max
            if prefSum in mp:
                res = max(res, i - mp[prefSum])
                
            #else put this sum in hash table
            else:
                mp[prefSum] = i
        return res
