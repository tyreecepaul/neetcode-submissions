"""

minHeap = [] of size k

for i in range(len(points)):


"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            dist = abs(math.sqrt(x1**2 + y1**2))
            heapq.heappush(minHeap, (dist, points[i]))

        res = []
        for i in range(len(points)):
            _, temp = heapq.heappop(minHeap)
            res.append(temp)
            if len(res) == k:
                return res

        return [[]]
