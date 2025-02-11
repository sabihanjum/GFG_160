"""Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. """

class Solution:
    def maxWater(self, arr):
        # code here
        left = 1
        right = len(arr)-2
        
        lMax = arr[left-1]
        rMax = arr[right+1]
        
        res = 0
        while left <= right:
            if rMax <= lMax:
                res += max(0, rMax - arr[right])
                
                rMax = max(rMax, arr[right])
                right -= 1
            else:
                res += max(0, lMax - arr[left])
                lMax = max(lMax, arr[left])
                left += 1
        return res