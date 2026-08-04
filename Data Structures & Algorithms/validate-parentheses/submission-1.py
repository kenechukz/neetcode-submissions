class Solution:
    def isValid(self, s: str) -> bool:

        closing_parentheses = { ")" : "(", "]": "[", "}" : "{"}
        stack = []
        i = 0
        while i < len(s):

            if not s[i] in closing_parentheses:
                stack.append(s[i])

            else:
                if not stack:
                    return False
                top = stack.pop()
                if closing_parentheses[s[i]] != top:
                    return False
            i+=1

        return not stack
        