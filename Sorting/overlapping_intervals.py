"""Given an array of Intervals arr[][], where arr[i] = [starti, endi]. The task is to merge all of the overlapping Intervals."""

class Solution:
    def mergeOverlap(self, arr):
        # Sort intervals based on start value
        arr.sort()
        
        # Initialize result list with the first interval
        res = [arr[0]]
        
        for i in range(1, len(arr)):
            last = res[-1]  # Last merged interval
            curr = arr[i]   # Current interval
            
            # If current interval overlaps with the last merged interval, merge them
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])  # Update the end of the last interval
            else:
                res.append(curr)  # Otherwise, add the current interval to the result
                
        return res


