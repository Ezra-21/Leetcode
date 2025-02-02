class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(n,hashh):
            if n==1 or n==2:
                return 1
            if n==0:
                return 0
            if n not in hashh:
                hashh[n] = solve(n-1,hashh)+solve(n-2,hashh)+solve(n-3,hashh)
            return hashh[n]
        hashh = {}
        return solve(n,hashh)

        