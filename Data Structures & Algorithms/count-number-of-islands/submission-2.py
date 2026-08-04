from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        count = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                curr_r, curr_c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = curr_r + dr, curr_c + dc

                    if  min(nr,nc) < 0 or nr >= ROWS or nc >= COLS or (nr,nc) in visited or grid[nr][nc] == "0":
                        continue
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and not (r,c) in visited:
                    count+=1
                    bfs(r, c)

        return count