class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, curr):
            # base case:
            if i >= len(s):
                res.append(curr[:])
                return

            # recursive case:
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if palindrome(substring):
                    curr.append(substring)
                    dfs(j + 1, curr)
                    curr.pop()

        def palindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0, [])
        return res