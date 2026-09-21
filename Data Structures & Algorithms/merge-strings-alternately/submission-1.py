class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0
        word1Length, word2Length = len(word1), len(word2)
        for _ in range(min(word1Length, word2Length)):
            res += word1[i]
            res += word2[i]
            i += 1
        if word1Length < word2Length:
            res += word2[i:]
        elif word1Length > word2Length:
            res += word1[i:]
        return res
