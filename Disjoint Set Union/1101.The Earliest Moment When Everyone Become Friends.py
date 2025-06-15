# Logic: when we see problems related to connectivity, we should think of applying DSU. 
# This problem asks us to find the first instance where the graph formed by friendships is connected. 
# To accomplish this, we'll first sort the friendships by timestamp

# If for one log, the two people belong to different groups, then merge the people of the two groups into one group
# and keep decreasing '1'.
# Once 'n' becomes 1, everyone becomes friends, so return the timestamp.

# Time: m*logm (m= len(logs))

import heapq
from collections import defaultdict
def minTime(logs, n):
    
    parent = [i for i in range(n)]  # list(range(n))
    size =   [1 for i in range(n)]

    def findParent(x):
        if x == parent[x]:
            return x
        parent[x] = findParent(parent[x])
        return parent[x]
    
    def unionBySize(n1, n2):
        p1, p2= findParent(n1), findParent(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return False
        if size[p1] < size[p2]:
            parent[p1]= p2  
            size[p2]+= size[p1]   
        else :   # rank[p1]>= rank[p2]
            parent[p2]= p1   
            size[p1]+= size[p2]
        return True
    
    logs.sort()
    print(logs)
    for w, u, v in logs:
        if unionBySize(u, v):
            n -= 1
            if n== 1:
                return w
    return -1

# logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]] 
# N = 6

# logs = [[2,0,1],[3,1,2],[4,2,3]]
# N = 4

logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
N = 4
print(minTime(logs, N))


# other method : using MST(see in graph)