"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


0   5   15

10  20  40
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        start,end = sorted([time.start for time in intervals]),sorted([time.end for time in intervals])
        e = minDays = days = 0
        for s in start:
            while e < len(end) and s >= end[e]:
                days-=1
                e+=1

            days+=1
            minDays = max(minDays, days)

        return minDays