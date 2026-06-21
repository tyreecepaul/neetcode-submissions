class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        kth_smallest = heapq.nsmallest(self.k, self.nums)[-1]
        return -kth_smallest