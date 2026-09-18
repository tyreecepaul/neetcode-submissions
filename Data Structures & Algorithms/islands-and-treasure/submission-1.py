"""
traverse the treasure:
three possible values: 
- -1 (water cannot be traversed)
- 0 (treasure chest)
- INF (land sell that can be traversed)

dist = 0 

queue = deque()
- traverse the grid and get the values of the treasure chests
- starting from the treasure chests, we expand out in all directions
- when we expand out we add the land cells to the queue
- replace them with dist (incremented by 1 each iteration)
- keep track of visited in visited set
- if q is empty we stop

consideration: is it possible for a value to be unoptainable (assuming for the input it would be no but keep this in mind)
"""


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        INF = 2147483647
        q = deque()
        dist = 0

        # init the queue by putting in all the chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        # bfs from the chests
        while q:
            n = len(q)
            for i in range(n):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == INF and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr, nc))
            dist += 1   
        
                        

                




