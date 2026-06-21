class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            res = numbers[i] + numbers[j]
            if res == target:
                return [i + 1, j + 1]
            elif res > target:
                j -= 1
            elif res < target:
                i += 1