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

        unions = 0 
        parents = defaultdict(int)
        rank = defaultdict(int)

        def find(a):
            if a != parents[a]:
                parents[a] = find(parents[a])
            return parents[a]

        def union(a, b):
            p_a,p_b = find(a),find(b)
            if p_a == p_b:
                return False

            if rank[p_a] > rank[p_b]:
                parents[p_b] = p_a
                rank[p_a] += 1
            else:
                parents[p_a] = p_b 
                rank[p_b] += 1

            return True

        for i in range(n):
            parents[i] = i

        for u,v in edges:
            if union(u, v):
                unions+=1


        return n - unions

            

        




        