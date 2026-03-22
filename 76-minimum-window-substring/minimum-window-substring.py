from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)  # required characters
        required = len(dict_t)
        
        # current window counts
        window_counts = defaultdict(int)
        formed = 0  # number of characters that meet required frequency
        
        l, r = 0, 0
        min_len = float('inf')
        min_window = (0, 0)
        
        while r < len(s):
            char = s[r]
            window_counts[char] += 1
            
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try to shrink window from left
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)
                
                char = s[l]
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                l += 1
            
            r += 1
        
        return "" if min_len == float('inf') else s[min_window[0]:min_window[1]+1]
