"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        """
        R:
        given: non sorted intervals

        if conflict -> return false
        return bool
        E:
        if len == 0:
            return true

        A:
        sort intervals first:
        intervals = [(0,30),(5,10),(15,20)]
                 if   prev[1]  > cur[0]:
                    return false

        """

        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda intr: intr.start )
        prev = intervals[0]
        for intr in intervals[1:]:
            cur = intr
            if cur.start < prev.end:
                return False
            prev = cur
        return True


