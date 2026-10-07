class Solution:
    def findMin(self, nums: List[int]) -> int:

        """

        Intuition:
        Find the pivot/minimum with binary search.

        A rotated sorted array consists of two sorted sections. Maintain the invariant
        that the minimum always remains within nums[left:right + 1].

        Compare nums[mid] with nums[right]:

        - If nums[mid] > nums[right], the rotation point must be strictly to the right
        of mid, so discard the left half including mid.
        - Otherwise, mid may be the minimum, so keep mid and discard only the portion
        strictly right of it.

        Continue until left == right; that one remaining position is the minimum.

        Time: O(log n)
        Extra space: O(1)

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
