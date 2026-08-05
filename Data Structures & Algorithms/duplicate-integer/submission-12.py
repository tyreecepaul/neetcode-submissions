"""
nums = [1, 2, 3, 3]
set() = len() == 3
nums == 4
len(set(nums)) != len(nums)  

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)