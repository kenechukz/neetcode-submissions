class Solution {
    public int longestOnes(int[] nums, int k) {
        int L = 0, zeroCnt = 0, maxConsc = 0;
        for (int R = 0; R < nums.length; R++) {
            if (nums[R] == 0) {
                zeroCnt++;
            }
            while (zeroCnt > k) { // Shrink window when zero count exceeds k
                if (nums[L] == 0) {
                    zeroCnt--;
                }
                L++;
            }
            // Update maxConsc for every valid subarray
            maxConsc = Math.max(maxConsc, R - L + 1);
        }
        return maxConsc;
    }
}
