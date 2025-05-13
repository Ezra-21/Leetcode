class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1,n+1):
            temp = []
            while i:
                temp.append(0 if i%2==0 else 1)
                i//=2
            ans.append(sum(temp))
        return ans
