class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s)-1
        while i>=0:
            if s[i]=='[':
                i-=1
                continue
            elif s[i].isdigit():
                num = ''
                while i>=0 and s[i].isdigit():
                    num = s[i] + num
                    i-=1
                col = ''
                while stack[-1] != ']':
                    col+=stack.pop()
                stack.pop()
                stack.append(col*int(num))

            if i>=0 and s[i]!='[':
                stack.append(s[i])
            i-=1
        stack.reverse()
        return ''.join(stack)
