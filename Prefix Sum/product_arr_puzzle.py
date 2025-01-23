"""Given an array, arr[] construct a product array, res[] where each element in res[i] is the product of all elements in arr[] except arr[i]. Return this resultant array, res[].
Note: Each element is res[] lies inside the 32-bit integer range."""

class Solution:
    def productExceptSelf(self, arr):
        #code here
        zeros = 0
        idx = -1
        prod = 1
        
        #count zeros and track the index of zeros
        for i in range(len(arr)):
            if arr[i] == 0:
                zeros += 1
                idx = i
            else:
                prod *= arr[i]
        res = [0] * len(arr)
        
        #if no zero calculate the product for all element
        if zeros == 0:
            for i in range(len(arr)):
                res[i] = prod // arr[i]
                
        #if one zero set product only at the zeros index
        elif zeros == 1:
            res[idx] = prod
        return res