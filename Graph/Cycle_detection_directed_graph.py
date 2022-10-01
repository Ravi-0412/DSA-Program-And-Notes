# method 1: By DFS
# it can't be done by one array and with parent logic(like undirected graph) because
# the adjacent node of current vertex can also be visited by other path but it may not be the cycle
#  because in directed graph is one directional (btw two vertex) unlike undirected graph

# so here we will need two array one dfs_visited to check if the adjacent node of curr node is 
# visited in current DFS call or not.
# if visited in curr DFS call then it contain a cycle otherwise not

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.dfs_visited= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)

    def DFS_Visit(self, adj,src):
        self.visited[src]= True
        self.dfs_visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                if self.DFS_Visit(adj, u):  # if for any component there is a cycle
                    return True
            # if adjacent node is visited then check if that is visited in current cycle or not
            elif self.dfs_visited[u]==True:
                return True
        # while traversing back(i.e curr node has no adjacent node) make dfs_visited of current node= False 
        # to check again in next DFS call or next component
        self.dfs_visited[src]= False
        # return False   # no need of this line 


    def isCycle(self,n, adj):
        for i in range(n):
            if not self.visited[i]:
                if self.DFS_Visit(adj,i):
                    return True
        # if no component has cycle then return False
        return False


g= Graph(9)
# test case 1: only one component
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(2,5)
# g.addEdge(4,2)
g.addEdge(5,4)
g.addEdge(6,1)
g.addEdge(6,7)
g.addEdge(7,8)
# g.addEdge(8,6)

# test case 2: more than one component
print(g.AdjList)
print(g.isCycle(9,g.AdjList))


# method 2: using BFS(kahn's Algorithm)
# this is under topological sort (Method 2)