"""
brute force:
- nested for loop
- for string in s check the substring from string to len(s) (right hand side only)
- from left to right if the value contains all values in XYZ, then get the length and store the minimum
that is returning the minimum substring, if we do this then we can store l, r as boolean and then get the
values from left to right when we return
Time: O(N^2), T: O(1)

sliding window:
- initalise
res = float('inf') (infty large)
check l to r, if substring from l:r does not include the values in t then keep increasing right
if they include value in t, then get the length
if we run into another case where it includes the values of t, then increment left until it matches 
same as above
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(t) > len(s):
            return ""
        
        tCount = Counter(t)        
        sCount = {}
        
        res = (float("inf"), 0, 0)
        l = 0

        def valid():
            for c in tCount:
                if sCount.get(c, 0) < tCount[c]:
                    return False
            return True

        for r in range(len(s)):
            if s[r] in tCount:
                sCount[s[r]] = 1 + sCount.get(s[r], 0)
            
            while valid():
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                if s[l] in tCount: 
                    sCount[s[l]] -= 1

                l += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]