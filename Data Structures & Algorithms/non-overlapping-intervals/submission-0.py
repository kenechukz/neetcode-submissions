class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        """
        Overlapping when inside another intervals range



        1 ---- 2
               2 ---- 3
                      3 ---- 4  
        1 ----------- 3
               2 ---- 3

        1--------4
        2---3 3--4
        ensure cur_itv[0] >= prev_itv[1]

        1 ---- 4
          2---3 

        dp  

        1 ---- 2
               2 ---- 3
                      3 ---- 4  
        when we delete prev ptr stays same  

        1 ----------------- 100 cnt: 1

            11-----22  
        1---11         
          2---12 cnt: 2

        Need to return minimum!!
        """

        intervals.sort()
        cnt = 0
        prev = None

        for itv in intervals:

            cur = itv

            if prev and cur[0] < prev[1]:
                cnt+= 1
                prev = prev if prev[1] < cur[1] else cur

            else:
                prev = cur

        return cnt

        """
        What I did wrong originally:
        I assumed intervals array was sorted
        didn't take into account that I need minimum removals
        """
        