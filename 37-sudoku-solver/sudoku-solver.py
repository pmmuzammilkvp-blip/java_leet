class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Uses backtracking with constraint propagation for optimization.
        """
        # Track rows, cols, and 3x3 boxes that have each digit
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]

        # Initialize the used sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box_idx = (i // 3) * 3 + (j // 3)
                    row_used[i].add(num)
                    col_used[j].add(num)
                    box_used[box_idx].add(num)

        def is_valid(r, c, num):
            box_idx = (r // 3) * 3 + (c // 3)
            return (num not in row_used[r] and 
                    num not in col_used[c] and 
                    num not in box_used[box_idx])

        def solve():
            # Find the empty cell with the fewest possible candidates (MRV heuristic)
            min_options = 10
            min_r, min_c = -1, -1
            min_candidates = None

            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        box_idx = (i // 3) * 3 + (j // 3)
                        candidates = []
                        for num in range(1, 10):
                            if (num not in row_used[i] and 
                                num not in col_used[j] and 
                                num not in box_used[box_idx]):
                                candidates.append(num)
                        if len(candidates) < min_options:
                            min_options = len(candidates)
                            min_r, min_c = i, j
                            min_candidates = candidates
                            if min_options <= 1:
                                break
                if min_options <= 1:
                    break

            # No more empty cells - solved
            if min_r == -1:
                return True

            # If no candidates, this path is invalid
            if not min_candidates:
                return False

            # Try each candidate
            for num in min_candidates:
                box_idx = (min_r // 3) * 3 + (min_c // 3)
                board[min_r][min_c] = str(num)
                row_used[min_r].add(num)
                col_used[min_c].add(num)
                box_used[box_idx].add(num)

                if solve():
                    return True

                # Backtrack
                board[min_r][min_c] = '.'
                row_used[min_r].remove(num)
                col_used[min_c].remove(num)
                box_used[box_idx].remove(num)

            return False

        solve()