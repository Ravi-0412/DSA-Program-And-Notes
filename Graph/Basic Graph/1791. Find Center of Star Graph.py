# Method 1:
# center node must have maximum indegree value.\
# time = space = O(n)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        indegree = [0] * n
        for u, v in edges:
            indegree[u - 1] += 1
            indegree[v - 1] += 1
        return indegree.index(max(indegree)) + 1  # return node having max indegree value


# method 2:
# Logic: A center node must appear in every edge.

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]