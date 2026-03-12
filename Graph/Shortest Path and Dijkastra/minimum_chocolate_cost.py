# Logic: We can purchase chocolate at each node 

from collections import defaultdict
import heapq

def minimumCost(n , routes, chocolateCost, k):
    adj = defaultdict(list)
    for a, b, c in routes:
        adj[a - 1].append((b - 1, c))
        adj[b- 1].append((a- 1,   c))
    

    def bfs(node, cost):
        minHeap = []
        visited = set()
        ans = float('inf')
        heapq.heappush(minHeap, (0, node))

        while minHeap:
            c, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            # 1) if we purchase at this town
            # current cost 'c' + cost_to_buy_chocolate_at_this_node + cost_returning_back
            totalCost = c + chocolateCost[node] + c*k
            ans = min(ans, totalCost)
            visited.add(node)

            # Also check when we purchase at it's neighbour town
            for nei , c1 in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (c + c1, nei))
        return ans

    ans = []
    for i in range(n):
        curAns = bfs(i, 0)
        ans.append(curAns)
    return ans 



# n = 4
# routes = [[1, 2, 4], [2, 3, 2], [2, 4, 5], [3, 4, 1], [1, 3, 4]]
# chocolateCost = [56, 42, 102, 301]
# k = 2

n = 3
routes = [[1, 2, 5], [2, 3, 1], [3, 1, 2]]
chocolateCost = [2, 3, 1]
k = 1

#In 2nd case all will purchase chocolate at same town only

print(minimumCost(n, routes, chocolateCost, k))