class Solution:
    def combine(self, n: int, k: int):
        res = []
        
        def backtrack(start, path):
            # If the combination is of length k, add it to results
            if len(path) == k:
                res.append(path[:])
                return
            
            # Try adding numbers from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # move to next number
                path.pop()  # backtrack
        
        backtrack(1, [])
        return res
