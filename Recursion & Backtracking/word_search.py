"""You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once."""
class Solution:
    def findMatch(self, mat, word, x, y, wIdx):
        wLen = len(word)
        n = len(mat)
        m = len(mat[0])
        # Pattern matched
        if wIdx == wLen:
            return True

        # Out of Boundary
        if x < 0 or y < 0 or x >= n or y >= m:
            return False

        # If grid matches with a letter while
        # recursion
        if mat[x][y] == word[wIdx]:

            # Marking this cell as visited
            temp = mat[x][y]
            mat[x][y] = '#'

            # finding subpattern in 4 directions
            res = (self.findMatch(mat, word, x - 1, y, wIdx + 1) or
                self.findMatch(mat, word, x + 1, y, wIdx + 1) or
                self.findMatch(mat, word, x, y - 1, wIdx + 1) or
                self.findMatch(mat, word, x, y + 1, wIdx + 1))

            # marking this cell as unvisited again
            mat[x][y] = temp
            return res
        # Not matching then return false
        return False

    def isWordExist(self, mat, word):
        wLen = len(word)
        n = len(mat)
        m = len(mat[0])
        # if total characters in matrix is
        # less than word length
        if wLen > n * m:
            return False

        # Traverse in the grid
        for i in range(n):
            for j in range(m):

                # If first letter matches, then recur and check
                if mat[i][j] == word[0]:
                    if self.findMatch(mat, word, i, j, 0):
                        return True
        return False