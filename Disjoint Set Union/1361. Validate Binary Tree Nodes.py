# Logic: Any binary tree follow 2 properties:
# 1) There shouldn't be any cycle 
# 2) All nodes should be connected in single component.

# But here tree is not given only leftchild and rightChild of a node is given(i.e indegree[child] = 1 exactly)
# So when we will try to connect them together we can connect because Dsu doesn't care about orientation.
# Dsu will simply connect them together avoiding cycle.

# Note: But here orientation will also matter i.e one node can be either left or right child of a single node.
# So once we have included any node as child of any other node then that node can't be child further.

# So we need to keep track of node that is included as child.

# Note: We can do this by bfs or dfs , just first find the root and then we need to check all three conditions treating link as undirected graph.

# See the code of bfs and dfs in graph

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findParent(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        p1, p2= self.findParent(n1), self.findParent(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        return True

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        child = set()  # will take care of node which is included as child
        dsu = DSU(n)
        for i in range(n):
            l , r = leftChild[i], rightChild[i]
            if l != -1:
                # if node 'l' is already included as child of any other node before
                if l in child or dsu.union(i, l) == False:
                    return False
                child.add(l)
            if r != -1:
                if r in child or  dsu.union(i, r) == False :
                    return False
                child.add(r)
        # Now to make sure that they are connected in a single component only
        maxSize = max(dsu.size)
        return True if maxSize == n else False
    

# My mistake at 1st time
# Was not taking care of node included as child.

# won't work here:
# 3
# [1,-1,-1]
# [-1,-1,1]

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        child = set()
        dsu = DSU(n)
        for i in range(n):
            l , r = leftChild[i], rightChild[i]
            if l != -1:
                if l in child or dsu.union(i, l) == False:
                    return False
                child.add(l)
            if r != -1:
                if r in child or  dsu.union(i, r) == False :
                    return False
                child.add(r)
        maxSize = max(dsu.size)
        return True if maxSize == n else False
