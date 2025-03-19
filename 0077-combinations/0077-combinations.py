class Solution:
    def backtrack(self,candidate,coll,ans,n,k):
        if len(coll)==k:
            ans.append(coll[:])
            return
    
        for next_candidate in range(candidate,n+1):
            coll.append(next_candidate)
            self.backtrack(next_candidate+1,coll,ans,n,k)
            coll.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.backtrack(1,[],ans,n,k)
        return ans




