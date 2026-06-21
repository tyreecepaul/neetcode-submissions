class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in data:
                return [data[comp], index]
            data[num] = index
        return []