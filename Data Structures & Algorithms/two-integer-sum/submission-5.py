class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        R:

        nums[i] + nums[j] = target

        return smaller index first

        return index i and j that satisfies condition above

        E:
        constraints
        min len: 2

        if len == 2:
            we could just check if index 0 and index 1 of nums gives target

        what if target < nums[i]

        -5 

        A:
        add all nums to a hashmap - O(n)
        iterate through nums - O(n)
        check if target- nums[i] is in hashmap - O(1)


        """

        #hashMap = {nums[i]: i for i in range(len(nums))}
        hashMap = dict()
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in hashMap:
                return [hashMap[(target - n)], i]

            hashMap[n] = i





        