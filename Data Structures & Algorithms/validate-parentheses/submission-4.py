class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charMatch = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in charMatch:
                if stack and stack[-1] == charMatch[char]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(char)

        return True if not stack else False
