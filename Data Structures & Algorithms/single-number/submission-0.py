class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = set()
        res = []
        for n in nums:
            if n in arr:
                res.remove(n)
            else:
                res.append(n)
                arr.add(n)
        return res[0]
            