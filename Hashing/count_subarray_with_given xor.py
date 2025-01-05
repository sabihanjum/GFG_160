"""Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k."""

class Solution:
    def subarrayXor(self, arr, k):
        res = 0
        
        #create map that stores number of prefix array 
        #corresponding to a XOR value
        mp = {}
        
        prefXOR = 0
        for val in arr:
            #find XOR of current prefix
            prefXOR ^= val
            
            #if prefXOR ^ k exist in mp then there is subarray 
            #ending at i with XOR = k
            res += mp.get(prefXOR ^ k, 0)
            
            #if this prefix subarray has XOR equal to k
            if prefXOR == k:
                res += 1
                
            #add the XOR of this subarray to map
            mp[prefXOR] = mp.get(prefXOR, 0) + 1
        
        #return total count of subarray having XOR of element
        #as given value k
        return res