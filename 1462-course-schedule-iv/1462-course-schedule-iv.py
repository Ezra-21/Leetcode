class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False] * n for _ in range(n)]
        
        for u,v in prerequisites:
            graph[u][v] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][k] and graph[k][j]:
                        graph[i][j] = True

        ans = []
        for u,v in queries:
            ans.append(graph[u][v])

        return ans

