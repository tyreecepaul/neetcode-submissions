"""
nums = [2, 5, 6, 9], target = 9
return [2, 2, 5], [9]

nums = [3, 4, 5], target = 16
5, 5, 3, 3 

- start from repeating the same value and keep summming up until that value > target
- if value > target, remove the value from the top and replace it with another value
- keep doing this
- exhaust each number and keep doing this until total > target and then pop the value from stack
"""

# T: O(2^(t/m))
# S: O(t/m)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res

    

                    