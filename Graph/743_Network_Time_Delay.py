# just totally based on Dijkastra Algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj= collections.defaultdict(list)
        for u,v,w in times:
            adj[u].append((v, w))
        min_time= 0
        minHeap= [(0,k)]
        visited= set()  # it will contain the node whose adjacent node is also visited
        while minHeap:
            w1, n1= heapq.heappop(minHeap)
            if n1 in visited: # if visited simply skip
                continue
            # if not visited, add to visited set and visit all its nodes and update the weight
            visited.add(n1)
            min_time= max(min_time, w1)
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap,(w1+ w2, n2))   # add in heap by adding the weight of its parent also
        return min_time if len(visited)== n else -1
    