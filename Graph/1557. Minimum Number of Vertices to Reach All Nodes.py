# logic: Nodes having indegree '0' won't be reachable by any other nodes,
# And other nodes having indegree > 0 will be reachable by nodes having indegree = 0.

# so Q reduces to: "Find the nodes having indegree= 0".

# time: O(n + E)

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree= [0]*n
        for u, v in edges:
            indegree[v]+= 1
        ans= []
        for i in range(n):
            if indegree[i]== 0:
                ans.append(i)
        return ans
    

# Note: Think if graph is cyclic?