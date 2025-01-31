class Solution:
    def interpret(self, command: str) -> str:
        hashh = {'G':'G','()':'o','(al)':'al'}
        ans = []
        res = ''
        for char in command:
            res += char
            if res in hashh:
                ans.append(hashh[res])
                res = ''
        return ''.join(ans)
        