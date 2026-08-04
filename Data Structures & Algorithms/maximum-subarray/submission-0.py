class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """
        R:
        Given array of ints "nums",
        find subarray with largest sum + return sum

        E:
        1 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000

        solution can be n^2

        A:

        [2,-3,4,-2,2,1,-1,4]

            
        2   l: 0 r: 5
       -3   l: 2 r: 8
        4   l:-1 r: 4


        [-16, -16, 8, 8, -16, -16]

        we want to determine starting point
        """

        max_sum = float("-inf")
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j] 
                max_sum = max(max_sum, cur_sum)


        return max_sum
        