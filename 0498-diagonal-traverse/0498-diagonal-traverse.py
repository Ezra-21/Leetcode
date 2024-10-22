class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        order = [[] for _ in range(row + col - 1)]
        ans = []
        for i in range(row):
            for j in range(col):
                order[i + j].append(mat[i][j])

        for i in range(len(order)):
            if i % 2 == 0:
                order[i].reverse()
            ans.extend(order[i])
        return ans
