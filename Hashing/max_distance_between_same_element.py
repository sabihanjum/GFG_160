""""""

class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        mp = {}
        res = 0
        
        for i in range(len(arr)):
            if arr[i] not in mp:
                mp[arr[i]] = i
            else:
                res = max(res, i - mp[arr[i]])
                
        return res