"""
e.g. s = "ababd"
output: "bab"

e.g. s = "abbc"
output: "bb"

two approaches:
- nested for loop -> go through every possible example, keep track of the longest and return it, tracked by a nested for loop O(N^3) 
- two pointer:
    - l, r = converge?, p1 and p2
l, r vs p1 and p2

e.g. "ababd"
i, j = 0, 0

"aba"
i, j = 0, 0 (i and j turn into l and r pointers)
-> check if palindrome (yes since both are a) set it to be a with length 1
keep incrementing until we get a j that is a palindrome?
-> j+= 1 
-> check for palindrome "ab" (false)

treat every value as the centre
- consider odd and even case
- odd case: starting from p1, p2 = i, p1 -= 1, p2 += 1 and check from there
- even case: starting from p1, p2 = i, i+1, p1 -= 1, p2 += 1 and check from there
    - could be i - 1 in case error comes up
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        count = 0

        for c in range(len(s)):
            # odd case
            odd_cnt = 0
            odd_i, odd_j = c, c
            while odd_i >= 0 and odd_j < len(s) and s[odd_i] == s[odd_j]:
                odd_cnt = odd_j - odd_i + 1
                odd_i -= 1
                odd_j += 1
        
            # even case
            even_cnt = 0
            even_i, even_j = c, c + 1
            while even_i >= 0 and even_j < len(s) and s[even_i] == s[even_j]:
                even_cnt = even_j - even_i + 1
                even_i -= 1
                even_j += 1

            max_cnt, i, j = 0, 0, 0
            if odd_cnt > even_cnt:
                max_cnt, i, j = odd_cnt, odd_i + 1, odd_j
            else:
                max_cnt, i, j = even_cnt, even_i + 1, even_j
            
            if max_cnt > count:
                count = max_cnt
                res = s[i:j]

        return res
