class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hashh = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hashh[i+j].append(mat[i][j])
        ans = []
        for val,listt in hashh.items():
            if val%2==0:
                listt.reverse()
            ans.extend(listt)

        return ans
        