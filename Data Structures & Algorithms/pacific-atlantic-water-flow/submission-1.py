from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        pac, atl = set(), set()  # cells reachable by Pacific / Atlantic

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):  # water can flow uphill or same height in reverse
                    dfs(nr, nc, visited)

        # DFS from Pacific borders
        for c in range(COLS):
            dfs(0, c, pac)        # top most row
            dfs(ROWS-1, c, atl)   # bottom most row
        for r in range(ROWS):
            dfs(r, 0, pac)        # left most column
            dfs(r, COLS-1, atl)   # right most column

        # Intersection of reachable cells
        res = [[r, c] for (r, c) in pac & atl]
        return res
