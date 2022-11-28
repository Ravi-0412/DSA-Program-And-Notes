# just the topological sorting
# how to reach think about topo sort?: we can only finish all the courses if there exist any order for completing all the courses
# and order is only possible when we will make a directed graph between the dependency given and graph should have no cycle.
# # and for finding any ordering checking with checking cycle , only thing comes into mind is 'Topological Sort'  
# if no cycle then it is possible 

# method1: using Bfs
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:  # graph arrow will be from first to second
            AdjList[first].append(second)
        
        count,Q,ans,n= 0, [], [], numCourses
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1
        
        
        # now applying the BFS to get the topological order
        # find the node with indegree '0' as this node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)
    
        while Q:
            count+= 1  
            u= Q.pop(0)
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j]-= 1
                if indegree[j]== 0:  # after decreasing if any node has indegree == 0 then put in the Q
                    Q.append(j)

        if count!= n:  # for checking the cycle in directed graph using BFS. count will always less than 'n' in case of cycle
            return False
        return True
        


# # method 2: Dfs (already done in topological sorting)
# # very better solution: used only one array 
# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         AdjList= defaultdict(list)
#         # first convert into adjacency list(edges) for directed graph
#         for second,first in prerequisites:
#             AdjList[first].append(second)
#         visited= [0]*numCourses
#         stack= []
#         for i in range(numCourses):
#             if not self.FindTopoSort(AdjList,i,stack,visited):    # if cycle simply return [], else continue checking for another node
#                 return []
#         return stack[::-1]
        

# false: means cycle 
#     def FindTopoSort(self, adj,src, stack,visited):
#         # base case for checking whether we have visited all the adjacent node.. if visited then check on another node
#         if visited[src]== 1:   # been visited and added to the stack(ans). so simply return true so that it can check for next node without repeating the work
#             return True
#         # base case for checking cycle 
#         if visited[src]== -1:   # means cycle as the current node(src) is already visited in current cycle only
#             return False

#         # code starts from here
#         visited[src]= -1   # means till now we have only visited the 'src' not its adjacent node
#         for u in adj[src]:
#             if not self.FindTopoSort(adj, u, stack, visited):
#                 return False
                
#         # while traversing back make visited[src]= 1 and  put the node into the stack
#         visited[src]= 1   # means we have visited the 'src' as well as its neighbour and added to the ans(stack)
#         stack.append(src)
#         return True   # means we have visited the current node as well as its neighbour successfully
