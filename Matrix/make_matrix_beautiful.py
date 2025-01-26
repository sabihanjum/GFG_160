"""A beautiful matrix is a matrix in which the sum of elements in each row and column is equal. Given a square matrix mat[][]. Find the minimum number of operation(s) that are required to make the matrix beautiful. In one operation you can increment the value of any one cell by 1."""

class Solution:
    def findMinOperation(self, mat):
        # code here
        n = len(mat)
        res = 0
        maxSum = 0
        
        #find maximum sum across all the row
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += mat[i][j]
            maxSum = max(sum, maxSum)
            
        #find maximum sum across all the column
        for j in range(n):
            sum = 0
            for i in range(n):
                sum += mat[i][j]
            maxSum = max(sum, maxSum)
            
        #sum of operation across alll the rows
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += mat[i][j]
            res += (maxSum - sum)
            
        return res