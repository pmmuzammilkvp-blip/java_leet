class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # no carry, done
            digits[i] = 0  # set to 0 and carry over
        
        # If all digits were 9, we have a carry for a new digit
        return [1] + [0] * n
