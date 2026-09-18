class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        count = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    count += 1

        while queue and count > 0:
            # bfs
            n = len(queue)
            for i in range(n):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        count -= 1

            time += 1

        return time if count == 0 else -1
