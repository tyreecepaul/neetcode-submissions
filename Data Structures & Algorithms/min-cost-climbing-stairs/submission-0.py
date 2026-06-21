class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # starting from the 3rd last position in the list
        for i in range(len(cost) - 3, -1, -1): # iterate backwards finding the minimum value to choose
            cost[i] += min(cost[i + 1], cost[i + 2]) # add that each time
        return min(cost[0], cost[1]) # return both since can start from either 1st or 2nd