class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        check = {'/','*','+','-'}
        def calculation(a,b,operator):
            if operator == '+':
                return b+a
            if operator == '-':
                return b-a
            if operator == '/':
                return int(b/a)
            if operator == '*':
                return b*a

        for value in tokens:
            if value in check:
                a = stack.pop()
                b = stack.pop()
                store =  calculation(a,b,value) 
                stack.append(store)
            else:
                stack.append(int(value))

        return stack[0]
        