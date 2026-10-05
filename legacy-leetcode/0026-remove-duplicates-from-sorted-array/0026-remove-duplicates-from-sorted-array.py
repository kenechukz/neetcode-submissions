class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        R:
        given sorted nums (increasing)

        remove duplicates in place
        order to be kept the same

        E:
        1 <= nums.length <= 3 * 10^4  -> nee O(N) solution
        -100 <= nums[i] <= 100

        A:

        if cur num is not equal to previous we add it to array at position k, and increment k
        we increment i always

        
        """

        k = i = 1
        n = len(nums)
        while i < n:
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1

            i+=1

        return k

            





        