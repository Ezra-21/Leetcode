class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == ']':
                res = ''
                while stack[-1]!='[':
                    res=stack.pop()+res
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num

                stack.append(int(num)*res)
            else:
                stack.append(ch)
        return ''.join(stack)