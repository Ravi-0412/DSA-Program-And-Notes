# method 1: using DFS
#logic:  just run the DFS and when there is no adjacent node put the node into the stack
# At last print the stack in opposite direction

# why came with DFS? 
# Ans: as DFS go deeper and deeper and we need to print the node with lesser outorder vertices first
# means stop at node with no adjacent node(no outgoing vertices as DAG will must contain at least one vertex with outgoing edge = 0 and incoming edge =0)
#  and we have to print the vertex with no outgoing edge at last and that can be done 
# while traversing back in case of DFS


# from collections import defaultdict
# class Graph:
#     def __init__(self,n):
#         self.V= n
#         self.visited= [False]*n
#         self.AdjList= defaultdict(list)
    
#     def addEdge(self,u,v):
#         self.AdjList[u].append(v)

#     def FindTopoSort(self, adj,src, stack):
#         self.visited[src]= True
#         for u in adj[src]:
#             if not self.visited[u]:
#                 self.FindTopoSort(adj, u, stack)  
#         # while traversing back put the node into the stack and node with less no of outorder vertices 
#         # will be kept first(as it will start traversing at this node only) so final ans will be the opposite of stack
#         stack.append(src)

#     def TopoSort(self,n, adj):
#         stack= []
#         for i in range(n):
#             if not self.visited[i]:
#                 self.FindTopoSort(adj,i,stack)

#         while stack:
#             print(stack.pop(), end=" ")

# g= Graph(6)
# g.addEdge(5,2)
# g.addEdge(5,0)
# g.addEdge(2,3)
# g.addEdge(3,1)
# g.addEdge(4,0)
# g.addEdge(4,1)
# print(g.AdjList)
# g.TopoSort(6,g.AdjList)



# method 2 using BFS: Kahn's Algorithm
# logic: use the concept of indegree as the node with indegree 0 will come at first and
# node with more indegree will come later and so

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        # self.visited= [False]*n  # here no need of this as we are pushing on ele in stack and doing the operation on that
        self.indegree= [0]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
    
    # calculate the indegree of all node
    def Indegree_count(self):
        for i in range(self.V):
            for k in self.AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                self.indegree[k]+= 1
        print(self.indegree)

    def FindTopoSort(self):
        Q, ans= [], []
        for i in range(self.V):
            if self.indegree[i]==0: 
                Q.append(i)

        count= 0  # will count the no of times node is added in the ans
        while Q:
            count+= 1  
            u= Q.pop(0)
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in self.AdjList[u]:
                self.indegree[j]-= 1
                if self.indegree[j]== 0:  # after decreasing if any node has indegree == 0 then put in the Q
                    Q.append(j)

        if count!= self.V:
            print("there exist a cycle in the graph")
        else:
            print(ans)
        

g= Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(4,0)
g.addEdge(4,1)
g.Indegree_count()
g.FindTopoSort()


