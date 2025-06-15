# Read this carefully:
# 'person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B'.

# In simple word, it means a person 'A' can know other person 'B' if 'A' is friend of 'B' or
# 'A' knows someone who is friend of 'B'.

# This is recursive statement in itself when you will draw on paper.

# note: we have to find minimum cost to connect all people.
# i.e from all possible path take the maximum time and that will be answer. 

# Other way to ask this question is: "find the max edge cost from a MST".
# Just 'MST' logic only. Here no need to add just take maximum of all edge weight.

import heapq
from collections import defaultdict
def minTime(logs, n):
    if len(logs) < n -1:  # we need at least 'n-1' edge to connect 'n' nodes
        return -1
    edges = defaultdict(list)
    for w, u, v in logs:
        edges[u].append((v, w))
        edges[v].append((u, w))
    visited = set()
    min_time = 0
    min_heap = [(0,0)]  # we can start from any node. strarted with smallest one
    # Here changed from 'while len(visited) < n'. Because all may be not connected also.
    while min_heap:  
        w1,n1= heapq.heappop(min_heap)
        if n1 in visited:  
            continue
        visited.add(n1)
        min_time = max(min_time, w1)  # taking max of all edge weight
        for n2,w2 in edges[n1]:
            if n2 not in visited:
                heapq.heappush(min_heap,(w2, n2))
        
    return min_time if len(visited)== n else -1


# Note: one more method using DSU (see inside DSU)