"""Given a sorted and rotated array arr[] of distinct elements, the task is to find the index of a target key. Return -1 if the key is not found."""

class Solution:
    def search(self, arr, key):
        lo = 0
        hi = len(arr) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            # if key found, return the index
            if arr[mid] == key:
                return mid
            
            # if left half is sorted
            if arr[mid] >= arr[lo]:
                # if key lies within this sorted half
                if key >= arr[lo] and key < arr[mid]:
                    hi = mid - 1
                # otherwise, move lo pointer to mid + 1
                else:
                    lo = mid + 1
            # if right half is sorted
            else:
                # if key lies within this sorted half
                if key > arr[mid] and key <= arr[hi]:
                    lo = mid + 1
                # otherwise, move hi pointer to mid - 1
                else:
                    hi = mid - 1
        return -1  # key is not found in the array
