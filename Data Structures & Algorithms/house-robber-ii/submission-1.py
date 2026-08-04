class Solution:
    def rob(self, nums: List[int]) -> int:

        """
        R:
        given nums:
        nums[i] - amount of money ith house has

        house are in circle, so first and last house are neighbours

        can't rob 2 adj houses

        return max money u can rob, without alerting police
        E:
        1 <= nums.length <= 100
        0 <= nums[i] <= 100

        constr. suggest O(N^2)

        if len(nums) == 1 ? cannot rob
        base case

        A:
        [2,9,8,3,6]
        take max of prev and cur + amount at i-2

        from index 0 to n-2 (inclusive)
        [2,9,8,3]

        [2,9,10,12]

        from 1 to n-1 (inclusive)
        [9,8,3,6]

        [9,9,12,15]
        
          



        """

        maxAmount = 0
        n = len(nums)

        if len(nums) < 3:
            return max(nums)


        def rob_house(houses):

            for i in range(1,len(houses)):
                if i > 1:
                    houses[i] = max(houses[i-1], houses[i] +  houses[i-2])

                else:
                    houses[i] = max(houses[i], houses[i-1])

            return houses[-1]



        return max(rob_house(nums[0:n-1]), rob_house(nums[1:n]))

        