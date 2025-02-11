"""The n-queens puzzle is the problem of placing n queens on a (n × n) chessboard such that no two queens can attack each other. Note that two queens attack each other if they are placed on the same row, the same column, or the same diagonal.

Given an integer n, find all distinct solutions to the n-queens puzzle.
You can return your answer in any order but each solution should represent a distinct board configuration of the queen placements, where the solutions are represented as permutations of [1, 2, 3, ..., n]. In this representation, the number in the ith position denotes the row in which the queen is placed in the ith column.
For eg. below figure represents a chessboard [3 1 4 2].
"""
class Solutions:
    def nQueenUtil(self, j, n, board, rows, diag1, diag2, res):

        if j > n:
            # A solution is found
            res.append(board[:])
            return

        for i in range(1, n + 1):
            if not rows[i] and not diag1[i + j] and not diag2[i - j + n]:

                # Place queen
                rows[i] = diag1[i + j] = diag2[i - j + n] = True
                board.append(i)

                # Recurse to the next column
                self.nQueenUtil(j + 1, n, board, rows, diag1, diag2, res)

                # Remove queen (backtrack)
                board.pop()
                rows[i] = diag1[i + j] = diag2[i - j + n] = False

    def nQueen(self, n):
        res = []
        board = []

        # Rows occupied
        rows = [False] * (n + 1)

        # Major diagonals (row + j) and Minor diagonals (row - col + n)
        diag1 = [False] * (2 * n + 1)
        diag2 = [False] * (2 * n + 1)

        # Start solving from the first column
        self.nQueenUtil(1, n, board, rows, diag1, diag2, res)
        return res