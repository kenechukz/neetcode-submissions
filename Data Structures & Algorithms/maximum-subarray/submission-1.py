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

        [


        [-1]
        [-1,8]

        [-3, -1, -2]

        [-16, -16, 8, 8, -16, -16]
        """

        max_sum = nums[0]
        cur_sum = 0


        for num in nums:

            if cur_sum < 0:
                cur_sum = 0

            cur_sum += num

            max_sum = max(cur_sum, max_sum)


        return max_sum

