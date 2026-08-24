from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        R:
        given n (no. nodes) and list of undirected edges
        check if edges make a tree

        condition for tree
        DAG 

        E:
        no duplicate edges ([0, 1], [1, 0] are the same)
        1 <= n <= 2000

        Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

        there are no cycles

        we mainly check for cycles

        create adj list for each

        0: 1, 2, 3
        1: 4
        2:
        3:

        0 - 1 - 4
        | \
        2  3

        so if while doing the checks something gets visited again return false?

        0: 1
        1: 0,2,3,4
        2: 3
        3: 2
        4: 1

        We check 2 conditions for a tree:
            - Connected
            - Acyclic

        Connected we check whether length of seen set is equal to n (all nodes have been reached) 
        Check there are no cycles using dfs

        """
        
        def valid(node, parent):
            seen.add(node)
            for val in adj_list[node]:
                if val == parent:
                    continue
                if val in seen:
                    return False
                if not valid(val, node):
                    return False

            return True
            

        seen = set()

        # O(n x m)
        # 0: 1
        # 1: 0,2,3,4
        # 2: 3
        # 3: 2
        # 4: 1
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)


        # Check there are no cycles AND all components of tree are connected 
        return valid(0, -1) and len(seen) == n
        

        

        

        





        





        