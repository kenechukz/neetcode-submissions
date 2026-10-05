class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        R:
        given nums
        can perfom at most 3 changes

        return min difference between largest and smallest val after changes
        E:

        constr: 1<= n <= 10^5
        -10^9 <= nums[i] <= 10^9

        if len == 1:
            return 0

        if min == max:
            return 0

        if n <= 4:
            return 0

        A:
        [1,5,0,10,14]
        n = 5
        maxV = 14
        minV = 0 
        [0, 1, 5, 10, 14]

        [1,5,0,10,14, 4, 17, 9]

        [0, 1, 4, 5, 9, 10, 17]

        you have 4 options:
        remove 3 from front, remove 3 from back
        remove 2 from front 1 from back,
        remove 1 from front 2 from back


        """

        if len(nums) <= 4:
            return 0

        nums.sort()
        return min(nums[-1] - nums[3], nums[-4] - nums[0], nums[-2] - nums[2], nums[-3] - nums[1])
        