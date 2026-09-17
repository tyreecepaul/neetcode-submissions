"""
nums = [1, 2, 1]
must not contain duplicate subsets -> set()

subsetsWithDup(nums):
    res = []
    subset = []
    
    def dfs(i):
        if i >= len(nums) and subset not in res:
            res.append(subset[:])
            return
        
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res
"""



class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return res