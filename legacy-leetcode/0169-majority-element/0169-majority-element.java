class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> elementFrequency = new HashMap<>();
        int threshold = nums.length / 2;
        for (int element : nums ){
            if (!elementFrequency.containsKey(element)){
                elementFrequency.put(element, 1);
            }
            else {
                elementFrequency.put(element, elementFrequency.get(element)+1);
            }

            if (elementFrequency.get(element) > threshold){
                return element;
            }
        }

        return -1;
        
    }
}