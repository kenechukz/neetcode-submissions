import heapq
class KthLargest:

    """
    R:
    Constructor():
    Initiliase object (with k and nums)

    k = 3, inp: [1,2,3,3]
    keep kth largest on top?

    heappop k times
    repopulate heap (n)

    Time: O( k log n)
    Space: O(n)

    heap:
        3
        3
        2
        1


    add(val) -> 
    add val to stream + return kth largest element 
    """

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        for x in nums:
            heapq.heappush(self.stream, -x)
        
        self.k = k



        

    def add(self, val: int) -> int:

        heapq.heappush(self.stream, -val)

        temp = []
        for i in range(self.k):
            cur = heapq.heappop(self.stream)
            temp.append(cur)

        for x in temp:
            heapq.heappush(self.stream, x)
        
        return -cur


        
