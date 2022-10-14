# method 1: using DFS
#logic:  just run the DFS and when there is no adjacent node put the node into the stack
# At last print the stack in opposite direction

# why came with DFS? 
# Ans: as DFS go deeper and deeper and we need to print the node with lesser outorder vertices first
# means stop at node with no adjacent node(no outgoing vertices as DAG will must contain at least one vertex with outgoing edge = 0 and incoming edge =0)

# i.e we have to print the vertex with no outgoing edge at last and that can be done 
# while traversing back in case of DFS

# Note(VVI) for dfs method: here you are putting the node in the ans(stack), while traversing back that's why it's giving correct ans always
# but if we put the node at start itself in the ans like when you are calling the dfs for that node then it will not give the corect ans always...keep this in mind
# if you do like this graph like test case 2 will not work

# if you do by finding the indegree like BFS then that will always give the correct ans as that is the basic of tolopogical sort

# Note: this method will only work if no cycle.. for cycle detecting and then printing see the below method that i submitted in Q "210. Course Schedule II"
# or we can also modify in this like we can use two visited array like we did in cycle detection Q

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
#         # will be kept first(as it will start traversing back at this node only) so final ans will be the opposite of stack

         # node with largest visiting time(or minimum finishing time) is pushed first when there is no further adjacent node is there which has not been visited
#         stack.append(src)

# you can start with any node, in dfs it doesn't matter in printing topological sort or detecting cycle
#     def TopoSort(self,n, adj):
#         stack= []
#         for i in range(n):
#             if not self.visited[i]:
#                 self.FindTopoSort(adj,i,stack)
#         while stack:  
#             print(stack.pop(), end=" ")

# test case 1:
# g= Graph(6)
# g.addEdge(5,2)
# g.addEdge(5,0)
# g.addEdge(2,3)
# g.addEdge(3,1)
# g.addEdge(4,0)
# g.addEdge(4,1)
# print(g.AdjList)
# g.TopoSort(6,g.AdjList)

# test case 2:
# g= Graph(3)
# g.addEdge(0,2)
# g.addEdge(0,1)
# g.addEdge(1,2)


# another way using dfs: this submitted in Q "269 Alien dictionary"


# method 2 using BFS: Kahn's Algorithm
# logic: use the concept of indegree as the node with indegree 0 will come at first and
# node with more indegree will come later and so

# This method can also be used to detect cycle in directed graph
# just count the no of nodes added in the Q, if there will be cycle then count <n because  at some point 
# there will not be any node whose indegree will be equal to '0' to put into the Q or call the bfs function
# here no need of visited set since we are adding only the node with 'indegree==0'

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        # self.visited= [False]*n  # here no need of this as we are pushing on ele in Q and doing the operation on that
        self.indegree= [0]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
    
    # calculate the indegree of all node
    def Indegree_count(self):
        for i in range(self.V):
            for k in self.AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                self.indegree[k]+= 1

    def FindTopoSort(self):
        Q, ans= [], []
        # find the node with indegree '0' as this node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS
        for i in range(self.V):   # for more than one component, make a separate function for bfs and call bfs inside the for loop like always
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

        if count!= self.V:  # for checking the cycle in directed graph using BFS
            print("there exist a cycle in the graph")
        else:
            print(ans)
        
# test case 1
# g= Graph(6)
# g.addEdge(5,2)
# g.addEdge(5,0)
# g.addEdge(2,3)
# g.addEdge(3,1)
# g.addEdge(4,0)
# g.addEdge(4,1)

# test case 2
# g= Graph(3)
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(2,0)
# g.Indegree_count()
# g.FindTopoSort()

# test case 3
g= Graph(3)
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(1,2)
print(g.AdjList)
g.Indegree_count()
g.FindTopoSort()








