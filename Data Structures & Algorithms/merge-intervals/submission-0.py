class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        res = []
        if n == 1:
            return intervals
        intervals.sort()
        prev = intervals[0]
        for i in range(1,n):
            cur = intervals[i]
            if cur[0] <= prev[1]:
                cur = [prev[0], max(prev[1],cur[1])]
            else:
                res.append(prev)
            prev = cur
        res.append(prev)

        return res