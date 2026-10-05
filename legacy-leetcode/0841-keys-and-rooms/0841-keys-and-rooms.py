class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Every time we check a room we mark it as visited
        # We then iterate through its keys which will give access to room 'key' (e.g. room 1)
        # We call this recursively on unvisted room numbers (represented by key)
        # Time complexity: O(n + k) ~ n rooms and k keys across all rooms
        # Space complexity: O(n) ~ call stack in worse case
        self.visited = [False] * len(rooms)

        def dfs(rooms, idx):
            self.visited[idx] = True
            for key in rooms[idx]:
                if not self.visited[key]:
                    dfs(rooms, key)

        dfs(rooms, 0)
        return all(self.visited)
