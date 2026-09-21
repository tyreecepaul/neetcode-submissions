"""
nums = [1,2,3,4,5,6,7,8], k = 4
output: [5,6,7,8,1,2,3,4]

l = 0, r = k + 1
nums = [5,6,7,8,1,2,3,4]

l = 0, r = k + 1
nums = [1,2,3,4,5,6,7,8], k = 2
output: nums = [8,7,1,2,3,4,5,6]

brute force: 
- for _ in range(k):
- pop the value and then prepend it and keep doing this

"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            temp = nums.pop()
            nums.insert(0, temp)
        
        