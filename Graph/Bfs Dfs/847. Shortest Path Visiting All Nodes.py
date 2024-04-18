# Why normal bfs won't work?
# If we apply simple bfs starting from any node(say 0) where we also keep track of visited array 
# (Consecutively meaning we can't visit them again) it will never lead us to the solution.
# On the other hand if we apply bfs from any node (say 0) and don't keep the track of visited array, 
# it will lead to cycle [ {0}->{0,1}->{0,1,0}->{0,1,0,1} and so on]

# How to proceed then?

# Logic: 1) we don't know starting from which node will lead to ans.
# 2) We can also visit same node but should be through different path i.e other set of visited nodes
# Otherwise will go in infinite loop.

# For handling these two we must put all nodes in 'queue' with 'set of visited_nodes_in_cur_path with steps' & 'steps'.
# for getting set of visited nodes in every path , we will use BIT masking.
# i.e if bitmask value is different after reaching any node then it means we have reached that node 
# through different path.

# And when mask == all_1 i.e 2^n -1 then means we have visited all nodes and that will be our ans.

# Note: first time when we will visit all nodes that will be our ans so no need to use minHeap according to steps.

# bitMask: mask of all the nodes we visited so far

# time: O(2^n -1)

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        allVisitedMask = (1 << n) - 1   # 2^n -1
        visited = set()
        q = deque()
        for i in range(n):
            # 1st add all nodes in queue we don't know starting from which node will lead to ans 
            # and make bit at that 'node' index = 1.
            # bit value at any position = 1 will tell this node is already visited in cur path.
            q.append((i, 1 << i, 0))   # (node, nodes_included_in_path, steps)
            visited.add((i, 1 << i))   # (node, nodes_included_in_path)
            # Path = mask 
        
        while q:
            node, mask, steps = q.popleft()
            if mask == allVisitedMask:
                return steps
            for nei in graph[node]:
                # check if we are visiting 'nei' through different path 
                if (nei , mask | 1 << nei) not in visited:
                    if mask | 1 << nei == allVisitedMask:
                        return steps + 1
                    # if we take include cur node also in path then mask= mask | 1 << nei
                # because we will have to set 'node' bit = 1
                    q.append((nei, mask | 1 << nei, steps + 1))
                    visited.add((nei, mask | 1 << nei))