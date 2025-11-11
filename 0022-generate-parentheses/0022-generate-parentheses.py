class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res

        def helper(curr, open_br,closed_br):
            if len(curr) == 2*n:
                res.append(curr)
                return
            
            if open_br < n:
                helper(curr+'(',open_br+1,closed_br)
            
            if closed_br < open_br:
                helper(curr+')',open_br,closed_br+1)
            return
        
        helper('',0,0)
        return res