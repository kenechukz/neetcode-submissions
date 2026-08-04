from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_cnt = 0
        minutes = 0
        queue = deque()

        def bfs(r, c):
            nonlocal fresh_cnt
            # boundary + non-fresh check
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                return

            # rot fresh orange
            grid[r][c] = 2
            fresh_cnt -= 1
            queue.append((r, c))  # add to queue so it can spread rot next round

        # collect initial rotten oranges & fresh count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        if fresh_cnt == 0:
            return 0

        if not queue:
            return -1

        while queue:
            n = len(queue)
            new_rotted = False
            for _ in range(n):
                r, c = queue.popleft()
                prev_cnt = fresh_cnt

                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

                if fresh_cnt < prev_cnt:
                    new_rotted = True

            if new_rotted:
                minutes += 1

            if fresh_cnt == 0:
                return minutes

        return -1
