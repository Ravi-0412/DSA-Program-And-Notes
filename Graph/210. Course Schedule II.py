# just print the order of topological sort
# method 1: By  Bfs

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:
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

        if count!= n:  # means cycle so no order is possible 
            return []
        return ans


# method 2: Dfs (already done in topological sorting)