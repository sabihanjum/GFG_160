"""Given a strictly sorted 2D matrix mat[][] of size n x m and a number x. Find whether the number x is present in the matrix or not.
Note: In a strictly sorted matrix, each row is sorted in strictly increasing order, and the first element of the ith row (i!=0) is greater than the last element of the (i-1)th row."""

class Solution:
    # Function to search a given number in a row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns
        
        # Initialize the binary search range over the entire matrix
        lo, hi = 0, m * n - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            # Calculate the row and column for the mid index
            row = mid // m
            col = mid % m
            
            # If the element at mid is equal to x, return True
            if mat[row][col] == x:
                return True
            # If x is greater, search in the right half
            elif mat[row][col] < x:
                lo = mid + 1
            # If x is smaller, search in the left half
            else:
                hi = mid - 1
        
        # If the loop ends without finding x, return False
        return False
