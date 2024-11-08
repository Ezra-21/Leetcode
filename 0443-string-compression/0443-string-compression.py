class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        s = ''
        count,i = 0,1
        while i<len(chars):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count == 0:
                    s += chars[i-1]
                else:
                    s += chars[i-1]
                    s += str(count+1)
                    count = 0
            i+=1
        
        if count == 0:
            s += chars[i-1]
        else:
            s += chars[i-1]
            s += str(count+1)
            count = 0
            
        chars.clear()
        for i in range(len(s)):
            chars.append(s[i])
        return len(chars)

        