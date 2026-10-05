class Solution {
    public int longestSubarray(int[] nums) {
        int maxSub = 0;
        int zeroCnt = 0;
        int L = 0;
        for (int R = 0; R < nums.length; R++){
            if (nums[R] == 0){
                zeroCnt++;
            }
            while (zeroCnt > 1){
                zeroCnt -= (nums[L] == 0 ? 1 : 0);
                L++;
            }
            // Find all subarrays
            maxSub = Math.max(maxSub, R-L);
        }
        // issue with oneCnt reset
        return maxSub;




        


        


        
    }
}