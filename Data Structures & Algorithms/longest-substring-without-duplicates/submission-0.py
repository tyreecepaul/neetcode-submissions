class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in mp:
                mp.remove(s[l])
                l += 1
            mp.add(s[r])
            res = max(res, r - l + 1)

        return res
