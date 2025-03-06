class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for c in s:
            if stack_s and c=='#':
                stack_s.pop()
            elif c!='#':
                stack_s.append(c)

        for c in t:
            if stack_t and c=='#':
                stack_t.pop()
            elif c!='#':
                stack_t.append(c)

        return stack_s == stack_t

        