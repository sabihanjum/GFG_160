"""You are given a 2D matrix mat[][] of size n×m. The task is to modify the matrix such that if mat[i][j] is 0, all the elements in the i-th row and j-th column are set to 0 and do it in constant space complexity."""

class Solution:
    def setMatrixZeroes(self, mat):
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns

        c0 = 1  # Variable to track if the first column needs to be set to 0

        # Step 1: Traverse the matrix to mark rows and columns that need to be set to 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    # Mark the first cell of the current row
                    mat[i][0] = 0
                    # Mark the first cell of the current column
                    if j == 0:
                        c0 = 0  # First column needs to be set to 0
                    else:
                        mat[0][j] = 0  # Mark the first row for the current column

        # Step 2: Traverse the matrix from (1, 1) to (n-1, m-1) to update cells
        for i in range(1, n):
            for j in range(1, m):
                # If either the current row or column is marked, set cell to 0
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0

        # Step 3: Update the first row if necessary
        if mat[0][0] == 0:
            for j in range(m):
                mat[0][j] = 0

        # Step 4: Update the first column if necessary
        if c0 == 0:
            for i in range(n):
                mat[i][0] = 0

