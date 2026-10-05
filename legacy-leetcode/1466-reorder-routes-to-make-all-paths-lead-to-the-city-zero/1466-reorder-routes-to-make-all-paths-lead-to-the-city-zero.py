class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        # We start at vertex 0 and ensure it's neighbour are directed towards it
        # Then we recursively check 0's neighbours; we ensure their unvisited neighbours are directed towards 0
        # i.e. towards them

        # Time Complexity: O(n)
        # Space Complexity: O(n)

        edges = {(a, b) for a,b in connections}
        neighbours = {city:[] for city in range(n)}
        visited = set()
        count = 0
        for a,b in connections:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def dfs(city):
            nonlocal edges, neighbours, visited, count
            for neighbour in neighbours[city]:
                if not neighbour in visited:
                    if not (neighbour, city) in edges:
                        count+= 1
                    visited.add(neighbour)
                    dfs(neighbour)
            return count
        visited.add(0)
        return dfs(0)

        
                




        