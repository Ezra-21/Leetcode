class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for val in s:
            if val =='#':
                if stack_s:
                    stack_s.pop()
                continue
            stack_s.append(val)
        
        for val in t:
            if val =='#':
                if stack_t:
                    stack_t.pop()
                continue
            stack_t.append(val)

        return stack_s == stack_t
        