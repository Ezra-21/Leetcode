class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i):
            res = ""
            num = 0

            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1

                elif s[i] == '[':
                    decoded, i = helper(i + 1)
                    res += num * decoded
                    num = 0  
                elif s[i] == ']':
                    return res, i + 1
                else:
                    res += s[i]
                    i += 1

            return res, i

        decoded, _ = helper(0)
        return decoded
