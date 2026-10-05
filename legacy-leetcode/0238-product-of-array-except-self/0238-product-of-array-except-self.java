class Solution {
    public int[] productExceptSelf(int[] nums) {

        int len = nums.length;
        int[] left = new int[len];
        int[] right = new int[len];

        left[0] = 1;
        for(int i = 0; i < len-1; i++){
            left[i+1] = left[i] * nums[i];
        }

        right[len-1] = 1;
        for(int i = len-1; i > 0; i--){
            right[i-1] = right[i] * nums[i];
        } 

        for (int i = 0; i < len; i++){
           nums[i] = left[i] * right[i]; 
        }

        return nums;


        
    }
}