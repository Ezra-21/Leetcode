class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90(mat):
            row = col = len(mat)
            trans = [[0]*row for _ in range(col) ]
            for c in range(col):
                for r in range(row):
                    trans[r][c] = mat[c][r]
            for i in range(row):
                trans[i].reverse()
            return trans

        for _ in range(4):
            if mat == target:
                return True
            print(mat)
            mat = rotate_90(mat)
        return False