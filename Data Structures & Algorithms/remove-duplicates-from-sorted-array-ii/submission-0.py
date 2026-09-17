"""
return the array with at most 2 duplicates of the same and same space with "_" filling in remaining duplicates O(1) space
- sorted in order
- must maintain same space
- output: length of modified array
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            cnt = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]:
                r += 1
                cnt += 1
            
            for i in range(min(2, cnt)):
                nums[l] = nums[r]
                l += 1
            r += 1
        
        return l