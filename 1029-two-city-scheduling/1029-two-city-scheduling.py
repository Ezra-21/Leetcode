class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:(x[1]-x[0]))
        n = len(costs)//2
        ans = 0
        for a,b in costs[:n]:
            ans+=b
            
        for a,b in costs[n:]:
            ans+=a

        return ans


        