import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # create a min heap
        # iterate through nums (O(N) time)
        # push to min heap k times (log k time, k space)
        # when size is == k, we push to min heap and pop from it
        # when finished iterating nums, return top of min heap
        # Time complexity: O(n log k)
        # Space complexity: O(k)

        min_heap = []

        hq.heapify(min_heap)

        for num in nums:

            if len(min_heap) < k:
                hq.heappush(min_heap, num)

            else:
                hq.heappushpop(min_heap, num)

        return min_heap[0]
