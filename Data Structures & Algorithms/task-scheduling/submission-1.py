from heapq import heapify, heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        R:

        given:
            tasks: List[str]
            n: int

        identical tasks, must be separated by n CPU cycles

        The completion of 1 task = 1 CPU cycle

        return minimum number of CPU cycle required to complete all tasks

        E:

        1 <= tasks.length <= 10000
        0 <= n <= 100

        if all tasks are unique or n == 0, we can return len(tasks)

        there are 26 possible tasks

    
        A:
        Input: tasks = ["A","A","A","B","C"], n = 3

        Output: 9

        
        ["A","A","A","B","B","C"]


        [A, 3], [B, 2], [C, 1]


        B ->A -> Idle -> B -> C -> A -> Idle -> Idle -> Idle -> A

        order doesn't matter here just that we minimise spacing 


        A-Z hash map:
        A: 3, B: 2, C: 1 

        A -> B -> C -> Idle -> B ->   


        ["A","A","D","A","A","B","B","C", "B", "D"]
        A: 4, B: 3, C: 1, D: 2 

        -> A: 4, B: 3, D: 2, C: 1

        A -> B -> D -> C -> A -> B -> D -> Idle -> A -> B -> Idle -> Idle -> A

        So on each iteration until exhaustion, I schedule highest frequency task, decrement, then schedule next highest frequency task, if next highest frequency task can't be scheduled, I add an idle cycle


        i.e.

        Each round, pick up to n + 1 distinct tasks with the highest current counts.
Decrement each one you picked.
If fewer than n + 1 tasks were available, fill the rest of the round with idles, unless everything is exhausted (no trailing idles on the last round).
Re-sort after every round. Don't just loop through the original order, since counts change and the ranking can shift.



        C:


        T:

        """

        heap = [-c for c in Counter(tasks).values()]
        heapify(heap)

        time = 0
        while heap:
            on_cooldown, executed_this_cycle = [], 0
            for _ in range(n + 1):
                if not heap:
                    break
                remaining = heappop(heap) + 1  # counts are negative, so +1 decrements
                executed_this_cycle += 1
                if remaining < 0:
                    on_cooldown.append(remaining)

            for remaining in on_cooldown:
                heappush(heap, remaining)

            time += n + 1 if heap else executed_this_cycle

        return time

                
                
                

        
        
        