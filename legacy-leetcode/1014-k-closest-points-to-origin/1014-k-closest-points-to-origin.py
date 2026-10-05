from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # time:O(n log n), space: O(n)
        points.sort(key=lambda point: sqrt( (point[0])**2 + (point[1])**2 )  )
        res = []
        for i in range(k):
            res.append(points[i])

        return res
