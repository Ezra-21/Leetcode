class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n):
            if n == 0:
                return {""}
            if n == 1:
                return {"()"}
            
            res = set()
            for i in range(n):
                for left in helper(i):
                    for right in helper(n - 1 - i):
                        res.add("(" + left + ")" + right)
            return res

        return list(helper(n))
