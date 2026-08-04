class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        R:

        given array digits: represents a large integer

        return digits incremented by 1

        E:
        1 <= digits.length <= 100
        digits[i] = 0-9

        can we end up with res with greater len than input? YES

        A:
        [9]
    
        output: [1,0]
        
        # case 2

        [9,9,9,9]
       +       1
               0    

        initially : carry = 0
        res = (digits[-1] + 1) % 10
        digits[i] = res
        for remaining digits:
            while we have a carry
        res = (digits[-1] + 1) % 10
        digits[i] = res + carry
        carry = digits[i] // 10

        if carry after we reach end of loop:
            preprend to digits
        """

        res = (digits[-1] + 1)
        digits[-1] = res % 10
        carry = res // 10

        i = len(digits)- 2
        if len(digits) > 1:
            while  i >= 0 and carry != 0:
                res = (digits[i] + carry) 
                digits[i] = res % 10
                carry = res // 10
                i -= 1

        if carry != 0:
            digits = [carry] + digits
        return digits
                
                
                





        