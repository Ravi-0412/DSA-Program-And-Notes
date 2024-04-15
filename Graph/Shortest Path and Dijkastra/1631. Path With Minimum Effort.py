# Q: Find min absolute diff between consecutive cell of all the possible paths.

# just same as Dijakstra Algo. Just slight modification acc to the Q.
# Difference from Q: "778. Swim in Rising Water"? => we were marking visited in 'Q 778' 
#  were visiting any node for first time only.
# since that will be the optimal ans for that cell.

# But in this Q, there can be other path possible with larger absolute difference 
# so we will mark visited only after we will relax all directions from it.
# i.e only after we will pop
# Take the 1st example for clarification.

# Time complexity:O(M∗N∗log(M∗N)). Just 'ElogV' where E = m*n and V= m*m

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m= len(heights), len(heights[0])
        visited= set()
        heap= [(0, 0, 0)]       # first one is min_difference_till_now and other two is cell index.
        heapq.heapify(heap)
        while heap:
            diff, r, c= heapq.heappop(heap)
            if r== n-1 and c== m-1 :
                return diff
            # this i was missing. mark visited only after you relax all directions from a cell, not when you visit for 1st time itself.
            if (r, c) in visited:  
                continue
            visited.add((r, c))  
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]  # up, down. left, right
            for nr, nc in directions:
                if 0<= nr < n and 0<= nc < m and (nr, nc) not in visited:
                    curr_diff= abs(heights[r][c] - heights[nr][nc])
                    # we have already taken the path with with difference = 'diff' so we can't take less than that for curr path so maximising.
                    min_diff_till_now= max(diff, curr_diff)
                    # you can only reach cell (nr, nc) with minimum diff between any two cell = min_diff_till_now  
                    heapq.heappush(heap, (min_diff_till_now, nr, nc))  


# Method 2: Using binary search
# Time complexity:O(M∗N∗log(M∗N))
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m= len(heights), len(heights[0])

        # Just bfs only
        # Is it possible to reach destination having height diff between any two consecutive <=k.
        def isPossible(k): 
            visited= set()
            q= deque()
            q.append((0, 0))
            visited.add((0, 0))
            while q:
                r, c= q.popleft()
                if r== n-1 and c== m-1 :
                    return 1
                directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]  # up, down. left, right
                for nr, nc in directions:
                    if 0<= nr < n and 0<= nc < m and (nr, nc) not in visited and abs(heights[r][c] - heights[nr][nc]) <=k:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return 0

        start , end = 0, 10**6
        while start < end:
            mid = start + (end - start)//2
            if isPossible(mid):
                # then find more less
                end = mid
            else:
                # check bigger value
                start = mid + 1
        return start


