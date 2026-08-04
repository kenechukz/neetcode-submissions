class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(coord, area):
            r,c = coord[0], coord[1]
            grid[r][c] = 0
            dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in dirs:
                nr,nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == 1:
                    area += dfs((nr, nc), 1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea,dfs((r,c), 1))

        return maxArea

        