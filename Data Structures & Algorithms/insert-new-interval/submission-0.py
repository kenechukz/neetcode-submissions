class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        """
        Time: O(n)
        Space: O(n)
        """

        for i in range(len(intervals)):
            
            # If the new interval is less than current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Check if lwr bound of new interval is greater than upr bound of intervls[i]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # There's an overlap, merge (take min lwr bound and max upr bound)
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), 
                                max(intervals[i][1], newInterval[1])]


        res.append(newInterval)
        return res

        