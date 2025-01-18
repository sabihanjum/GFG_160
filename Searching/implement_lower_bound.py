"""Given a sorted array arr[] and a number target, the task is to find the lower bound of the target in this given array. The lower bound of a number is defined as the smallest index in the sorted array where the element is greater than or equal to the given number.

Note: If all the elements in the given array are smaller than the target, the lower bound will be the length of the array. """

class Solution:
    def lowerBound(arr, target):
        lo = 0
        hi = len(arr) - 1
        res = len(arr)
    
        while lo <= hi:
            mid = lo + (hi - lo) // 2
        
            # If arr[mid] >= target, then mid can be the
            # lower bound, so update res to mid and
            # search in left half, i.e. [lo...mid-1]
            if arr[mid] >= target:
                res = mid
                hi = mid - 1
            
            # If arr[mid] < target, then lower bound
            # cannot lie in the range [lo...mid] so
            # search in right half, i.e. [mid+1...hi]
            else:
                lo = mid + 1
            
        return res