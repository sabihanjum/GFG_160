"""Given an integer array arr[ ], your task is to find the minimum number of increment operations required to make all the array elements unique. i.e. no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.

Note: The answer will always fit into a 32-bit integer."""

class Solution:
    def minIncrements(self, arr): 
        n = len(arr)
        cnt = 0
        
        #find the maximum elemnt in thar array
        mx = max(arr)
        freq = [0]*(n+mx)
        
        #find the frequency of all element from the model
        for ele in arr:
            freq[ele] += 1
            
        for num in range(len(freq)):
            #if there is more than one occurence of the num
            if freq[num] > 1:
                #increment all extra occurence by 1
                freq[num + 1] += freq[num] - 1
                
                #count this increment operation
                cnt += freq[num] - 1
                freq[num] = 1
                
        return cnt