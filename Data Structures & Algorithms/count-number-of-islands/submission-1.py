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
            r,c = coord[0], coord[1]

            if grid[r][c] == "0":
                return
            grid[r][c] = "0"

            neighbours = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for f,l in neighbours:
                if (0 <= f < m and 0 <= l < n) and grid[f][l] == "1":
                    dfs((f, l))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count+=1
                    dfs((i,j))

        return count

        # for loop: O(m * n)
        # dfs for loop: O(1)
        # dfs recursive call(k), where k = no. of 1s  
        # total time: O(m*n + k) 
        # total space(k)                 
                
                
        