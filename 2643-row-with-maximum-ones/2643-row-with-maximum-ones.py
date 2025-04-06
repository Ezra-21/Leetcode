class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i,row in enumerate(mat):
            count = row.count(1)
            if count>ans[0]:
                ans = [i,count]
        return ans

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]

        for i, row in enumerate(mat):
            ones_count = sum(row)

            if ones_count > ans[1]:
                ans = [i, ones_count]

        return ans