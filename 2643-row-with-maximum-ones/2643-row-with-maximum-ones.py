class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i,row in enumerate(mat):
            count = row.count(1)
            if count>ans[1]:
                ans = [i,count]
        return ans
