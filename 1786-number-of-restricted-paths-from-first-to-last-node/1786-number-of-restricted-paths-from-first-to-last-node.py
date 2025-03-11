
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[n] = 0
        min_heap = [(0, n)]  

        while min_heap:
            d, node = heapq.heappop(min_heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))

        memo = {}

        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]

            ways = 0
            for neighbor, _ in graph[node]:
                if dist[node] > dist[neighbor]:  
                    ways = (ways + dfs(neighbor)) % MOD

            memo[node] = ways
            return ways

        return dfs(1)
