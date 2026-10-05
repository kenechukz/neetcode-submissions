class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
              3      2      5
            a ---- b ---- c --- d  
                 1/3    1/2    1/5  
        """

        # We make a bi-directional weighted graph from the equations object, 
        # where weights are inverted going counter-clockwise
        # We then iterate through queries and first validate the symbols
        # Next we run a traversal (dfs) on the query, giving it a fresh visited set
        # We have the same v value from recursive call to recursive call and return 
        # when u (cur vertex) = v (targegt vertex)
        # e.g. query [a,d]
        # Time complexity O(Q . (V + E))
        # Space complexity (worst case): O(V^2 + Q) ~ Q - result length (query length), V - For both visited and recursive stack

        def dfs(u, v, curAns, visited):
            if u == v:
                return curAns
            visited.add(u)
                
            for nb, w in graph[u].items():
                if nb in visited:
                    continue
                ans = dfs(nb, v, curAns * w, visited)

                if ans != -1:
                    return ans
            return -1
                
        symbols = {symbol for eq in equations for symbol in eq}
        graph = {symbol:{} for symbol in symbols}
        res = []

        for [a,b],val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1/val

        for s,t in queries:
            curAns = 1     
            if not s in graph or not t in graph:
                res.append(-1)
                continue  
            else:
                res.append(dfs(s, t, curAns, set()))

            

        return res
        

        






        

        
        