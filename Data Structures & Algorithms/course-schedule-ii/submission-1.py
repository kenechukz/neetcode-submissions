from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        """
        R:
        return valid ordering of courses to finish all courses knowing: [a,b] -> b < a (b comes befor a)


        E:
        if prereq courses doesn't have all numCourses courses we add remaining:
            Input: numCourses = 3, prerequisites = [[1,0]]
            Output: [0,1,2]

        A:

        Kahn's Topological Sort

        Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]


        1 -> 0    2 -> 1  2 -> 0

        2 < 1 < 0 
        0 < 2 ? Contradiction

        initialise array of size numCourses

        for each index we check  indegree (has indegree if it depends on something) of that elem

        arr [1, 1, 1]

        we also store an adjancency list:

        we add elem which has indegree 0 to queue

        if we have are visiting a dependency, we will decrease it's degree by 1

        each time element is found with in degree zero, we add it to final result

        on each iteration we are looking for elem with in degree 0


        1-> 2, 4     4 -> 3  2 -> 4

        1 < 2 < 4 < 3
        

        """


        in_deg = [0] * numCourses
        adj_list = defaultdict(list)
        order = []
        for a,b in prerequisites:
            adj_list[b].append(a)
            in_deg[a] += 1

        queue = deque([c for c in range(len(in_deg)) if in_deg[c] == 0])

        while queue:
            c = queue.popleft()
            order.append(c)

            for dep in adj_list[c]:
                in_deg[dep] -= 1

                if in_deg[dep] == 0:
                    queue.append(dep)

        return order if len(order) == numCourses else []




