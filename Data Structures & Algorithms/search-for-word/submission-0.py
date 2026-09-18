"""
CAT

board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]

word[i], i = 0, C

bfs(i, position, curr)

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                board[r][c] != word[i] or (r, c) in visited):
                return False

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True
            visited.remove((r, c))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        return False