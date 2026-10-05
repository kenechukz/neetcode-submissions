class Solution {
    public void moveZeroes(int[] nums) {
        int l = 0;
        int r = 1;
        int temp;


        if (nums.length == 1){
            return;
        }

        while (r < nums.length){
            if (nums[l] == 0 && nums[r] != 0){
                temp = nums[l];
                nums[l] = nums[r];
                nums[r] = temp;
            }
            if (nums[l] != 0){
                l++;
            }
            if (nums[r] == 0 || r <= l){
                r++;
            } 
        }
        return;
    }
}