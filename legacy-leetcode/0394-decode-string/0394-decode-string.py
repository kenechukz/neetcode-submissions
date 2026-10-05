class Solution:
    def decodeString(self, s: str) -> str:


        

        # We iterate through s, adding chars in s to stack as long as the char is not ']'
        # Once we hit ']', we move down the stack and pop the letters, adding them to a substring 
        # till we hit '[' and pop it
        # We then move down stack to find k (integer) and pop digits, adding them to k digit by digit
        # When we hit a non digit we now append the result of "substring * int(k)" to stack
        # We continue till we reach end of s

        # Example:
        # for "3[a12[bc]]" we do subproblem first: 12[bc] -> bcbcbc...bc
        # stack after first subproblem: 3[abcbcbc...bc]
        # stack after second subproblem (final): abcbcbc...bcabcbcbc...bcabcbcbc...bc
        # Time Complexity: O(n)
        # Space Complexity: O(n) ~ stack for auxillary memory

        

        st = []

        for i in range(len(s)):

            if s[i] != "]":
                st.append(s[i])

            else:

                substr = ""

                while st and st[-1] != "[":
                    substr = st.pop() + substr

                st.pop()

                k = ""

                while st and st[-1].isdigit():
                    k = st.pop() + k

                st.append(substr * int(k))

        return "".join(st)

                



        