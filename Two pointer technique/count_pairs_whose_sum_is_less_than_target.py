"""Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target."""

class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        cnt = 0
        arr.sort()
        n = len(arr)
        
        l = 0
        r = n-1
        while l<r:
            if arr[l]+arr[r] < target:
                cnt += (r-l)
                l+=1
            else:
                r -= 1
        return cnt