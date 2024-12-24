"""Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]."""
def lower_bound(arr, target):
    res = len(arr)
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] >= target:
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res
    
def upper_bound(arr, target):
    res = len(arr)
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] > target:
            res = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return res

class Solution:
    def countFreq(self, arr, target):
        return upper_bound(arr, target) - lower_bound(arr, target)