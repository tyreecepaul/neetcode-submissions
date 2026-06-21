class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        # Loops until pointers meet
        while l < r:

            # Checking if valid char for palidrome (A, a, 0) 
            while l < r and not self.alphaNums(s[l]):
                l += 1
            while r > l and not self.alphaNums(s[r]):
                r -= 1
            
            # If not equal return false
            if s[l].lower() != s[r].lower():
                return False

            # Move pointers
            l, r = l + 1, r - 1

        # Return true
        return True

    def alphaNums(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')) 