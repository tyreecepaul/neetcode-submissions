"""
brute force:
- nested for loop approach
- for n_1 in nums, for n_2 in nums, for n_3 in nums
- check each combination of n1, n2, n3 and add to output array
T: O(N^3), O(1)

two pointers:
- for n1 in nums, n2 and n3 pointers
- check combination of each
O(N^2), O(1)

sorted two pointer:
- sort nums
- for n in nums, set l be i+1 and r be len(nums) - 1

while l < r:
    threeSum = n1 + nums[l] + nums[r]
    if threeSum > 0:
        r += 1
    elif threeSum < 0:
        l += 1
    elif threeSum == 0:
        res.append([n1, nums[l], nums[r]])
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
            

            
        