class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0


        for num in nums:

            curMax = max(num + rob1, rob2)
            
            rob1 = rob2
            rob2 = curMax

        return rob2
            


        