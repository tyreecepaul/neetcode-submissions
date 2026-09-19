"""
jump game:

return whether starting from index 0, the end index can be reached only moving nums[i] times at maximum, meaning they can also move nums[i] - 1 times, as long as it is >= 0

e.g. nums = [1, 2, 0, 1, 0]
output true:
-> start at index 0
-> move to index 1 (since nums[i] == 1)
-> nums[i] == 2, so 1 and 2 are available
-> moving maximum index (2) gets us to index 3
-> index 3 gets us to index 4 (len(nums) - 1)
-> return True

-> alt: would have moved to index from index 1 to index 2 and be stuck at 0


# problem in reverse by redefining the goal

currIndex, goalIndex = 0, len(nums) - 1 
while currIndex < goalIndex:
    # get number from currIndex
    while n < 0:
        


        n -= 1

return False


"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
