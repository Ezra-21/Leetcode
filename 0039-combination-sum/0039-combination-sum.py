class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        temp = []

        def dfs(i,total):
            if total == target:
                res.append(temp.copy())
                return
            if total > target or i==len(candidates):
                return

            temp.append(candidates[i])
            dfs(i,total+candidates[i])

            temp.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res
