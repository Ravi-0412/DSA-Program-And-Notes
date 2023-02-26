# just convert into graph and apply bfs. same as rotten oranges.

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph= collections.defaultdict(list)
        self.MakeGraph(root, graph)
        visited= set()
        return self.BFS(graph, start, visited)  # did like this to handle the corner cases like when there is no node at given distance
    
    def MakeGraph(self,root,graph):   # using dfs to make the graph 
        if root.left:  # add edge between root to left child and left child to root
            graph[root.val].append(root.left.val)    # making node with node val to return the ans(Q) directly otherwise we will get ans as node(will conatin all connected nodes)
            graph[root.left.val].append(root.val)
            self.MakeGraph(root.left, graph)
        if root.right:  # add edge between root to left child and left child to root
            graph[root.val].append(root.right.val)
            graph[root.right.val].append(root.val)
            self.MakeGraph(root.right, graph)
            
    def BFS(self, graph, start, visited):     # multisource bfs 
        time= 0
        q= collections.deque([start]) 
        visited.add(start)
        while q:
            for i in range(len(q)):
                curr= q.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            time+= 1
        return time -1
