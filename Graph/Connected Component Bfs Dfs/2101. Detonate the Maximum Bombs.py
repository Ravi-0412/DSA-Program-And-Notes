# Method 1: 

"""
Just same as:"695. Max Area of Island". Just we have to think and reduce into this q.
Intitution: Just we have to find the "max no of node in connected comopnents".

How we will connect ?
if detonating bomb 'i' will detonate the bomb 'j' then we will add 'j' in adj list of 'i'.
Note: it may happen that 'i' detonate 'j' but 'j' won't detonate 'i'.

VVi: How we will find the detonating bombs?
say we have to find whether detonating 'i' will detonate 'j' or not?
if distance between their location is <= radius of 'i' then 'i' will detonate 'j'.

Time Complexity: O(N^3) 
Phase 1 (Building graph) takes O(N^2). 
Phase 2 runs a BFS (O(V+E)) for each of the N bombs. Since E can be up to N^2, we get N * (N + N^2) ~ O(N^3).
Space Complexity : O(N^2), The adjacency list stores all possible detonation connections. In a worst-case scenario where every bomb triggers every other bomb, we store N^2 edges.
"""

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # make adjacency list i.e connect bomb which can detonate each other
        adj= collections.defaultdict(list)  # [node: bombs that will get detonate after detonating 'node']
        n= len(bombs)
        for i in range(n):
            x1, y1, r1= bombs[i]
            for j in range(n):
                if i== j:
                    continue
                x2, y2, r2= bombs[j]
                # check if denotating 'i' can denotate 'j'.
                x_diff, y_diff= abs(x1 - x2), abs(y1 - y2)
                # if distance between their location is <= radius of 'i' then 'i' will detonate 'j'.
                if x_diff * x_diff + y_diff * y_diff <= r1*r1:
                    adj[i].append(j)

        def dfs(node, visited):
            count = 1
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                   count += dfs(nei, visited)
            return count

        # now just find the maximum no of nodes in a connected components
        ans= 1
        for i in range(n):
            visited= set()
            ans= max(ans, dfs(i, visited))
        return ans


# Method 2:
# Using BFS

import collections
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = collections.defaultdict(list)
        
        # Step 1: Build the Adjacency List - O(N^2)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j: continue
                x2, y2, r2 = bombs[j]
                
                # Euclidean distance squared: (x1-x2)^2 + (y1-y2)^2
                # We compare it to r1^2 to avoid expensive square root operations
                dist_sq = (x1 - x2)**2 + (y1 - y2)**2
                if dist_sq <= r1**2:
                    adj[i].append(j)
        
        # Step 2: BFS Helper Function
        def bfs(start_node):
            queue = collections.deque([start_node])
            visited = {start_node}
            
            while queue:
                node = queue.popleft()
                
                for neighbor in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return len(visited)
            
        return max(bfs(i) for i in range(n))

# my mistake
# 1) I was taking 'visited' as global but it won't work.
# because: it may happen that 'i' detonate 'j' but 'j' won't detonate 'i'.

# 2) was finding the count in wrong way.
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # make adjacency list i.e connect bomb which can detonate each other
        adj= collections.defaultdict(list)  # [node: bombs that will get detonate after detonating 'node']
        n= len(bombs)
        for i in range(n):
            x1, y1, r1= bombs[i]
            for j in range(n):
                if i== j:
                    continue
                x2, y2, r2= bombs[j]
                # check if denotating 'i' can denotate 'j'.
                x_diff, y_diff= abs(x1 - x2), abs(y1 - y2)
                if x_diff * x_diff + y_diff * y_diff <= r1*r1:
                    adj[i].append(j)

        def dfs(node):
            count= 1
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                   count = 1 +  dfs(nei, visited)
                #   count += dfs(nei)
            return count

        # now just find the maximum no of nodes in a connected components
        visited= set()   
        ans= 1
        for i in range(n):
            if i not in visited:
                ans= max(ans, dfs(i))
        return ans


# Similar Question asked in Google
"""
Q) In a 2D space, you are given N routers each having the same radius of R. The routers are initially in the OFF status. 
You select 1 router, it turns on and pings all the routers that are within its radius. You need to find the minimum time at which all the routers will turn ON.
"""
import collections
from typing import List

class Solution:
    def minTimeToTurnOnAll(self, routers: List[List[int]], R: int) -> int:
        n = len(routers)
        if n == 0: return 0
        adj = collections.defaultdict(list)
        
        # 1. POPULATE UNDIRECTED ADJ LIST: O(N^2) but half the checks
        for i in range(n):
            x1, y1 = routers[i][0], routers[i][1]
            for j in range(i + 1, n): # Only check pairs once
                x2, y2 = routers[j][0], routers[j][1]
                
                dist_sq = (x1 - x2)**2 + (y1 - y2)**2
                if dist_sq <= R**2:
                    adj[i].append(j)
                    adj[j].append(i) # Symmetric connection

        # 2. BFS HELPER: Level-by-level
        def get_max_distance(start_node):
            queue = collections.deque([start_node])
            visited = {start_node}
            time = 0
            
            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    curr = queue.popleft()
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                if queue:
                    time += 1
            
            # Returns max distance and whether it reached everyone
            return time, len(visited) == n

        # 3. INITIAL CONNECTIVITY CHECK
        # If the first node can't reach everyone, no one can (in undirected graph)
        first_time, reaches_all = get_max_distance(0)
        if not reaches_all:
            return -1
        
        # 4. FIND MINIMUM ECCENTRICITY
        # We already have the result for node 0, so start min with first_time, because radius is same
        min_max_time = first_time
        for i in range(1, n):
            time, _ = get_max_distance(i)
            min_max_time = min(min_max_time, time)
            
        return min_max_time

# follow ups
"""
Q)  each router having its own radius and asked me to do minimal change to incorporate the change ?
"""
import collections
from typing import List

class Solution:
    def minTimeToTurnOnAll(self, routers: List[List[int]]) -> int:
        n = len(routers)
        # 1. Initialize the adjacency list
        # Key: Router index, Value: List of routers it can reach
        adj = collections.defaultdict(list)
        
        # 2. Populate the adj list based on unique radii: O(N^2)
        for i in range(n):
            x1, y1, r1 = routers[i] # Source router 'i' and its radius
            for j in range(n):
                if i == j: continue
                x2, y2, _ = routers[j] # Target router 'j'
                
                # Calculate squared Euclidean distance
                dist_sq = (x1 - x2)**2 + (y1 - y2)**2
                
                # Logic: If source 'i' can reach 'j', add a DIRECTED edge
                if dist_sq <= r1**2:
                    adj[i].append(j)

        # 3. Your BFS function logic
        def get_max_distance(start_node):
            queue = collections.deque([start_node])
            visited = {start_node}
            time = 0
            
            while queue:
                level_size = len(queue)
                # Level-by-level processing
                for _ in range(level_size):
                    curr = queue.popleft()
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                
                # Only increment time if there's another "wave" of pings coming
                if queue:
                    time += 1
            
            return time if len(visited) == n else float('inf')

        # 4. Try starting from every router to find the minimum time
        ans = min(get_max_distance(i) for i in range(n))
        
        return ans if ans != float('inf') else -1
