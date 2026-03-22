class Solution:
    def subsets(self, nums):
        res = []
        
        def backtrack(start, path):
            res.append(path[:])  # add current subset
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)  # include next numbers
                path.pop()  # backtrack
        
        backtrack(0, [])
        return res
