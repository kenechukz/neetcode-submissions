import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """
        R
        nums: unsorted ints


        return kth largest elem (in sorted order)

        brute force: 
        sort array (n log n)
        then loop k times 

        time: O( k + n log n)



        E:
        constraints:
        1 <= k <= nums.length <= 10000
        ***important** -1000 <= nums[i] <= 1000

        k == len(nums)
        A: 
        use heap (heapify)  - O(n)

        
        pop k times (k log n)

        time : O(n + k log n)


        nums = [2,3,1,5,4], k = 2
        make neg
        heap: -5 -4 -3 -2 -1
           k   1  2  3  4  5

           n -k +1
           5-4 +1



        heap 1 2 3 4 5

        k > half len(heapMax):
            use min heap
        
        """
        n = len(nums)
        minHp = [x for x in nums]
        maxHp = [-x for x in nums]

        heapq.heapify(minHp)
        heapq.heapify(maxHp)


        if k == n:
            return heapq.heappop(minHp)

        if k <= math.ceil(n / 2):
            for _ in range(k):
                val = heapq.heappop(maxHp)
            return -val

        else:
            for _ in range((n - k)+1):
                val = heapq.heappop(minHp)
            return val



        
        

        
        