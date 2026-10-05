class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        R:
        given nums: 0s and 1s
        return max consec. 1s

        E:

        if there are no 1s? -> return 0

        if len == 1 and nums[0] == 1 -> 1 else 0


        A:

        [1,1,0,1,1,1]
         c

        [1,1,0,1,1,1,1,1,0,1,1,1]


        """

        max_ones = 0
        n = len(nums)
        i = 0
        while i < n:
            cur_ones = 0
            while i < n and nums[i] == 1:
                cur_ones += 1
                i += 1

            max_ones = max(max_ones, cur_ones)
            i+=1

        return max_ones
              

        