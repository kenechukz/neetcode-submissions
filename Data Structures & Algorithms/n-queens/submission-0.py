class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """

        R:

        given:
            n: int
        
        return all solutions to the n-queens puzzle (in any order)

        n -> n x n chess board

        E:
        1 <= n <= 8

        A:
        we need 1 queen per row and 1 queen per column and 1 per diagonal axis

            [Q.]
            [.Q] -> 0 solutions

            end state of different turns 

            [Q...]
            [....]          
            [.Q..]
            [....]

            [Q...]
            [..Q.]
            [....]
            [.Q..]

            [....]
            [Q...]          
            [....]
            [....]

            [..Q.]
            [Q...]   --> solution          
            [...Q]
            [.Q..]
        
        """


        from collections import defaultdict


        res = []
        rowTaken = defaultdict(bool)


        board = [["." for _ in range(n)] for _ in range(n)]

        def upLeftTaken(curRow, curCol):
            if curRow < 0 or curCol < 0:
                return False
            if board[curRow][curCol] == "Q":
                return True
            return upLeftTaken(curRow - 1, curCol - 1)

        def downLeftTaken(curRow, curCol):
            if curRow >= n or curCol < 0:
                return False
            if board[curRow][curCol] == "Q":
                return True
            return downLeftTaken(curRow + 1, curCol - 1)

        def diagonalTaken(curRow, curCol):
            return upLeftTaken(curRow - 1, curCol - 1) or downLeftTaken(curRow + 1, curCol - 1)


        def recurse(curCol): 

            if curCol >= n:
                res.append([row[:] for row in board])
                return

            for row in range(n):

                if rowTaken[row]:
                    continue

                if curCol > 0 and diagonalTaken(row, curCol):
                    continue
                    
                board[row][curCol] = "Q"
                rowTaken[row] = True
                recurse(curCol+1)
                board[row][curCol] = "."
                rowTaken[row] = False
                

            return

                
            




        recurse(0)

        cleanedRes = []
        if res:
            for sol in res:
                newArr = []
                for row in sol:
                    newArr.append("".join(row))
                
                cleanedRes.append(newArr)      

        return cleanedRes


        
        