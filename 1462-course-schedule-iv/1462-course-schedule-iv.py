class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False] * n for _ in range(n)]
        
        for u,v in prerequisites:
            graph[u][v] = True

        

        ans = []
        for u,v in queries:
            ans.append(graph[u][v])

        return ans