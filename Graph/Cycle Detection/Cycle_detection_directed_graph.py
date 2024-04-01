# method 1: By DFS
# it can't be done by one array and with parent logic(like undirected graph) because
# the adjacent node of current vertex can also be visited by other path but it may not be the cycle
#  because in directed graph is one directional (btw two vertex) unlike undirected graph.
# e.g: [[0,1], [0,2],[1,2]]

# so here we will need two array one dfs_visited to check if the adjacent node of curr node is 
# visited in current DFS call or not.
# if visited in curr DFS call then it contain a cycle otherwise not

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.dfs_visited= [False]*n   # will check whether that node has been visited in current cycle or not
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

# you can start with any node, in dfs it doesn't matter in printing topological sort or detecting cycle
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


# another way using dfs: this submitted in Q "269 Alien dictionary"
# understand the logic properly and do here 


# method 2: using BFS(kahn's Algorithm)
# this is under topological sort (Method 2)


# Dfs template to use in other Q
# Just code of: 207. Course Schedule
from collections import defaultdict
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        # According to the meaning of the Q.
        for second,first in prerequisites:
            AdjList[first].append(second)

        def checkCycle(src):
            visited.add(src)
            path_visited.add(src)
            for u in AdjList[src]:
                if u not in visited:
                    if checkCycle(u):
                        return True
                elif u in path_visited:
                    return True
            path_visited.remove(src)
            return False

        visited= set()
        path_visited= set()
        for i in range(numCourses):
            if i not in visited and checkCycle(i):    # if cycle simply return False, else continue checking for another node
                return False
        return True