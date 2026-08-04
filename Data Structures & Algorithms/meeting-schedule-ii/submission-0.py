"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        """
        R:
        0 --------------------- 40

           5--10
                 15--20
        """
        start = sorted([intr.start for intr in intervals])
        end = sorted([intr.end for intr in intervals])
        s,e = 0,0
        res,count = 0,0

        while s < len(intervals):

            if start[s] < end[e]:
                count+= 1
                s+=1
            else:
                count-=1
                e+=1

            res = max(res, count)

        return res


        