class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """

        R:

        given 
            grid: List[List[str]]

        return number of islands

        island - formed by connecting '1's horizontally and vertically

        edges are water and 0s

        E:
        are rows consistent with columns?
        Like does each row have same number of columns

        What are the constraints?

        1 <= grid.length, grid[i].length <= 100

        A:

        Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

        iterate through grid
        if I find a 1 I increment land_count by 1
        When I've visited a 1 in make it a 0
        I call dfs on the one 
        Then I look for its neighbours (vertically and horizontally)

        base case:

        # Checking if we are no longer on land
        if min(i,j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
            return 



        """



        ROWS, COLS = len(grid), len(grid[0])
        land_count = 0
        neighbours = [(0,-1), (-1, 0), (0,1), (1,0)]


        def dfs(i, j):

            if min(i,j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            for r,c in neighbours:
                nr, nc = i + r, j + c

                dfs(nr, nc)

            return






        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    land_count += 1
                    dfs(i,j)

        return land_count
        