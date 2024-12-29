"""Given a square matrix mat[][] of size n x n. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space. """

class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        n = len(mat)
        
        #reverse each row
        for row in mat:
            row.reverse()
            
        #performing transpose
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]