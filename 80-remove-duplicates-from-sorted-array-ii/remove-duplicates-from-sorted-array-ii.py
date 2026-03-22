class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 2:
            return len(nums)
        
        # Start writing from index 2
        i = 2
        for j in range(2, len(nums)):
            # If nums[j] is greater than the element two places before, it's allowed
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        
        return i
