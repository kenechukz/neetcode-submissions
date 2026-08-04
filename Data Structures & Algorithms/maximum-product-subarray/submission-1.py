class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """
        R:
        given nums; arr[int]

        return max product sub array

        E:
        1 <= nums.length <= 1000
        -10 <= nums[i] <= 10

        A:
        3 choices:
        take last elem ~ we found a negative
        take last elem * cur elem
        take cur elem (start new subarray) ~ we found a negative


        [1, -2, 3, -4]
        """

        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for n in nums[1:]:
            # if n is negative, swap
            if n < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)

            ans = max(ans, cur_max)

        return ans

        