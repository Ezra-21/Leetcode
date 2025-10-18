class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def dfs(temp,check):

            if len(temp) == n:
                res.append(temp)
                return 

            if check == 1:
                dfs(temp+'0',0)

            dfs(temp+'1',1)

        dfs('',1)
        return res