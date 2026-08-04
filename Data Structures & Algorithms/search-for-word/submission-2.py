class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        R:

        given: 2-D grid "board", and word: str

        return whether word present

        E:

        constraints:
        can't reuse cell for same word
        only lower
        1 <= word.length <= 10

        base case:
        if curWord == word:
            return True

        if depth == len(word):
            return
        acc nvm

        

        A:

                        A
                    S       B
                A     A    A   C
                              A  T


        check next options:
        if col + 1 (right), col - 1 (left), row + 1 (down), row -1 (up)

        only add to cur word if char equal to cur idx of word


        """

        row_bound = len(board)
        col_bound = len(board[0])

        visited_paths = set()

        def dfs(row, col, idx):

            
            if idx == len(word):
                return True

            if ( not (0<= row < row_bound) or not (0<= col < col_bound) 
                or word[idx] != board[row][col] 
                or (row, col) in visited_paths):

                return False

            visited_paths.add((row, col))
            res = (dfs(row+1, col, idx+1) or dfs(row-1, col, idx+1) or 
                    dfs(row, col+1, idx+1) or dfs(row, col-1, idx+1) 
                )
            visited_paths.remove((row, col))

            return res


        for r in range(row_bound):
            for c in range(col_bound):
                if dfs(r, c, 0):
                    return True

        return False


    

            


 
        