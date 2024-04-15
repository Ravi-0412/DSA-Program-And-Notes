# Logic: Just exact Dijkastra, just before adding into 'minHeap' check if that node is already disappeared in that time. If not disappeared then only add into 'minHeap'.


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v, length in edges:
            adj[u].append((v, length))
            adj[v].append((u, length))
            
        ans = [-1] * n       
        minHeap = [(0, 0)]             
        while minHeap:
            time, node = heapq.heappop(minHeap)            
            if ans[node] != -1:
                # already this node is relaxed
                continue
            ans[node] = time                      
            for nei, t in adj[node]:
                if time + t < disappear[nei]:
                    # If 'nei' has not disappeared till this time then only add
                    # i.e we can only use 'nei' for shortest time if it has not disappeared
                    heapq.heappush(minHeap, (time + t, nei))
        return ans