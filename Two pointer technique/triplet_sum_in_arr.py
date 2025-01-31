"""Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

Return true if such a triplet exists, otherwise, return false."""

class Solution:
    # Function to find if there exists a triplet in the array arr[] which sums up to target.
    def hasTripletSum(self, arr, target):
        # Your Code Here
        n = len(arr)
        arr.sort()
        
        for i in range(n-2):
            l = i + 1
            r = n - 1
            
            reqSum = target - arr[i]
            
            while l < r:
                if arr[l]+arr[r] == reqSum:
                    return True
                elif arr[l]+arr[r]>reqSum:
                    r-=1
                else:
                    l+=1
        return False