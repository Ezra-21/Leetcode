class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        nn = len(grid)
        n,s,e,w = [0]*nn,[0]*nn,[0]*nn,[0]*nn
        for i in range(nn):
            for j in range(nn):
                n[j] = max(n[j],grid[i][j])
                s[j] = max(s[j],grid[i][j])
                e[i] = max(e[i],grid[i][j])
                w[i] = max(w[i],grid[i][j])

        ans = 0
        for i in range(nn):
            for j in range(nn):
                minn = min(n[j],s[j],e[i],w[i])
                ans += (minn-grid[i][j])

        return ans

        