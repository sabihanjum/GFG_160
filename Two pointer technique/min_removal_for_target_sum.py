"""You are given an array of positive integers arr[] and an integer k. In one operation, you can remove either the leftmost or the rightmost element from the array. After each operation, the size of arr[] will be reduced by one.

Your task is to determine the minimum number of operations required to make the total sum of removed elements exactly equal to k. If it is not possible to achieve this, return -1."""

class Solution:
    def minRemovals(self, arr, k):
        # code here
        n = len(arr)
        sum = 0
        l = 0
        r = 0
        
        maxL = -1
        total = 0
        
        for i in range(n):
            total += arr[i]
        total -= k
        
        if total == 0:
            return n
        for r in range(n):
            sum += arr[r]
            
            while l<r and sum>total:
                sum -= arr[l]
                l+=1
                
            if sum == total:
                maxL = max(maxL, r-l+1)
        if maxL == -1:
            return -1
        else:
            return n - maxL