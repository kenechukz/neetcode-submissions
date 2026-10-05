class Solution {
    public boolean increasingTriplet(int[] nums) {
       double i = Double.POSITIVE_INFINITY;
       double j = Double.POSITIVE_INFINITY;
       double k = Double.POSITIVE_INFINITY;

       for (int num: nums){
            if (num < i){
                i = num;
            }
            else if (num > i && num < j){
                j = num;

            }
            else if (num > j){
                k = num;
            }        
       }
       return i != Double.POSITIVE_INFINITY && j != Double.POSITIVE_INFINITY && k != Double.POSITIVE_INFINITY;
    }
}