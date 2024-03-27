# can detect cycle even graph is given as component
# method 1 : using BFS
# time complexity is same as BFS

# # logic: if adjacent node of any vertex is already visited and if it is not parent then there is a cycle .
#  because if that is not parent and already visited then there must be another path also for reaching that adjacent node from curr node and 
# since undirected graph is two way(btwn two node) so it will be a cycle only.

# this method can also be used to detect the no of connected components in the undirected graph
# just count the no of times BFS is called that will be the ans


from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
        self.AdjList[v].append(u)
    
    def BFS(self, adj, src):
        Q= deque()
        # while adding vertex to Q, add its parent node also
        Q.append((src, -1))
        while Q:
            (curr, parent)= Q.popleft()
            # print(curr, parent)
            for u in self.AdjList[curr]:
                if self.visited[u]== False:
                    self.visited[u]= True
                    Q.append((u,curr))
                elif u!= parent:  # u is visited as well as not parent means cycle so return true
                    return True
        # return False   # no need of this line

    def isCycle(self,n, adj):
        for i in range(n):
            if self.visited[i]== False:
                self.visited[i]= True  
                if self.BFS(adj,i):
                    return True
        # if no component has cycle then return False     
        return False   

    
g= Graph(11)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(4,9)
g.addEdge(4,5)
g.addEdge(5,6)
# g.addEdge(5,8)
g.addEdge(9,8)
g.addEdge(8,7)
g.addEdge(6,7)
g.addEdge(7,10)
print(g.AdjList)
print(g.isCycle(11,g.AdjList))
print(g.visited)



# # method 2: using DFS
# # logic is exactly same as BFS
# from collections import defaultdict
# class Graph:
#     def __init__(self,n):
#         self.V= n
#         self.visited= [False]*n
#         self.AdjList= defaultdict(list)
    
#     def addEdge(self,u,v):
#         self.AdjList[u].append(v)
#         self.AdjList[v].append(u)

#     def DFS_Visit(self, adj,src,parent):
#         self.visited[src]= True
#         for u in adj[src]:
#             if not self.visited[u]:
#                 if self.DFS_Visit(adj, u, src):
#                     return True
#             elif u != parent:
#                 return True

# you can start with any node, in dfs it doesn't matter in printing topological sort or detecting cycle
#     def isCycle(self,n, adj):
#         for i in range(n):
#             if not self.visited[i]:    
#                 if self.DFS_Visit(adj,i, -1):
#                     return True       
#         return False


# g= Graph(11)
# g.addEdge(0,1)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(4,9)
# g.addEdge(4,5)
# g.addEdge(5,6)
# # g.addEdge(5,8)
# g.addEdge(9,8)
# g.addEdge(8,7)
# # g.addEdge(6,7)
# g.addEdge(7,10)
# # print(g.AdjList)
# print(g.isCycle(11,g.AdjList))
