# Method 1: Find the ans for each node.

# Will give TLE in the case of [[0,1],[0,2],[0,3]....[0,n-1]],
# each edge will be picked in each call of dfs, it will become O(n^2) in total.

# graph[i][j]: cost of going from 'i' to 'j'.

# Note: 1) making adjacency matrix of (n*n) will go in infinite loop.
# So used dictioanry to store only node having edge between them.
# or make adjacency matrix like this: graph = [[] for _ in range(n)]
# 2) When the last node (having degree = 1) will get visited then 'dfs' will start to return back.

# Time : O(n^2)

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(dict)  # storing adj nodes in dict only to get default value= 0
        for u, v in edges:
            graph[u][v] = 0  # no extra cost is required to go from 'i' to 'j'.
            graph[v][u] = 1  # we need to reverse this edge to go from 'v' to 'u'.
        
        # print(graph)

        def dfs(cur , par):
            cost = 0
            for k in graph[cur]:
                if k != par:
                    # print(k, cur,  "node")
                    cost += graph[cur][k] + dfs(k , cur)
            return cost

        
        ans = []
        # finding the nodes to reverse for each node
        for i in range(n):
            # print("new node")
            cost = dfs(i , -1)   # [curNode , parent]
            ans.append(cost)
        return ans


# Method 2: optimising the above one
# find the ans for any node. O(n)

# After that find the ans for remaining node taking help of calculated one.
# How?
# Assume we know the answer for node u and consider v, a neighbour of u.
# The answer for v is going to be either answer[u] + 1 or answer[u] - 1.

# Time: O(n)

class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(dict)  # storing adj nodes in dict only to get default value= 0
        
        for u, v in edges:
            graph[u][v] = 0  # no extra cost is required to go from 'i' to 'j'.
            graph[v][u] = 1  # we need to reverse this edge to go from 'v' to 'u'.
        
        # print(graph)

        def dfs(cur , par):
            cost = 0
            for nei in graph[cur]:
                if nei != par:
                    # print(k, cur,  "node")
                    cost += graph[cur][nei] + dfs(nei , cur)
            return cost

        def dfs2(cur, cost):
            ans[cur] = cost
            for nei in graph[cur]:
                if ans[nei] < 0:
                    # if nei ans is not calculated yet
                    # doing '-' because while making graph we have already added the cost.
                    # so if we don't '-' then it will get added two times and 
                    # '+' : if nei is reachable from cur then it will add '0' else '1'.
                    dfs2(nei, cost - graph[cur][nei]  + graph[nei][cur])

        ans = [-1] * n
        # find the ans for any one node
        cost = dfs(0 , -1)   # [curNode , parent]
        # then again call dfs to find the ans of all.
        dfs2(0, cost)

        return ans


# Method 3:
# Other way of writing the above code.
# Easier one .
class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)] 
        reversed_graph = [[] for _ in range(n)]  # for checking the reverse pair
        for u, v in edges:
            graph[u].append(v)
            reversed_graph[v].append(u)
        
        def dfs(cur, par):
            cnt = 0
            for nei in graph[cur]:
                if nei != par:
                    cnt += dfs(nei, cur)
            for nei in reversed_graph[cur]:
                if nei != par:
                    cnt += 1   # we will have to reverse the edge to visit 'nei' from cur.
                    cnt += dfs(nei, cur)
            return cnt
        
        answer = [0] * n
        answer[0] = dfs(0, -1)
        
        def dfs2(cur, par, cnt):
            answer[cur] = cnt
            for nei in graph[cur]:
                if nei != par:
                    # for visiting 'cur' from 'nei' we have to reverse the edge
                    # so for nei count will increase by '1'.
                    dfs2(nei, cur, cnt + 1)
            for nei in reversed_graph[cur]:
                if nei != par:
                    # for visiting 'cur' from 'nei' , we don't need to reverse any edge.
                    # so for nei count will decrease by '1'.
                    dfs2(nei, cur, cnt - 1)
                
        dfs2(0, -1, answer[0])
        return answer
