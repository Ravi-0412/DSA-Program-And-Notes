# Q: Find min absolute diff between consecutive cell of all the possible paths.

# just same as Dijakstra Algo. Just slight modification acc to the Q.
# Difference from Q: "778. Swim in Rising Water"? => we were marking visited in 'Q 778' when we were visiting any node for first time only
# since that will be the optimal ans for that cell.
# But in this Q, there can be other path possible with larger absolute difference so we will mark visited only after we will relax all directions from it.
# i.e only after we will pop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m= len(heights), len(heights[0])
        visited= set()
        heap= [(0, 0, 0)]       # first one is difference and other two is cell index.
        heapq.heapify(heap)
        while heap:
            diff, r, c= heapq.heappop(heap)
            if r== n-1 and c== m-1 :
                return diff
            if (r, c) in visited:  # this i was missing. mark visited only after you relax all directions from a cell, not when you visit for 1st time itself.
                continue
            visited.add((r, c))   # since same cell can be added more than once with othwe weight value. and if it has been already visited then skip.
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]  # up, down. left, right
            for nr, nc in directions:
                if 0<= nr < n and 0<= nc < m and (nr, nc) not in visited:
                    curr_diff= abs(heights[r][c] - heights[nr][nc])
                    min_diff_till_now= max(diff, curr_diff)   # we have already taken the path with with difference = 'diff' so we can't take less than that for curr path so maximising.
                    heapq.heappush(heap, (min_diff_till_now, nr, nc))


