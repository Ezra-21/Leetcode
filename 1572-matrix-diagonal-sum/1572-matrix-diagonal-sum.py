class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        left = 0
        right = len(mat)-1
        for i in range(len(mat)):
            if left == right:
                count += mat[right][i]
            else:
                summ = mat[left][i] + mat[right][i]
                count += summ
            left += 1
            right -= 1
        return count