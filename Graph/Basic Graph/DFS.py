from collections import defaultdict
from time import time
class Graph:
    def __init__(self,n):
        self.V= n
        self.colors= ['white']*n
        self.pred= [-1]*n
        self.time= 0
        self.first_time_visited= [0]*n
        self.last_time_visited= [0]*n
        self.graph= defaultdict(list)
    
    # for directed graph
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFS(self):
        print("Dfs traversal is: ")
        for u in range(self.V):
            if self.colors[u]== 'white':
                self.DFS_Visit(u)
        print()
        print("first time visit of nodes",self.first_time_visited)
        print("last time visit of nodes ",self.last_time_visited)
    
    def DFS_Visit(self,u):
        self.time+= 1
        self.first_time_visited[u]= self.time
        self.colors[u]= 'gray'
        print(u, end=" ")
        for v in self.graph[u]:
            if self.colors[v]== 'white':
                self.pred[v]= u
                self.DFS_Visit(v)
        self.time+= 1
        self.last_time_visited[u]= self.time
        self.colors[u]= 'black'

g= Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(5,5)
print(g.graph)
g.DFS()
