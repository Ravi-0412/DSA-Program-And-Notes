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

# Java Code 
"""
import java.util.*;

class Solution {
    // Method 1: Using Dijkstra-like approach with a min-heap (PriorityQueue)
    public int minimumEffortPath(int[][] heights) {
        int n = heights.length, m = heights[0].length;
        Set<String> visited = new HashSet<>();
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        heap.offer(new int[]{0, 0, 0}); // {diff, r, c}

        while (!heap.isEmpty()) {
            int[] curr = heap.poll();
            int diff = curr[0], r = curr[1], c = curr[2];
            if (r == n - 1 && c == m - 1) {
                return diff;
            }
            // this i was missing. mark visited only after you relax all directions from a cell, not when you visit for 1st time itself.
            String key = r + "," + c;
            if (visited.contains(key)) {
                continue;
            }
            visited.add(key);

            int[][] directions = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}}; // up, down, left, right
            for (int[] d : directions) {
                int nr = d[0], nc = d[1];
                String nkey = nr + "," + nc;
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && !visited.contains(nkey)) {
                    int curr_diff = Math.abs(heights[r][c] - heights[nr][nc]);
                    // we have already taken the path with difference = 'diff' so we can't take less than that for curr path so maximising.
                    int min_diff_till_now = Math.max(diff, curr_diff);
                    // you can only reach cell (nr, nc) with minimum diff between any two cell = min_diff_till_now  
                    heap.offer(new int[]{min_diff_till_now, nr, nc});
                }
            }
        }
        return 0; // fallback, should not happen
    }

    // Method 2: Using binary search + BFS
    public int minimumEffortPathBinarySearch(int[][] heights) {
        int n = heights.length, m = heights[0].length;

        // Just bfs only
        // Is it possible to reach destination having height diff between any two consecutive <=k.
        boolean isPossible(int k) {
            Set<String> visited = new HashSet<>();
            Queue<int[]> q = new LinkedList<>();
            q.offer(new int[]{0, 0});
            visited.add("0,0");
            int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

            while (!q.isEmpty()) {
                int[] curr = q.poll();
                int r = curr[0], c = curr[1];
                if (r == n - 1 && c == m - 1) {
                    return true;
                }
                for (int[] d : directions) {
                    int nr = r + d[0], nc = c + d[1];
                    String nkey = nr + "," + nc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m && !visited.contains(nkey) &&
                        Math.abs(heights[r][c] - heights[nr][nc]) <= k) {
                        q.offer(new int[]{nr, nc});
                        visited.add(nkey);
                    }
                }
            }
            return false;
        }

        int start = 0, end = 1000000;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (isPossible(mid)) {
                // then find more less
                end = mid;
            } else {
                // check bigger value
                start = mid + 1;
            }
        }
        return start;
    }
}

"""
# C++ Code 
"""
#include <vector>
#include <queue>
#include <set>
#include <cmath>
using namespace std;

class Solution {
public:
    // Method 1: Using Dijkstra-like approach with min-heap (priority_queue)
    int minimumEffortPath(vector<vector<int>>& heights) {
        int n = (int)heights.size();
        int m = (int)heights[0].size();
        set<pair<int,int>> visited;
        // priority_queue stores {diff, {r, c}} with smallest diff on top
        priority_queue< pair<int,pair<int,int>>, vector<pair<int,pair<int,int>>>, greater<pair<int,pair<int,int>>> > heap;
        heap.push({0, {0, 0}});  // {diff, {r, c}}

        while (!heap.empty()) {
            auto curr = heap.top();
            heap.pop();
            int diff = curr.first, r = curr.second.first, c = curr.second.second;
            if (r == n - 1 && c == m - 1) {
                return diff;
            }
            // this i was missing. mark visited only after you relax all directions from a cell, not when you visit for 1st time itself.
            if (visited.count({r, c})) {
                continue;
            }
            visited.insert({r, c});

            vector<vector<int>> directions = {{r-1, c}, {r+1, c}, {r, c-1}, {r, c+1}}; // up, down, left, right
            for (auto &d : directions) {
                int nr = d[0], nc = d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && visited.count({nr, nc}) == 0) {
                    int curr_diff = abs(heights[r][c] - heights[nr][nc]);
                    // we have already taken the path with difference = 'diff' so we can't take less than that for curr path so maximising.
                    int min_diff_till_now = max(diff, curr_diff);
                    // you can only reach cell (nr, nc) with minimum diff between any two cell = min_diff_till_now  
                    heap.push({min_diff_till_now, {nr, nc}});
                }
            }
        }
        return 0; // fallback, should not happen
    }

    // Method 2: Using binary search + BFS
    bool isPossible(int k, vector<vector<int>>& heights) {
        int n = (int)heights.size();
        int m = (int)heights[0].size();
        set<pair<int,int>> visited;
        queue<pair<int,int>> q;
        q.push({0, 0});
        visited.insert({0, 0});
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // up, down, left, right

        while (!q.empty()) {
            auto curr = q.front();
            q.pop();
            int r = curr.first, c = curr.second;
            if (r == n - 1 && c == m - 1) {
                return true;
            }
            for (auto &d : directions) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && visited.count({nr, nc}) == 0 &&
                    abs(heights[r][c] - heights[nr][nc]) <= k) {
                    q.push({nr, nc});
                    visited.insert({nr, nc});
                }
            }
        }
        return false;
    }

    int minimumEffortPathBinarySearch(vector<vector<int>>& heights) {
        int start = 0, end = 1000000;
        while (start < end) {
            int mid = start + (end - start)/2;
            if (isPossible(mid, heights)) {
                // then find more less
                end = mid;
            } else {
                // check bigger value
                start = mid + 1;
            }
        }
        return start;
    }
};

"""