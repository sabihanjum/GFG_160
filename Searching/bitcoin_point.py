"""Given an array of integers arr[] that is first strictly increasing and then maybe strictly decreasing, find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing."""

class Solution:

    def findMaximum(self, arr):
        n = len(arr)
        
        # Check if the first element is maximum
        if n == 1 or arr[0] > arr[1]:
            return arr[0]
        
        # Check if the last element is maximum
        if arr[n-1] > arr[n-2]:
            return arr[n-1]
    
        # Binary search to find the peak (maximum element)
        lo, hi = 1, n - 2  # Search space excludes first and last element (already checked)
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            # If the element at mid is maximum, return it
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return arr[mid]
            
            # If the next element is greater, the maximum exists in the right subarray
            if arr[mid] < arr[mid+1]:
                lo = mid + 1
            
            # Otherwise, it exists in the left subarray
            else:
                hi = mid - 1
        
        # This return statement is just a fallback for safety
        return arr[hi]
