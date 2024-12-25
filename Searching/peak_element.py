"""Given an array arr[] where no two adjacent elements are same, find the index of a peak element. An element is considered to be a peak if it is greater than its adjacent elements (if they exist). If there are multiple peak elements, return index of any one of them. The output will be "true" if the index returned by your function is correct; otherwise, it will be "false".

Note: Consider the element before the first element and the element after the last element to be negative infinity."""

class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        
        #if there is only element then it is peak
        if n == 1:
            return 0
        
        #check if the first element is a peak
        if arr[0] > arr[1]:
            return 0
            
        #check if the last elemnt is a peak
        if arr[n-1] >arr[n-2]:
            return n-1
        
        #search space for binary search
        lo, hi = 1, n-2
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            #if the element at mid is a peak element return mid
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
                
            #If next neighbor is greater than peak
            #element will exist in the right sub array
            if arr[mid] < arr[mid+1]:
                lo = mid + 1
            
            #other wise exist in left subarray
            else:
                hi = mid - 1
            