# for every query ans = '&' of all weight of components in which they lie.
# Reason: to minimise bitwise '&' , it's better if we can include as much no of elements and 
# amximum we can include = no of edges in that component.
# If they are not in same component then ans = -1
# And if they are same then ans = 0

# Since talking about component then 1st thing comes in mind is 'union-find'.
# But here we just have to take '&' of all , we won't check here 'cycle' in union 
# because we have to find 'walk' and vertices can repeat.
# So we will take '&' of all edges given.


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
        else:
            self.parent[yy] = xx
        # to avoid checking conditions like to whom to add weight, update 'weights' for both 'xx' and 'yy'.
        self.weights[xx] = self.weights[yy] = self.weights[xx] & self.weights[yy] & weight   
        if self.rank[xx] == self.rank[yy]:
            self.rank[xx] += 1
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
    

# I was trying to do like below but getting wrong ans
class DSU:
    def __init__(self, n):
        self.parent=    [i for i in range(n)]
        self.size=      [1 for i in range(n)]
        self.andValue = [2**32 -1] * n
    
    def findParent(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2, w):  
        p1, p2= self.findParent(n1), self.findParent(n2)
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2  
            self.size[p2] += self.size[p1]
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        self.andValue[p2] = self.andValue[p1] = self.andValue[p2] & self.andValue[p1] & w

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)
        for u, v , w in edges:
            dsu.union(u, v, w)
            
        print(dsu.parent, dsu.andValue, "parent")   
        ans = []
        for u, v in query:
            if u == v:
                ans.append(0)
            elif dsu.parent[u] == dsu.parent[v]:
                ans.append(dsu.andValue[dsu.parent[u]])
            else:
                ans.append(-1)
        return ans

        
    