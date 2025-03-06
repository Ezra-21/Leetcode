class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0]*(n*n+1)
        for i in range(n):
            for j in range(n):
                arr[grid[i][j]]+=1
        repeat,miss = 0,0
        for i,val in enumerate(arr[1:]):
            if val == 0:
                miss = i+1
            elif val==2:
                repeat = i+1
            if repeat and miss:
                break
        return repeat,miss