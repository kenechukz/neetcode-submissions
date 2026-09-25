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

        from heapq import heapify, heappush, heappop

        task_freq = [0] * 26


        uniq_tasks = set()
        max_task = []

        for task in tasks:
            if task_freq[ord(task) - ord("A")] == 0:
               uniq_tasks.add(task)
            task_freq[ord(task) - ord("A")] += 1


        for task in uniq_tasks:
            heappush(max_task, (-task_freq[ord(task) - ord("A")], task))


        result = 0
        
        while max_task:
            len_this_round = 0
            temp = []
            for i in range(n+1):
                if not max_task:
                    break

                popped = heappop(max_task)
                len_this_round+=1
                task_freq[ord(popped[1]) - ord("A")] -=1
                cur_freq = task_freq[ord(popped[1]) - ord("A")]

                if cur_freq > 0:
                    temp.append((-cur_freq, popped[1]))

            result += len_this_round

            for task in temp:
                heappush(max_task, (task[0], task[1]))

            if max_task:
                result += (n+1) - len_this_round

        return result 

                
                
                

        
        
        