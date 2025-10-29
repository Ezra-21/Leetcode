class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def dfs(res,check):
            if len(res) == n:
                ans.append(res)
                return
            
            dfs(res+'1',True)
            
            if check:
                dfs(res+'0',False)
        dfs('',True)
        return ans
            

        