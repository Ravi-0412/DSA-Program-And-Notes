# Just similar logic as : "778. Swim in Rising Water"

# time: O(4*n*m) , we can visit same cell four time from four different directions.

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # left, right, up , down
        minTime = [[float('inf') for j in range(m)] for i in range(n)]
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        visited = set()
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == m - 1:
                return time
            visited.add((r, c))
            for dr, dc in directions:
                r1, c1 = r + dr , c + dc
                if 0 <= r1 < n and 0 <= c1 < m and (r1, c1) not in visited:
                    min_time_required = max(moveTime[r1][c1], time) + 1
                    if minTime[r1][c1] > min_time_required:
                        heapq.heappush(minHeap, (min_time_required, r1, c1))
                        minTime[r1][c1] = min_time_required
        
                
# Related q:
# 1) 3342. Find Minimum Time to Reach Last Room II
