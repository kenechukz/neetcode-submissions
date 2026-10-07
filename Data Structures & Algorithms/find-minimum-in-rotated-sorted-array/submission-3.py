class Solution:
    def findMin(self, nums: List[int]) -> int:

        """


        how to approach it for next time to get answer on first attempt:
            O(log n) required
            → sorted/rotated structure
            → pivot search
            → choose a comparison that identifies which half cannot contain the pivot
            → preserve the pivot in the remaining range
        """

        l,r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # Minimum must be strictly right of m.
                l = m + 1
            else:
                # Minimum is at m or somewhere left of m.
                r = m

        return nums[l]
