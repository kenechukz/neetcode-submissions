class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = prefixSum = 0
        prefixSums = {0: 1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixSums:
                count += prefixSums[prefixSum - k]  
            prefixSums[prefixSum] = prefixSums.get(prefixSum, 0) +1

        return count