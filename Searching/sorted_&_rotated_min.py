"""A sorted array of distinct elements arr[] is rotated at some unknown point, the task is to find the minimum element in it. """

class Solution:
    def findMin(self, arr):
        lo, hi = 0, len(arr)-1
        
        while lo < hi:
            #the current subarray already sorted
            #the min is at the low index
            if arr[lo] < arr[hi]:
                return arr[lo]
                
            #we reach hear when we have at least 2 elements and
            #currect subarray is rotated
            mid = (lo + hi) // 2
            
            #the right half is not sorted so the min element
            #must be in right half
            if arr[mid] > arr[hi]:
                lo = mid + 1
                
            #the right haf is sorted note that in this case we don't 
            #change high to mid - 1 but keep it to mid.
            #as the mid element itself smallest
            else:
                hi = mid
        return arr[lo]
        
        #Tc  = O(logn)
        #SC = O(1)