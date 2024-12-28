"""Given a row-wise sorted 2D matrix mat[][] of size n x m and an integer x, find whether element x is present in the matrix.
Note: In a row-wise sorted matrix, each row is sorted in itself, i.e. for any i, j within bounds, mat[i][j] <= mat[i][j+1]."""

def search(arr, x):
    lo, hi = 0, len(arr) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        
        #if x==mid, return True
        if x == arr[mid]:
            return True
            
        #if x < arr[mid] search in left half
        if x < arr[mid]:
            hi = mid - 1
        #if x > arr[mid] search in right half
        else:
            lo = mid + 1
            
    return False
        
class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        n, m = len(mat), len(mat[0])
        
        #n iterates over all the rows to find x
        for i in range(n):
            #perform binary search on the ith row
            if search(mat[i], x):
                return True
                
        #if x was not found return false
        return False