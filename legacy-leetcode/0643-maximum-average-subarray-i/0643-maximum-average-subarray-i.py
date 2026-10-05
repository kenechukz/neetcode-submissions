class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        maxValue = 0
        value = 0
        for i in range(k):
            value += nums[i]

        maxValue = value
        l+=1
        r+=1
        while r < len(nums):
            # Add next current right pointer value to value
            value -= nums[l-1]
            value += nums[r]
            if value > maxValue:
                maxValue = value
                
            l+=1
            r+=1
        return maxValue/k


            


            
            

             




        