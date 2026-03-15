class Solution:
    def solveNQueens(self, n):
        result = []
        board = ["." * n for _ in range(n)]

        cols = set()
        diag = set()      # r - c
        antiDiag = set()  # r + c

        def backtrack(row):
            if row == n:
                result.append(board[:])
                return

            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in antiDiag:
                    continue

                # Place queen
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                cols.add(col)
                diag.add(row - col)
                antiDiag.add(row + col)

                backtrack(row + 1)

                # Remove queen (backtrack)
                board[row] = board[row][:col] + '.' + board[row][col+1:]
                cols.remove(col)
                diag.remove(row - col)
                antiDiag.remove(row + col)

        backtrack(0)
        return result
