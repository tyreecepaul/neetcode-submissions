"""
stones:
- choose two heaviest stone
    - if equal they are destroyed
    - if diff, take largestStone - smallerStone and that becomes new height

- we need to take the greatest 2 stones, in priority
- either destroy the stone or create a new stone
- repeat until either 1 stone left or 0 stones left (return weight)

approach: heap
init heap
add elements to heap
grab top 2 from heap
perform operation in while loop (while len of heap > 1)
if len of heap == 0 then return 0, else return heap[1]
maxHeap hence using -ve ints
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0] 
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            largerStone = -heapq.heappop(max_heap)
            smallerStone = -heapq.heappop(max_heap)
            if largerStone != smallerStone: # if == then do nothing
                print(f"{largerStone} - {smallerStone}")
                newStone = largerStone - smallerStone
                heapq.heappush(max_heap, -newStone)
            print(max_heap)
        return -max_heap[0] if len(max_heap) != 0 else 0
