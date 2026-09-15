"""
sliding window: (using set)
- start l and r at 0
- for n in nums, 
    - move r++
    - check if the value is in the set
        - if so return true
    - add value to set
    - if abs(r - l) > k:
        - remove nums[l] from set
        - move l++
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        seen = set()
        for n in nums:

            # check if duplicate
            r += 1
            if n in seen:
                return True
            seen.add(n)

            # move window
            if abs(r - l) > k:
                seen.remove(nums[l])
                l += 1
    
        return False