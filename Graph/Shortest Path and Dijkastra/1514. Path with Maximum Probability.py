# Logic: Exactly same as "Dijkastra Algo".
# only difference here we will use maxHeap instead of minHeap.

# vvi: when we will relax the node then only we will get the ans because 
# later probability will keep on multiplying so it will become smaller only.
# so it will guarantee the maximum one.

# Time: O(ElogV)
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj= collections.defaultdict(list)
        # First make the adjacency list in same way we used to make in Dijkastra.
        for i in range(len(edges)):
            u , v , prob = edges[i][0], edges[i][1] , succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob)) 

        visited = set()
        maxHeap = [(-1, start)]
        while maxHeap:
            prob, n1 = heapq.heappop(maxHeap)
            if n1 == end:
                return -1 * prob
            visited.add(n1)
            for n2, p in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(maxHeap, (prob * p , n2))
        return 0 


# Getting the ans when we will see for first time will give wrong ans.
# Because later we can get 'end' with other path having maximum probability ,so  it will not guarantee the maximum one.

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj= collections.defaultdict(list)
        for i in range(len(edges)):
            u , v , prob = edges[i][0], edges[i][1] , succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob)) 

        visited = set()
        maxHeap = [(-1, start)]
        while maxHeap:
            prob, n1 = heapq.heappop(maxHeap)
            visited.add(n1)
            for n2, p in adj[n1]:
                if n2 == end:
                    return -1 *prob * p 
                if n2 not in visited:
                    heapq.heappush(maxHeap, (prob * p , n2))
        return 0 