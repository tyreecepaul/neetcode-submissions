class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        T: O(N), S: O(1)

        """
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr