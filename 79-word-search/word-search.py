class Solution:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, k):
            # i, j = current cell
            # k = index in word
            if k == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # mark the cell as visited
            temp = board[i][j]
            board[i][j] = '#'
            
            # explore all 4 directions
            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))
            
            # restore the cell
            board[i][j] = temp
            return found
        
        # try starting from each cell
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
