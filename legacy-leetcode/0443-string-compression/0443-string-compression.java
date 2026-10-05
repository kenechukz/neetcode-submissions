class Solution {
    public int compress(char[] chars) {

        int groupLength = 1;
        int res = 0;
        int i = 0;
        
        while (i < chars.length){

            while(i+groupLength < chars.length && chars[i+groupLength] == chars[i]){
                groupLength++;
            }

            chars[res++] = chars[i];
            if (groupLength > 1){

                for (char c: Integer.toString(groupLength).toCharArray()){
                    chars[res++] = c;
                }
            }
            i += groupLength;
            groupLength = 1;

        }
        
        
        return res;
        
    }
}