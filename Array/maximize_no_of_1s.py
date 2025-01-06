"""Given a binary array arr[] (containing only 0s and 1s) and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times."""

class Solution:
    # k is the maximum number of zeros allowed to flip
    def maxOnes(self, arr, k):
        res = 0
        
        #start and end pointer of the window
        start = 0
        end = 0
        
        #counter to keep track of zeros in current window
        cnt = 0
        
        while end < len(arr):
            if arr[end] == 0:
                cnt += 1
                
            #shrink the window from left if no. of 
            #zeroes are greater than k
            while cnt > k:
                if arr[start] == 0:
                    cnt -= 1
                start += 1
            
            res = max(res, (end - start + 1))
            
            #increment the end pointer to expand the window
            end += 1
        return res