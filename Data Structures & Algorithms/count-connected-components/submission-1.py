class UnionFind:
            def __init__(self, n):
                self.par = {}
                self.rank = {}
                for i in range(n):
                    self.par[i] = i
                    self.rank[i] = 1
            
            def find(self, n):
                p = self.par[n]
                while p != self.par[p]:
                    self.par[p] = self.par[self.par[p]]
                    p = self.par[p]
                return p
            
            def union(self, n1, n2):
                r1 = self.find(n1)
                r2 = self.find(n2)

                if self.rank[r1] < self.rank[r2]:
                    self.par[r1] = r2
                elif self.rank[r2] < self.rank[r1]:
                    self.par[r2] = r1
                else:
                    self.par[r2] = r1
                    self.rank[r2] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for i in range(len(edges)):
            x, y = edges[i]
            uf.union(x, y)
        
        nonorphans = 0
        for key in uf.par:
            if uf.par[key] != key:
                nonorphans += 1

        return n - nonorphans 
        