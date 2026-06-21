class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialise array with all values set to 1
        res = [1] * (len(nums))
        
        # l to r
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        
        # r to l
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res