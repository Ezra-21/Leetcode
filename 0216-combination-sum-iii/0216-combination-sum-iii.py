class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(num,total,collect):
            if total == n and len(collect) == k:
                res.append(collect)
                return

            if total>n or len(collect)>k or num>9:
                return

            dfs(num+1,total+num,collect+[num])
            
            dfs(num+1,total,collect)

        dfs(1,0,[])
        return res

        