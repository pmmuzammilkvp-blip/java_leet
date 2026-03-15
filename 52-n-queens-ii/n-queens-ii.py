class Solution:
    def totalNQueens(self, n):
        count = 0

        cols = set()
        diag = set()      # r - c
        antiDiag = set()  # r + c

        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return

            for col in range(n):
                if col in cols or (row - col) in diag or (row + col) in antiDiag:
                    continue

                # Place queen
                cols.add(col)
                diag.add(row - col)
                antiDiag.add(row + col)

                backtrack(row + 1)

                # Remove queen (backtrack)
                cols.remove(col)
                diag.remove(row - col)
                antiDiag.remove(row + col)

        backtrack(0)
        return count
