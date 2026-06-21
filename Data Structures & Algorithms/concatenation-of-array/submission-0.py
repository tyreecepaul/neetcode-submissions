class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = nums.copy()
        for n in array:
            nums.append(n)

        return nums