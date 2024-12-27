"""Given a sorted array of distinct positive integers arr[], we need to find the kth positive number that is missing from arr[]. """

class Solution:
    def kthMissing(self, arr, k):
        lo = 0
        hi = len(arr) - 1
        res = len(arr) + k
        
        #binary search for index where arr[i] > i+k
        while lo <= hi:
            mid = (lo + hi)// 2
            if arr[mid] > mid + k:
                res = mid + k
                hi = mid - 1
            else:
                lo = mid + 1
                
        return res