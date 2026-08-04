import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        R
        points[i] = [xi, yi]

        distance formula: (sqrt((x1 - x2)^2 + (y1 - y2)^2))

        return k closest points to origin (order doesn't matter)

        constraints: 1 <= k <= points.length <= 1000

        E
        what if k > len(points):
        return all points

        nvm k is leq len(points)

        if k equal tho return all points

        what to do if there's a tie

        A
        loop through points and calculate distance
        change them in place to a tuple, where:  (dst, pt)

        Time: O(n+ k log n)
        Space: O(k)
        """
        res = []
        distance = -1
        if k == len(points):
            return points

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            dst = math.sqrt((pow(x1, 2)) + (pow(y1, 2)) )
            points[i] = (dst, points[i])

        heapq.heapify(points)

        # O(k log n)
        for _ in range(k):
            pt = heapq.heappop(points)[1]
            res.append(pt)

        return res


