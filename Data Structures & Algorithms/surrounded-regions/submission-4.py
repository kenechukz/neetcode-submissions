from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        queue = deque()

        # Add all border 'O's to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O':
                    queue.append((r, c))

        # BFS: mark all border-connected 'O's as 'E' (escaped)
        while queue:
            r, c = queue.popleft()
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = 'E'
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((r + dr, c + dc))

        # Flip remaining 'O' → 'X' and 'E' → 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'
