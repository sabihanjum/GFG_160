"""Given a 2D square matrix mat[][] of size n x n, turn it by 180 degrees without using extra space.

Note: You must rotate the matrix in place and modify the input matrix directly."""

class Solution:
	def rotateMatrix(self, mat):
		# Code here
		n = len(mat)
		
		#swap element from start and end to rotate at 180 degree
		for i in range(n // 2):
			for j in range(n):
				mat[i][j], mat[n - i - 1][n - j - 1] = mat[n - i - 1][n - j - 1], mat[i][j]
				
        #handle the middle row if the matrix has odd dimension        
		if n % 2 != 0:
			mid = n // 2
			for j in range(n // 2):
				mat[mid][j], mat[mid][n - j - 1] = mat[mid][n - j - 1], mat[mid][j]
        