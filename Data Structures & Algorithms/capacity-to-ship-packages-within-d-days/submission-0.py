class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower, upper = max(weights), sum(weights)
        res = upper
        
        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while lower <= upper:
            cap = (lower + upper) // 2
            if canShip(cap):
                res = min(res, cap)
                upper = cap - 1
            else:
                lower = cap + 1
        return res
            