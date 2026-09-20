"""
nums = [0,0,1,2,0,5]
output: [1,2,5,0,0,0]

nums = [0, 1, 0]
output = [1, 0, 0]

two pointers:
- left pointer keeps track of zeros
- right pointer keeps on iterating until the end
- left pointer stays on the zero and when right encounters an element that is not zero then swap
- O(N), O(1)
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


