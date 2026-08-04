class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        R:
        givenn grid (2D)

        return no. of islands

        E:

        assume water is surrounding grid

        if grid is 1x1: 1 if grid[0] == 1 else 0


        if not 0 <= neighbour cell < row/col bound:
            out of bounds neighbour 
        A:

        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]


        """


        count = 0
        m = len(grid)
        n = len(grid[0])
        def dfs(coord):
            nonlocal m, n
            r,c = coord[0], coord[1]

            if grid[r][c] == "0":
                return

            up = (r-1, c)
            down = (r+1, c)
            left = (r, c-1)
            right = (r, c+1)

            neighbours = [up, down, left, right]

            grid[r][c] = "0"
            for f,l in neighbours:

                if (0 <= f < m and 0 <= l < n) and grid[f][l] == "1":
                    dfs((f, l))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    dfs((i,j))

        return count
                    
                
                
        