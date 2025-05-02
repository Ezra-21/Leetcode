class Solution:
    class UnionFind:
        def __init__(self, size):
            self.parent = [i for i in range(size)]
            self.rank = [0] * size

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):
            root_x = self.find(x)
            root_y = self.find(y)

            if root_x == root_y:
                return

            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_y] < self.rank[root_x]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = self.UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n): 
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        roots = []

        for i in range(n):
            root = uf.find(i)  
            roots.append(root)

        
        return len(set(roots))

