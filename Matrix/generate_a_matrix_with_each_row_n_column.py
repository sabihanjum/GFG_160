"""Given two integer arrays rowSum[] of size n and colSum[] of size m, the task is to construct a 2D matrix of size n x m such that the sum of matrix elements in ith row is rowSum[i] and the sum of matrix elements in jth column is colSum[j].
Note: Since multiple answers are possible, return any one of them. 
Arrays are generated such that answer is always possible.
The driver code will print true if output matrix is correct, otherwise it will print false."""

class Solution:
    def generateMatrix(self, rowSum, colSum):
        # code here
        n = len(rowSum)
        m = len(colSum)
        
        res = [[0]*m for _ in range(n)]
        
        i = j = 0
        
        while i < n and j < m:
            res[i][j] = min(rowSum[i], colSum[j])
            
            rowSum[i] -= res[i][j]
            colSum[j] -= res[i][j]
            
            if rowSum[i] == 0:
                i += 1
            if colSum[j] == 0:
                j += 1
        return res