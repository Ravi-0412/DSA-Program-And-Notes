# Just same as "3341. Find Minimum Time to Reach Last Room I".
# Only difference is here cost of movement from adjacent cell will be alternate i.e
# 1 -> 2 -> 1 -> 2 ....

# Time: O(4*n*m)

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # left, right, up , down
        minTime = [[float('inf') for j in range(m)] for i in range(n)]
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0, 2))
        visited = set()
        while minHeap:
            time, r, c, move_taken = heapq.heappop(minHeap)
            if r == n - 1 and c == m - 1:
                return time
            visited.add((r, c))
            for dr, dc in directions:
                r1, c1 = r + dr , c + dc
                if 0 <= r1 < n and 0 <= c1 < m and (r1, c1) not in visited:
                    min_time_required = max(moveTime[r1][c1], time) + 1 if move_taken == 2 else max(moveTime[r1][c1], time) + 2
                    if minTime[r1][c1] > min_time_required:
                        if move_taken == 1:
                            heapq.heappush(minHeap, (min_time_required, r1, c1, 2))
                        else:
                            heapq.heappush(minHeap, (min_time_required, r1, c1, 1))
                        minTime[r1][c1] = min_time_required
        
                
        
        
