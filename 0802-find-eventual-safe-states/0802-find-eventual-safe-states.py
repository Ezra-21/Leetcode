from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        outdegree = [0] * len(graph)

        # Reverse the edges and build outdegree
        for node, edges in enumerate(graph):
            outdegree[node] = len(edges)
            for edge in edges:
                adj_list[edge].append(node)  # reverse the graph here

        queue = deque()
        for node, outdeg in enumerate(outdegree):
            if outdeg == 0:
                queue.append(node)

        safeNode = [False for _ in range(len(graph))]

        while queue:
            node = queue.popleft()
            safeNode[node] = True
            for nei in adj_list[node]:
                outdegree[nei] -= 1  # decrement the outdegree of the neighbor
                if outdegree[nei] == 0:
                    queue.append(nei)

        return [node for node, is_safe in enumerate(safeNode) if is_safe]
