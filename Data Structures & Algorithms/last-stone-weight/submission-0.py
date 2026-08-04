import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        """
        R
        smash two heaviest stones each iter

        need two biggest stones - heap max

        pop twice till heap is 0 or len 1

        E
        base case:
        len 1

        constraints:
        1 <= stones.length <= 20
        1 <= stones[i] <= 100

        A:
        make stone a heap
        if x== y
         pop both

        if x < y


        6 4 3 2 2

        x = 6, y = 4

        3 2 2 2

        x = 3 y = 2
        2 2 1



        """
        heap = []
        heapq.heapify(heap)
        for st in stones:
            heapq.heappush(heap, -st)

        
            
        while heap:
            
            if len(heap) == 1:
                return -heap[0]

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            # negative x and y
            if x < y:
                heapq.heappush(heap,-(-x + y)  )

        
        return 0
        


        