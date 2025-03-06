class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(num1,num2,sign):
            if sign == '+':
                return num1+num2
            if sign == '-':
                return num1-num2
            if sign == '*':
                return num1*num2
            if sign == '/':
                return int(num1/num2)
        op = {'+','-','*','/'}
        stack = []
        for c in tokens:
            if c in op:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                result = operation(n1,n2,c)
                stack.append(result)
            else:
                stack.append(c)

        return int)
        
        