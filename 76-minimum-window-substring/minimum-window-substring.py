class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Build frequency array for t (only 52 letters: a-z and A-Z)
        # Map characters to indices: 0-25 for a-z, 26-51 for A-Z
        def char_index(c):
            if 'a' <= c <= 'z':
                return ord(c) - ord('a')
            else:
                return ord(c) - ord('A') + 26

        t_freq = [0] * 52
        for c in t:
            t_freq[char_index(c)] += 1

        # Number of unique characters in t
        required = sum(1 for count in t_freq if count > 0)
        formed = 0

        window_freq = [0] * 52

        left = 0
        best_left = 0
        best_len = float('inf')

        for right in range(len(s)):
            right_idx = char_index(s[right])
            window_freq[right_idx] += 1

            if t_freq[right_idx] > 0 and window_freq[right_idx] == t_freq[right_idx]:
                formed += 1

            while formed == required:
                current_len = right - left + 1
                if current_len < best_len:
                    best_len = current_len
                    best_left = left

                left_idx = char_index(s[left])
                window_freq[left_idx] -= 1

                if t_freq[left_idx] > 0 and window_freq[left_idx] < t_freq[left_idx]:
                    formed -= 1

                left += 1

        if best_len == float('inf'):
            return ""
        return s[best_left:best_left + best_len]