from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        Question:
        Given array of ints "nums",
        find subarray with largest sum + return sum

        Edge cases:
        1 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000

        Approach:

        Kadane's Algorithm

        if prefix sum (sum of elements behind current element) i.e. cur_sum is less than zero, we reset
        it to 0 since any negative prefix would only reduce the sum of a future subarray.


        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        max_sum = nums[0]
        cur_sum = 0


        for num in nums:

            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num

            max_sum = max(cur_sum, max_sum)


        return max_sum
