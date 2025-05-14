class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n,m = len(a),len(b)
        ans = []
        c = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(max(n,m)):
            aa,bb = 0,0
            if i<n:
                aa = int(a[i])
            if i<m:
                bb = int(b[i])

            temp = aa+bb+c
            res = temp&1
            c = temp>>1
            ans.append(str(res))
        if c>0:
            ans.append('1')
        ans.reverse()
        return ''.join(ans)

