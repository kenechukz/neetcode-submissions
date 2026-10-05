
from typing import List
class Solution:
    """
    Summary of Approach:
    I use dynamic programming where dp[i] represents the length of the longest increasing subsequence that
    ends at index i. For each index i, I compare nums[i] with all elements at earlier indices j < i in the array.
    If nums[j] < nums[i], I update dp[i] = max(dp[i], dp[j] + 1). The final answer is the maximum value in dp.



    A:

        if cur < next:
            # we add it to subsequence
            dp[cur_idx] = 1+ dp[next_idx]


        [9,1,4,2,3,3,7]
        [1,4,2,3,2,2,1]

    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
