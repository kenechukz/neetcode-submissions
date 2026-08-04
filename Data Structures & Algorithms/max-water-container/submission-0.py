class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """
        Given height arr (int), where i repr. height of ith bar
        choose 2 bars
        Return max water container can store

        E:

        if height[l] < height[r]:
            use min height and do as follows:
            
            minHeight x r-l+1

        if equal:
            regular

        A:

        """

        l,r = 0, len(heights)-1
        res = 0
        while l < r:

            dis = r-l
            if heights[l] >= heights[r]:
                res = max(res,heights[r] * dis)
                r-=1

            else:
                res = max(res,heights[l] * dis)
                l+=1

        return res



        