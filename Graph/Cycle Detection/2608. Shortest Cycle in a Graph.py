# just same way we find the cycle in undirected graph.
# only diiff here is when we will detect the cycle we will update the no of nodes also at that time.
# node in cycle= distance[node] + distance[nei] + 1 ('1' for edge between node-->nei). 
# note: Do dry run on paper for visualisation.

# note: for counting the nodes(length), we are taking an array 'distance'.

# why we are checking from each node one by one?
# Ans: Because here same node can be part of more than one cycle.(diff from  "2360. Longest Cycle in a Graph").
# so we can't get ans like Q: "2360. Longest Cycle in a Graph". 
# e.g: [[0,1],[1,2],[2,3],[1,3]]

# Note: we will only get exact no of nodes in a cycle either minimum or max when that node will be part of any cycle.
# best: when we will check if any cycle start from this node.
# so for every vertex, we check if it is possible to get the shortest cycle involving this vertex(more concise: starting from this vertex).

# Time Complexity: O( |V| * (|V|+|E|))
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        adj= collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans= float('inf')

        for v in range(n):
            distance= [float('inf')]*n   # will store the shortest distnce of a node from vertex 'v'.
            parent= [-1] * n  # will store the parent of each node
            q= collections.deque([])  
            q.append(v)# [(node)]
            distance[v]= 0
            while q:
                node= q.popleft()
                for nei in adj[node]:
                    # if nei is not visited i.e distance[nei]== 'inf', update the distance of nei and add into the Q
                    if distance[nei]== float('inf'):
                        distance[nei]= distance[node] + 1
                        q.append(nei)
                        parent[nei]= node
                    # if nei is visited i.e distance[nei]!= 'inf' then check if it forming a cycle.
                    elif parent[node]!= nei : # forming a cycle so return the length of the cycle.
                        ans= min(ans, distance[nei] + distance[node] + 1)  # we may get even smaller ans form 'v'
        
        return ans if ans!= float('inf') else -1
    

# my mistake.
# i was simply returning after seeing any cycle.
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        def bfs(v):
            distance= [float('inf')]*n   # will store the shortest distnce of a node from vertex 'v'.
            q= collections.deque([])  
            q.append((v, -1))# [(node, parent)]
            distance[v]= 0
            while q:
                node, parent= q.popleft()
                for nei in adj[node]:
                    # if nei is not visited i.e distance[nei]== 'inf', update the distance of nei and add into the Q
                    if distance[nei]== float('inf'):
                        distance[nei]= distance[node] + 1
                        q.append((nei, node))
                    # if nei is visited i.e distance[nei]!= 'inf' then check if it forming a cycle.
                    elif nei != parent: # forming a cycle so return the lengthof the cycle.
                        return distance[nei] + distance[node] + 1
            return float('inf')

        adj= collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        ans= float('inf')
        for node in range(n):
            ans= min(ans, bfs(node))
        return ans if ans!= float('inf') else -1