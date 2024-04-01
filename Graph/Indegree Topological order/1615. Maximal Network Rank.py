# Just we need to find the indegree of all the nodes then, 
# network rank(a, b) = indegree[a] + indegree[b] if (a,b) is not conected and
# network rank(a, b) = indegree[a] + indegree[b] - 1, if (a,b) is connected

# And our ans will be max of any network rank.

#storing the edges in set to check if there is edge between any two node in O(1)
# Or you can use 2d matrix(adjacency matrix) and if any edge make value = 1

# Time: O(n^2)

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] *n
        roadsEgdes = set()  
        for a, b in roads:
            indegree[a] += 1
            indegree[b] += 1
            roadsEgdes.add((a, b))   # no need to add other pair (b, a) since bidirectional
            
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in roadsEgdes:
                    ans = max(ans, indegree[i] + indegree[j] -1)
                else:
                    ans = max(ans, indegree[i] + indegree[j])
        return ans