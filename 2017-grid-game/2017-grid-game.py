class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix_row1 = list(accumulate(grid[0],initial = 0))
        prefix_row2 = list(accumulate(grid[1],initial = 0))

        ans = float('inf')

        for i in range(len(grid[0])):
            top = prefix_row1[-1]-prefix_row1[i+1]
            bottom = prefix_row2[i]

            secondRobot_point = max(top,bottom)  
            ans = min(ans,secondRobot_point)

        return ans     

        