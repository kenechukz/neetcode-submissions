class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # 1 2 3 1
        # l m   r
        #     l r
        #     m

        # 1,2,1,3,5,6,4
        #         l m r

        # 3 2 1

        # we have to variable prev and forward which represent 
        # previous neighbour and next neighbour accordingly
        # we handle edge cases where middle element is at the start or end of array
        # and let prev/forward = neg infinity as specified in question
        # when we middle element is greater than both neighbours we return as it is
        # a peak element
        # when we are less than next element we let left pointer equal forward neighbour index
        # we do this as since forward neighbour is greater than current middle element there's a chance
        # forward nenighbour is greater than it's forward neighbour
        # if prev neighbour is greater we let right pointer equal prev neighbour index
        # we do this as since prev neighbour is greater than current middle element there's a chance
        # prev neighbour is greater than it's prev neighbour
        # we rely on fact that there is at least 1 guaranteed peak element
        # time complexity: O(log n)
        # space complexity: O(1)

        l,r = 0,len(nums)-1
        while (l <= r):
            m = (l+r)//2
            prev = float('-inf') if m - 1 < 0 else nums[m - 1]
            forward = float('-inf') if m + 1 >= len(nums) else nums[m+1]
            if nums[m] > prev and nums[m] > forward:
                return m            
            elif nums[m] < forward:
                l = m+1
            elif nums[m] < prev:
                r = m-1
                
