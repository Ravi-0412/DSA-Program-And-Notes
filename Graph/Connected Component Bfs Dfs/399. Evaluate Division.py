# logic: just simple bfs to find the cost from src to destination.
# Difficult part to think how we can do by graph.

# expalanation:
# Given:
# a/b = 2.0, b/c = 3.0
# We can build a directed graph:
# a --> 2.0 --> b -- 3.0 --> c
# If we were asked to find a/c, we have:
# a/c = a/b * b/c = 2.0 * 3.0
# In the graph, it is the product of costs of edges.

# Do notice that, 2 edges need to added into the graph with one given equation,
# because with a/b we also get result of b/a, which is the reciprocal of a/b.
# in short using reciprocal we can also get ans .

# e.g: If asked to find 'c/a' then reciprocal will only help.
# c -- 0.333 --> b -- 0.5 --> a

# how to do?
# FOr each query [a, b], run a bfs starting from 'a' and keep multiplying the edges that is adjacent 
# And once you reach 'b', return ans. (a and b can be equal also)

# time: n * (E+ V), n= len(queries)

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj= collections.defaultdict(list)
        # form adjacency list (directed graph with values for that eqn)
        for i, eq in enumerate(equations):
            a, b= eq
            adj[a].append((b, values[i]))  # 'a/b' = values[i]
            adj[b].append((a, 1 / values[i]))  # for reverse value will also reverse. 'b/a' = 1/values[i]
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q= collections.deque()
            visited= set()   # we are adding reverse also so there will be cycle . so take visited.
            q.append((src, 1))   # [variable, values_till_now]
            visited.add(src)
            while q:
                a, w= q.popleft()
                if a== target:
                    return w
                for nei, weight in adj[a]:
                    if nei not in visited:
                        q.append((nei, w *weight))
                        visited.add(nei)
            # Both src and destination is present but there is no way we can find src/target.
            return -1
        
        ans= []
        for q in queries:
            curAns= bfs(q[0], q[1])
            ans.append(curAns)
        return ans


# Later do by dfs
