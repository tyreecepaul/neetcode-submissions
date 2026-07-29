class NumArray:
    
    def __init__(self, nums: List[int]):
        # init nums array   
        self.nums = nums


    def sumRange(self, left: int, right: int) -> int:
    # take the left and right given and return the sum of the points in nums
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)