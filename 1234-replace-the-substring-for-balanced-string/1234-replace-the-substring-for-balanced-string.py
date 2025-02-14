class Solution:
    #"QQQWQQWE"
    def balancedString(self, s: str) -> int:
        def solve(dic,bal):
            for val,fre in dic.items():
                if fre>bal:
                    return False
            return True

        hashh = Counter(s)
        min_length = len(s)
        balance = len(s)//4
        j = 0

        if solve(hashh,balance):
            return 0

        for i in range(len(s)):
            hashh[s[i]]-=1
            while solve(hashh,balance):
                min_length = min(min_length,i-j+1)
                hashh[s[j]]+=1
                j+=1

        return min_length

