# method 1: find the distance of each node from target and if it equal to k then add that node into the ans
# very much complicated and lengthy. Can't even think of solving this way in dreams
# time: O(n^2)


# method 2: very logical and easy
# since we have to find the nodes at distance "k" and 
# the nodes can be above the target node and may be in different subtree of target node.
# so there is no way we can reach the these nodes from target as we can't traverse in upward direction

# Note vvi: one thing always remember if told to find anything at some given distance or 
# shortest path always think of BFS.
# so somehow  if we can convert the three into graph and make a adjacency list between parent to children
# then we can easily apply multisource bfs (even single source also fine) to get the all the nodes at distance 'K'.

class Solution:
    def distanceK(self, root, target, K):
        # first make a graph. here making undirected graph. Directed graph will also work no problem
        graph= collections.defaultdict(list)
        self.MakeGraph(root, graph)
        visited= set()
        ans= []
        ans= self.BFS(graph, target, K, visited)  # did like this to handle the corner cases like when there is no node at given distance
        if ans== None:  # no answer exist
            return []
        return ans
    
    def MakeGraph(self,root,graph):   # using dfs to make the graph 
        if root.left:  # add edge between root to left child and left child to root
            graph[root.val].append(root.left.val)    # making node with node val to return the ans(Q) directly otherwise we will get ans as node(will conatin all connected nodes)
            graph[root.left.val].append(root.val)
            self.MakeGraph(root.left, graph)
        if root.right:  # add edge between root to left child and left child to root
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
            self.MakeGraph(root.right, graph)
            
    def BFS(self, graph, target, K, visited):     # multisource bfs 
        distance= 0
        # q= collections.deque()  # not working don't know why
        q= [target.val]     # added the target 
        # q will contain the all the nodes level wise
        visited.add(target.val)
        while q:
            if distance== K:    # then simply return q that will your ans if exist
                return q  
            for i in range(len(q)):
                curr= q.pop(0)
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            distance+= 1



# Method 2: Using dfs
# we only need to cover the nodes till distance 'k'.
# for this we will use distance 'd' also as one of the parameter.
# if 'd' < k then we need to cover the adjacent nodes to cur node 
# And if = k then we got one of the ans (No need to call function in this).

import collections
class Solution:
    def distanceK(self, root, target, K):
        adj, res, visited = collections.defaultdict(list), [], set()
        def dfs(node):
            if node.left:
                adj[node].append(node.left)
                adj[node.left].append(node)
                dfs(node.left)
            if node.right:
                adj[node].append(node.right)
                adj[node.right].append(node)
                dfs(node.right)

        # to make the graph
        dfs(root)

        # Again run dfs to find the ans
        def dfs2(node, d):
            if d < K:
                visited.add(node)
                for v in adj[node]:
                    if v not in visited:
                        dfs2(v, d + 1)
            else:
                res.append(node.val)
        dfs2(target, 0)
        return res


# Related q: 
# 1) 2385. Amount of Time for Binary Tree to Be Infected