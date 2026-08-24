from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        R:
        UDCyclicG
        given edges
        nodes from 1-n

        return edge which can be removed an keep graph connected 

        E:
        3 <= n <= 1000

        A:

        we iterate over edges and union various sets
        if the nodes we are uniting have the same parent, then that edge is redundant


        """
        parents = defaultdict(int)
        ans = -1

        def find(a):
            if parents[a] != a:
                return find(parents[a])
            return parents[a]

        def union(a, b):
            p_a,p_b = find(a),find(b)
            if p_a == p_b:
                return False
            else:
                parents[p_b] = p_a 
                return True

        for i in range(len(edges)):
            parents[i] = i

        for u,v in edges:
            if not union(u,v):
                ans = [u,v]

        return ans
        