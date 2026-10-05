class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        [4, 2, 3] -> [4, 2, 3, 10]
         4  4  4   in 4  4  7
                   ex 0  2  3  12
        Time: O(n)
        Space: O(n)
        """

        n = len(nums)
        if n==1:
            return nums[0]

        def rob_choice(arr):
            dpArray = [0] *(n - 1)
            dpArray[0] = arr[0]
            for i in range(1,n-1):
                if i-2 >= 0:
                    dpArray[i] = max(dpArray[i-1], arr[i] + dpArray[i-2])
                else:
                    dpArray[i] = max(arr[i-1], arr[i])

            return dpArray[-1]

        return max(rob_choice(nums[:-1]), rob_choice(nums[1:]))
