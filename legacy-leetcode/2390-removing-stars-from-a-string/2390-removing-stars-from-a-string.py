class Solution:
    def removeStars(self, s: str) -> str:
        
        #lee*cod*e
        #lecoe
        
        #given string which can contains *

         
        # if current char in string is a star '*' and stack exists 
        # we pop top of stack
        # otherwise we add that char the stack 
        # at the end we join the array into a string
        # Time complexity: O(n) ~ Iterating through characters in string takes n iterations 
        # n being the length of the string
        # Space complexity: O(n) ~ Auxillary memory in use of stack which is of size n

        stack = []
        for i in range(len(s)):

            if s[i] == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)
        
                
            

        
    


        
                