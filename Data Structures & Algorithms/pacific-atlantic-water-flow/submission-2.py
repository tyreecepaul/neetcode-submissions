"""
Problem:
- heights is island, heights[r][c] is height above sea level
- top and left: Pacific Ocean
- botton and right: Atlantic Ocean
- directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- from a cell to a neighbouring cell with equal or lower
goal: find all cells where water can flow from that cell to both the pacific and atlantic oceans
- can return list in any order

bfs vs dfs: 
- bfs will search in all available directions until ending
- dfs will search each direction at a time 
we don't need to return the path, just making sure that we can return whether that coordinate can access both pacific and atlantic
adjanceny matrix: O(V^2)

pacific: r < 0, c < 0
atlantic: r > 0, c > 0

(INVALID) alternative approach:
- start at bottom left and top right, add them to a row in which we can perform a bfs solution
- check each time in each direction if it works
- although will not work because there are values in the middle that can make it but cannot go the entire way

instead, get all nodes that can reach the pacific ocean, all nodes that can reach the atlantic ocean, then combine them into a joint set and return that set
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])  

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res 
        