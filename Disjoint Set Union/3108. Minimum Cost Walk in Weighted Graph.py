"""
for every query ans = '&' of all weight of components in which they lie.
Reason: to minimise bitwise '&' , it's better if we can include as much no of elements and 
maximum we can include = no of edges in that component.
If they are not in same component then ans = -1
And if they are same then ans = 0

Since talking about component then 1st thing comes in mind is 'union-find'.
But here we just have to take '&' of all , we won't check here 'cycle' in union 
because we have to find 'walk' and vertices can repeat.
So we will take '&' of all edges given in that component.

Time complexity: O(N + E + Q), where E is the number of edges and Q is the number of queries

Note: If we are asked to find maximum 'OR' for each query then, solution will be exacty same. Just we need take OR instead of 'AND'.
Because 'OR' value increases when we include maximum possible element, same way 'AND' decreases.
"""


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [(1<<32) -1] * n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y, weight):
        xx, yy = self.find(x), self.find(y)
        if self.rank[xx] < self.rank[yy]:
            self.parent[xx] = yy
            self.rank[yy] += self.rank[xx]        
        else:
            self.rank[xx] += self.rank[yy]    
            self.parent[yy] = xx
        # to avoid checking conditions like to whom to add weight, update 'weights' for both 'xx' and 'yy'.
        self.weights[xx] = self.weights[yy] = self.weights[xx] & self.weights[yy] & weight
    def minimum_cost_of_walk(self, x, y):
        if x == y: 
            return 0
        if self.find(x) != self.find(y): 
            # both don't lie in same component
            return -1
        # return weight of any of the parent
        return self.weights[self.find(x)]

class Solution:
    def minimumCost(self, n, edges, query):
        uf = DSU(n)
        for x, y, z in edges:
            # pass the weight also 
            uf.union(x, y, z)
        return [uf.minimum_cost_of_walk(x, y) for x, y in query]
    


        
    
