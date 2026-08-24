from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        R:
        undirected unconnected graph
        labelled from 0 - n-1
        given:
            n
            edges
        return no. connected comp. 
        E:

        1 <= n <= 2000

        A:

        0: 1
        1: 2
        2: 1 
        3: 4
        """

        def dfs(node):

            seen.add(node)
            for val in adj_list[node]:
                if not val in seen:
                    dfs(val)

            return
        
        seen = set()
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        count = 0
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)

        return count




        