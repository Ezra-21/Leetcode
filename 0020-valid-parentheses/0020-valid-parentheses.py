class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for braket in s:
            if braket == '[' or braket == '(' or braket == '{':
                stack.append(braket)
            else:
                if not stack: return False
                if braket == ']' and stack.pop() != '[':
                    return False
        
                if braket == ')' and stack.pop() != '(':
                    return False
        
                if braket == '}' and stack.pop() != '{':
                    return False
        return not stack

            
        