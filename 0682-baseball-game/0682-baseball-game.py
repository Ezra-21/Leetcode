class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        check = {'C','D','+'}
        for operation in operations:
            if operation in check:
                if operation == 'C':
                    stack.pop()
                elif operation == 'D':
                    record = stack[-1]*2
                    stack.append(record)
                else:
                    num1 = stack[-1]
                    num2 = stack[-2]
                    record = num1+num2
                    stack.append(record)

            else:
                stack.append(int(operation))

        return sum(stack)

        