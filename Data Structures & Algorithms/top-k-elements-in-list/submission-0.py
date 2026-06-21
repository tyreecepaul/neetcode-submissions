class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for _ in range(k):
            highest_key = max(count.keys(), key= lambda x: count[x])
            res.append(highest_key)
            del count[highest_key]
        return res

            