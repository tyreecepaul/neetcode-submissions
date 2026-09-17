class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])

                    dfs(curr)
                    curr.pop()
                    used[i] = False

        dfs([])
        return res