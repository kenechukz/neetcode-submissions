from collections import Counter
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets [i, j, k] such that i + j + k = 0.
        """

        nums.sort()  # sort to make duplicate handling easier - O(n log n)
        res = []

        for i, a in enumerate(nums): # O(n^2)

            if i > 0  and nums[i] ==  nums[i-1]:
                continue

            
            l,r = i+1,len(nums)-1

            while l < r:

                threeSum =  a + nums[l] + nums[r]


                if threeSum > 0:
                    r-=1

                elif threeSum < 0:
                    l+=1

                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return res