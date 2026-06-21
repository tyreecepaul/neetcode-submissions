class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                left = mp[num - 1] 
                right = mp[num + 1]

                total_len = left + right + 1 #num
                mp[num] = total_len

                # update boundaries
                mp[num - left] = total_len
                mp[num + right] = total_len

                res = max(res, total_len)
        
        return res
