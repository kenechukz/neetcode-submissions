import math
class Solution:
    def performOperation(self,operand1, operand2, operator) -> int:
        if operator == '+':
            return operand1 + operand2
        if operator == '-':
            return operand1 - operand2
        if operator == '*':
            return operand1 * operand2
        if operator == '/':
            if (operand1 < 0 and operand2 > 0) or (operand2 < 0 and operand1 > 0):
                return math.ceil(operand1/operand2)
            
            return operand1 // operand2
        else:
            return 0

    
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        
        if len(tokens) == 1 and tokens[0].lstrip('+-').isnumeric():
            return int(tokens[0])
        elif len(tokens) == 1 and not tokens[0].lstrip('+-').isnumeric():
            return result
        
        
        for token in tokens:
            operand1 = 0
            operand2 = 0
            operator = ''
            
            if token.lstrip('+-').isnumeric():
                stack.append(token)
                
            else:
                if len(stack) < 2:
                    return 0
                operand2 = stack.pop()
                operand1 = stack.pop()
                operator = token
                #print(f'Operation to be completed: {operand1} {operator} {operand2}')
                result = self.performOperation(int(operand1),int(operand2),operator)
                #print(result)
                stack.append(result)
                
        return result
                
    

        