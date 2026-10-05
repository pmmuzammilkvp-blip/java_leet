class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Store index; -1 is the base/boundary
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()  # Remove last unmatched '(' or boundary
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)  # New boundary at this ')'

        return max_len