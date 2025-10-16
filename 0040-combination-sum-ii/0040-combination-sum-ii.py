class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i,total,temp):
            if total == target:
                res.append(temp)
                return 

            if total > target or i == len(candidates):
                return 
            
            dfs(i+1,total+candidates[i],temp+[candidates[i]])

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1,total,temp)
        
        dfs(0,0,[])
        return res