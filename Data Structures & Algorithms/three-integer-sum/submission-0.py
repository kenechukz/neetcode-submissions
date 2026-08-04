from collections import Counter
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets [i, j, k] such that i + j + k = 0.
        """

        nums.sort()  # sort to make duplicate handling easier
        hashMap = Counter(nums)
        res = set()

        for l in range(len(nums)):
            i = nums[l]
            for r in range(l + 1, len(nums)):
                j = nums[r]
                k = -(i + j)

                # ensure triplets are in sorted order to avoid duplicates like (1, -1, 0)
                if k < j:
                    continue

                if k not in hashMap:
                    continue

                # check if there are enough counts for repeating numbers
                if (k == i and hashMap[i] < 2) or (k == j and hashMap[j] < 2) or (i == j == k and hashMap[i] < 3):
                    continue

                res.add((i, j, k))

        # convert tuples to lists for final output
        return [list(x) for x in res]
