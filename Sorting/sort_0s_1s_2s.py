"""Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order."""
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr)
        lo = 0
        hi = n - 1
        mid = 0
        
        #iterate till all the element are sorted
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo = lo + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid = mid + 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi = hi - 1
        return arr


