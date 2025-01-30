"""Given an array arr[] and an integer target, you need to find and return the count of quadruplets such that the index of each element of the quadruplet is unique and the sum of the elements is equal to target."""

class Solution:
    def countSum(self, arr, target):
        #code here
        mp = defaultdict(int)
        res = 0
        
        for j in range(len(arr)):
            for k in range(j+1, len(arr)):
                res += mp[target - arr[j] - arr[k]]
            for i in range(j):
                mp[arr[i]+arr[j]]+=1
        return res