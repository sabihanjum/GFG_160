"""Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. 

A triangle with three given sides is only possible if sum of any two sides is always greater than the third side."""

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        res = 0
        arr.sort()
        
        for i in range(2, len(arr)):
            left, right = 0, i - 1
            
            while left < right:
                if arr[left] + arr[right] > arr[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res