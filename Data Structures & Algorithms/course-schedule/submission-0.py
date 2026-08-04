from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        R:
        Given 
        preq: arr[int]
        numCourses: int

        return true if all courses can be complete

        preq[i] = [a, b] = course b taken before a

        E:
        1 <= numCourses <= 10000

        if num courses == 0 -> false

        A:

        0 -> 1
          <-

        0: 1
        1: 0

        there's a cycle

        We traverse input like an adjancency list, if we find a cycle it's not possible

        If we start traversal from each vertex time complexity would be (V (V + E) )

        1000(1000 + 1000)
        1000(2000) = 2000000



        """
        def possible(key, visited):
            if key in visited:
                return False

            visited.add(key)
            
            for val in adj_map[key]:
                if not possible(val, visited):
                    return False

            visited.remove(key)
            adj_map[key] = []
            return True 

        adj_map = defaultdict(list)

        for a,b in prerequisites:
            adj_map[a].append(b)

        keys = list(adj_map.keys())
        for key in keys:
            if not possible(key, set()):
                return False

        return True