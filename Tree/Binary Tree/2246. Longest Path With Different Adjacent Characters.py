# Brute force
# Just check maximum possible length from each node.

# Note: Here making adjacency list like undirected graph.

# Time : O(n^2)

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = collections.defaultdict(list)
        for i , par in enumerate(parent):
            if i == 0:
                continue
            adj[par].append(i)
            adj[i].append(par)

        def dfs(node):
            visited.add(node)
            # Take max of all its adjacent node and add '1'.
            ans = 1
            for nei in adj[node]:
                if nei not in visited and s[node] != s[nei]:
                    ans = max(ans, 1 + dfs(nei))
            return ans

        n = len(parent)
        visited = set()
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
            # print(res, i, "res")
            visited.clear()
        return res


# Optimising to O(n)

# Just an extension of "543. Diameter of Binary Tree".
# Only differnce one node can have more than 2 children.

# Logic: In a generic tree there are more than 2 nodes however 
# the longest path can only be found from 2 of the longest nodes for each node.

# So for each node, keep track of 2 longest path going through that node 
# then ans for that node = best + second_best + 1.

# Implementation is similar to ""543. Diameter of Binary Tree".

# Note: Here we are making directed graph and after finding ans for children , forwarding that to parent & so on.

# Time = O(n)

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = collections.defaultdict(list)
        for i , par in enumerate(parent):
            if i == 0:
                continue
            adj[par].append(i)
            # adj[i].append(par)
        
        self.ans = 1

        # dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
        def dfs(node):
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node 
            # in the sub-tree rooted at this node.
            best , second_best = 0, 0   # these will come from all possible children
            for nei in adj[node]:
                length = dfs(nei)
                if s[node] != s[nei]:
                    # length = dfs(nei)  # writing here will wrong ans because if characters are same 
                    # then, function call will never happen for 'nei' node but we can get the maximum ans starting from 'nei' node also.
                    # update best and second_best
                    if length > best:
                        second_best = best
                        best = length
                    elif length > second_best:
                        second_best = length
            
            # Update ans
            # best + second_best + 1 means the length of the longest valid path 
            # going through this node in the sub-tree rooted at this node.
            self.ans = max(self.ans, best + second_best + 1)  # '1' for cur node
            # But it will return only one length i.e maximum possible one. Parent can only take one of the path so take best one
            return best + 1

        dfs(0)
        return self.ans
        