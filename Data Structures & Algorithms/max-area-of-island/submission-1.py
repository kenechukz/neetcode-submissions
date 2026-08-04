class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        """
        given grid of 1s (island) and 0s (water) of type int

        cannot be connected diagonally

        area - number of cells within island

        return max area of an islan in grid else if no island then 0

        E:
        grid is at least size 1


        [1 1 1 0 1]
        [1 0 1 0 1]
        [0 1 1 0 1]
        
        count = l + d + r + u
        A:

        DFS from each 1, and inc count as new 1 discovered
        mark those 1s as 0 when done with them




        """


        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(0, -1), (1,0), (0, 1), (-1,0)]
        maxArea = 0
        curArea = 0


        def dfs(r,c, count):

            grid[r][c] = 0

            for dr, dc in dirs:
                
                nr, nc = r + dr, c + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                    continue

                # grid[nr][nc] = 0
                count = dfs(nr, nc, count + 1)

            return count





        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curArea = dfs(r,c,1) 

                if curArea > maxArea:
                    maxArea = curArea

        return maxArea
        