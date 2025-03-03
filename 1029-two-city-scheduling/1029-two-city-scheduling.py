class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x:(x[0]-x[1]))
        print(costs)
        n = len(costs)//2
        ans = 0
        for a,b in costs[:n]:
            ans+=a
            
        for a,b in costs[n:]:
            ans+=b

        return ans


        