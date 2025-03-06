class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        sett = {'*','/','+','-'}
        ans = 0
        def calculate(sign,num1,num2):
            if sign == '+':
                return num1+num2
            elif sign == '*':
                return num1*num2
            elif sign == '-':
                return num1-num2
            elif sign == '/':
                return int(num1/num2)

        for token in tokens:
            if token in sett:
                a = stack.pop()
                b = stack.pop()
                ans = calculate(token,b,a)
                stack.append(ans)
            else:
                stack.append(int(token))
        
        return stack[0]
           