class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')  # split by '/'

        for part in parts:
            if part == '' or part == '.':
                # Ignore empty parts and current directory
                continue
            elif part == '..':
                # Go up one level if possible
                if stack:
                    stack.pop()
            else:
                # valid directory name
                stack.append(part)

        # Join stack with '/' and add leading '/'
        return '/' + '/'.join(stack)
