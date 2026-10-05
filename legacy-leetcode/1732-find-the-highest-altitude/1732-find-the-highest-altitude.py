class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Approach
        # To get prefixSum[i] we add the thing at gain[i-1] to prefixSum[i-1]
        # It's gain[i-1] as initial altitude 0 is not in gain array so we have to start
        # at first index of gain rather than index 1
        # Time complexity: O(n)
        # Space complexity: 0(1)
        
        gain.insert(0, 0)
        for i in range(1, len(gain)):
            gain[i] = gain[i] + gain[i-1]

        return max(gain)
        