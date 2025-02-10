"""Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1]."""

class Solution:
    def subarraySum(self, arr, target):
        # code here
        s, e = 0, 0
        res = []
        curr = 0
        
        for i in range(len(arr)):
            curr += arr[i]
            
            if curr >= target:
                e = i
                while curr > target and s < e:
                    curr -= arr[s]
                    s += 1
                if curr == target:
                    res.append(s+1)
                    res.append(e+1)
                    return res
        return [-1]