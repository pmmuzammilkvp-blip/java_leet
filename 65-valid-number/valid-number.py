class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # remove leading/trailing spaces
        if not s:
            return False
        
        seen_digit = seen_dot = seen_e = False
        
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
                
            elif c in ['+', '-']:
                # sign is valid only at the start or just after 'e'
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
                    
            elif c == '.':
                if seen_dot or seen_e:  # dot cannot appear after e or twice
                    return False
                seen_dot = True
                
            elif c in ['e', 'E']:
                if seen_e or not seen_digit:  # e must appear once and after a digit
                    return False
                seen_e = True
                seen_digit = False  # reset digit for exponent part
                
            else:
                return False  # any other character is invalid
        
        return seen_digit  # must have at least one digit at the end
