"""You are given two positive integers n and m, and an integer array arr[] containing total (n*m) elements. Return a 2D matrix of dimensions n x m by filling it in a clockwise spiral order using the elements from the given array."""

class Solution:
    def spiralFill(self, n, m, arr):
        # code here
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        #boundary variables
        top, bottom, left, right = 0, n - 1, 0 , m - 1
        index = 0
        
        while index < len(arr):
            #traverse top row from left to right
            for j in range(left, right+1):
                res[top][j] = arr[index]
                index += 1
            top += 1
            
            #traverse the right most column from top to bottom
            for i in range(top, bottom + 1):
                res[i][right] = arr[index]
                index += 1
            right -= 1
            
            #traverse the bottom most rows from right to left
            if top <= bottom:
                
                for j in range(right, left - 1, -1):
                    res[bottom][j] = arr[index]
                    index += 1
                bottom -= 1

            #traverse the left most column from bottom to up
            if left <= right:
                
                for i in range(bottom, top-1, -1):
                    res[i][left] = arr[index]
                    index += 1
                left += 1
        return res