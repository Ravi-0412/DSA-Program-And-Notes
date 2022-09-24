# method 1: using BFS

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        color= [-1]*n
        for i in range(n):
            if color[i]== -1:
                if self.BfsCheck(graph,i,color)== False:
                    return False
        return True
    
    def BfsCheck(self, graph,src,color):
        Q= [src]
        color[src]= 1
        while Q:
            curr= Q.pop(0)
            for nei in graph[curr]:
                if color[nei]== -1:
                    color[nei]= 1^color[curr]  # just change the color of its adjacent node, 
                    # for this we used xor operation with 1(to get the diff one , xor with 0 will result into the same color)
                    Q.append(nei)
                elif color[nei]== color[curr]:
                    return False
        return True



# method 2: By using DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        color= [-1]*n
        for v in range(n):
            if color[v]== -1:
                color[v]= 1
                if  self.DfsCheck(graph,v,color)== False:
                    return False
        return True

    def DfsCheck(self, graph, src, color):
        for u in graph[src]:
            if color[u]== -1:
                color[u]= 1^color[src]
                if self.DfsCheck(graph,u,color)== False:
                    return False
            elif color[u]== color[src]:
                return False
        return True



# don't know wjy this giving incorrect result by using two array visited and color
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        visited= [False]*n
        color= [-1]*n
        for v in range(n):
            if not visited[v]:
                print(v)
                color[v]= 0
                visited[v]= True
                if self.DFSVisit(graph,v, visited, color)== False:
                    return False
        return True
    
    def DFSVisit(self, graph, src, visited, color):
        for u in graph[src]:
            if not visited[u]:
                visited[u]= True
                color[u]= 0^color[src]  # here i was making mistake , xor with 0 will give the same no i.e same color so was getting false for all inputs
                if self.DFSVisit(graph,u,visited, color)== False:
                    return False
            elif color[u]== color[src]:
                return False
        return True

