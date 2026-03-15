class Solution:
    def canJump(self, nums):
        farthest = 0
        n = len(nums)

        for i in range(n):
            if i > farthest:
                # Current position is unreachable
                return False

            # Update farthest reachable index
            farthest = max(farthest, i + nums[i])

            if farthest >= n - 1:
                return True

        return True
