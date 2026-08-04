class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        R:
        given m x n grid
        can move down or right

        return no. possible unique paths that can be taken from grid[0][0] to grid[m-1][n-1]

        E:
        1 <= m, n <= 100

        A:
        start from goal and move left and up/ reverse iterate

        if i == m or j == n, -> grid[i][j] = 1

        else grid[i][j] == grid[i-1][j] + grid[i][j+1]


        return grid[0][0]

        """



        grid = [[0 for _ in range(n)]  for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):

                if i == m-1 or j == n-1:
                    grid[i][j] = 1

                else:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]
        