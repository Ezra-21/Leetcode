class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])

        ans = [[0]*(col-2) for _ in range(row-2)]

        for i in range(row-2):
            for j in range(col-2):

                Max = grid[i][j]
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        Max = max(Max,grid[r][c])
                        
                ans[i][j] = Max

        return ans


        