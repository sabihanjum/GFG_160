"""Given an array arr[] and an integer target, the task is to find the sum of three integers in arr[] such that the sum is closest to target. 

Note: If multiple sums are closest to target, return the maximum one."""

class Solution:
    def closest3Sum(self, arr, target):
        # code here
        res = 0
        minDiff = float('inf')
        flag = 0
        
        n = len(arr)
        arr.sort()
        
        for i in range(n-2):
            l = i+1
            r = n-1
            while l < r:
                sum = arr[i]+arr[l]+arr[r]
                if abs(sum-target)<minDiff:
                    minDiff = abs(sum-target)
                    res = sum
                elif abs(sum-target)==minDiff:
                    res = max(res, sum)
                
                if sum>target:
                    r-=1
                elif sum<target:
                    l+=1
                else:
                    flag-1
                    break
        
            if flag == 1:
                break
        return res