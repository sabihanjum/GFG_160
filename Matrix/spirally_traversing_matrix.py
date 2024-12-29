"""You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form."""

class Solution:
    # Function to return a list of integers denoting spiral traversal of the matrix.
    def spirallyTraverse(self, mat):
        m, n = len(mat), len(mat[0])  # Dimensions of the matrix
        
        # List to store the elements in spiral order
        res = []
        
        # Initializing the boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        # Loop until all elements are visited
        while top <= bottom and left <= right:
            # Traverse the top row from left to right
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1  # Move the top boundary down
            
            # Traverse the right column from top to bottom
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1  # Move the right boundary left
            
            # Traverse the bottom row from right to left, if still within bounds
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1  # Move the bottom boundary up
            
            # Traverse the left column from bottom to top, if still within bounds
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1  # Move the left boundary right
        
        return res
