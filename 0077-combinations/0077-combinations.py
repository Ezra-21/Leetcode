class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        candidate = list(range(1,n+1))
        def backtrack(idx,path):
            if len(path)==k:
                ans.append(path[:])
                return 

            if idx==len(candidate):
                return 

            path.append(candidate[idx])
            backtrack(idx+1,path)

            path.pop()
            backtrack(idx+1,path)

        backtrack(0,[])
        return ans

        





