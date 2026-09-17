class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        R
        Given 2D grid 

        given:
            matrix: List[List[int]]

        return # of longest increasing path in matrix

        E & C:
        can only move vertically and horizontally
        integer i >= 0

        1 <= matrix.length, matrix[i].length <= 100

        no. of rows & columns between 1 an 100

        100 x 100 = 10000 biggest number of elements

        O(m * n)

        

        A:

        dp[i][j] = longest increasing path from cell i,j

        Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]

        Output: 4

        [[1,1,1],
         [3,2,1],
         [4,3,1]]
        
        0. Initialise dp grid with all zeros (not visited yet)
        1. iterate through matrix
        2. (dfs) for each cell we check:
            for neighbour in neighbours:
                if neighbour visited:
                    if neighbour is greater than current
                        current = 1 + neighbour
                i.e.    dp[i][j] = 1 + dp[ni][nj]
                else:
                    we do dfs and pass back into this function
                    current = 1 + dfs(...)

        we keep max value as we go through grid


        Example 2:
        [[7,6,5],
         [2,7,4],
         [1,2,3]]


        Result:
         Had algorithm down to a tea (Essentially solved Q/would've passed interview)
         Small typos in the constraints particulary this: "f not (0 <= nr < num_rows and 0 <= nc <  num_cols) or matrix[nr][nc] <= matrix[r][c]:"

         Didn't realise that I shouldn't only pass (0,0) inf dfs entrypoint 
        
        """

        num_rows = len(matrix)
        num_cols = len(matrix[0])
        neighbours = [(-1, 0), (0, -1), (1,0), (0,1)]

        dp = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        maxVal = -1
        def dfs(r,c):

            if dp[r][c] > 0:
                return dp[r][c] 

            best = 1
            for x,y in neighbours:
                nr,nc = r+x,c+y
                if not (0 <= nr < num_rows and 0 <= nc <  num_cols) or matrix[nr][nc] <= matrix[r][c]:
                    continue
                
                best = max(best,1 + dfs(nr,nc))

            dp[r][c] = best

            return dp[r][c]


        

        return max(dfs(r,c) for r in range(num_rows) for c in range(num_cols))





        