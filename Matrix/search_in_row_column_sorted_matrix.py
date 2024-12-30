"""Given a 2D integer matrix mat[][] of size n x m, where every row and column is sorted in increasing order and a number x, the task is to find whether element x is present in the matrix."""

class Solution:
    def matSearch(self, mat, x):
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns
        
        # Start from the top-right corner of the matrix
        i = 0
        j = m - 1
        
        # Traverse the matrix within its bounds
        while i < n and j >= 0:
            # If x is greater than mat[i][j], move down to the next row
            if x > mat[i][j]:
                i += 1
            # If x is smaller than mat[i][j], move left to the previous column
            elif x < mat[i][j]:
                j -= 1
            # If x matches mat[i][j], return True (found)
            else:
                return True
        
        # If we exit the loop, x was not found
        return False
