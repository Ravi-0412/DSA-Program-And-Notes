# Method 1: 
# Q: min time needed to reach all the nodes from all possible paths.

# Similar to Q: "778. Swim in Rising Water". 
# Analyse both properly.

# my mistake
#  used mutisource bfs.
# TLE : Because we are inserting a single node multiple times and checking it's nei also many time.
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        q= collections.deque([(0,0)])
        time= 0
        while q:
            visited= set()
            for i in range(len(q)):
                r, c= q.popleft()
                if r== row-1 and c== col-1:
                    return time
                directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
                for nr, nc in directions:
                    if 0<= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc]<= time +1:
                        # if nr== row-1 and nc== col-1:
                        #     return time
                        q.append((nr, nc))
                        visited.add((nr, nc))
            time+= 1
        return -1


# Correct

# optimising and using dijskatra
# Note: we can always reach the bottom-right cell of the matrix if we can move to at least one adjacent cell (i.e. grid[0][1] or grid[1][0]). 
# After that we can simply move back and forth to spend time as needed.
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1 :
            return -1
        row, col= len(grid), len(grid[0])
        minHeap= []
        heapq.heappush(minHeap, (0, 0, 0) )   # [(time, r, c)]
        visited= set()
        while minHeap:
            time, r, c= heapq.heappop(minHeap)
            if r== row- 1 and c== col-1:
                return time
            if (r, c) in visited:    # means we have already relaxed all edges through this. Already poped before
                continue
            visited.add((r, c))    # we are going to relax all edges through this.
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
            for nr, nc in directions:
                    if nr < 0 or nr >= row or nc <0 or nc >= col or (nr, nc) in visited:
                        continue
                    # if we can visit the neigh with current time then add into the heap
                    if grid[nr][nc] <= time +1:
                        heapq.heappush(minHeap, (time+1, nr, nc))
                    # find the time when we can visit the cell (nr, nc) later
                    else:
                        diff= grid[nr][nc] - time
                        if diff & 1: 
                            # if difference is odd then we can visit that cell in 'grid[nr][nc]' time during back and forth 
                            # to other cell in this diff to of time i.e we can come back to (nr, nc) in grid[nr][nc].
                            heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                        else:  # if even then we can visit in time = 'grid[nr][nc] +1' later.
                            heapq.heappush(minHeap, (grid[nr][nc] +1, nr, nc))
        return -1  # No need of this. if it reachable to any of two of the directions from (0,0) then it will keeping going back & forth.
                    # And will reach the destination at any point of time.


# Java
"""
import java.util.*;

class Solution {
    public int minimumTime(int[][] grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }
        int row = grid.length, col = grid[0].length;
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{0, 0, 0});  // [(time, r, c)]
        boolean[][] visited = new boolean[row][col];

        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int time = curr[0], r = curr[1], c = curr[2];

            if (r == row - 1 && c == col - 1) return time;

            if (visited[r][c]) continue;  // means we have already relaxed all edges through this
            visited[r][c] = true;         // we are going to relax all edges through this

            int[][] directions = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}}; // up, down, left, right
            for (int[] dir : directions) {
                int nr = dir[0], nc = dir[1];
                if (nr < 0 || nr >= row || nc < 0 || nc >= col || visited[nr][nc]) continue;

                // if we can visit the neigh with current time then add into the heap
                if (grid[nr][nc] <= time + 1) {
                    minHeap.offer(new int[]{time + 1, nr, nc});
                } else {
                    // find the time when we can visit the cell (nr, nc) later
                    int diff = grid[nr][nc] - time;
                    if ((diff & 1) == 1) {
                        // if difference is odd then we can visit that cell in 'grid[nr][nc]' time during back and forth
                        // to other cell in this diff to of time i.e we can come back to (nr, nc) in grid[nr][nc].
                        minHeap.offer(new int[]{grid[nr][nc], nr, nc});
                    } else {
                        // if even then we can visit in time = 'grid[nr][nc] +1' later.
                        minHeap.offer(new int[]{grid[nr][nc] + 1, nr, nc});
                    }
                }
            }
        }
        return -1; // No need of this. if it reachable to any of two of the directions from (0,0)
                   // then it will keep going back & forth. And will reach the destination at any point of time.
    }
}

"""


# C++
"""
#include <vector>
#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }

        int row = grid.size(), col = grid[0].size();
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> minHeap;
        set<pair<int, int>> visited;

        minHeap.push({0, 0, 0}); // (time, r, c)

        while (!minHeap.empty()) {
            auto [time, r, c] = minHeap.top();
            minHeap.pop();

            if (r == row - 1 && c == col - 1) {
                return time;
            }

            if (visited.count({r, c})) {
                // means we have already relaxed all edges through this. Already popped before
                continue;
            }

            visited.insert({r, c}); // we are going to relax all edges through this.

            // up, down, left, right
            vector<pair<int, int>> directions = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}};
            for (auto [nr, nc] : directions) {
                if (nr < 0 || nr >= row || nc < 0 || nc >= col || visited.count({nr, nc})) {
                    continue;
                }

                // if we can visit the neighbor with current time then add into the heap
                if (grid[nr][nc] <= time + 1) {
                    minHeap.push({time + 1, nr, nc});
                } else {
                    int diff = grid[nr][nc] - time;
                    if (diff % 2 == 1) {
                        // if difference is odd then we can visit that cell in 'grid[nr][nc]' time during back and forth 
                        // to other cell in this diff of time i.e. we can come back to (nr, nc) in grid[nr][nc].
                        minHeap.push({grid[nr][nc], nr, nc});
                    } else {
                        // if even then we can visit in time = 'grid[nr][nc] + 1' later.
                        minHeap.push({grid[nr][nc] + 1, nr, nc});
                    }
                }
            }
        }

        return -1; 
        // No need of this. if it reachable to any of two of the directions from (0,0) then it will keep going back & forth.
        // And will reach the destination at any point of time.
    }
};

"""


# Method 2: 

# Note: we can mark visited when we will see the cell for first time also because when we are seeing the cell for 1st time then,
# we are able to find the minimum time in which we can reach that node later similar to "Q.778. swimming water".
# we can check the ans at 1st time itself.
# Better one: Helps in avoiding to update the time for same node more than one time.

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1 :
            return -1
        row, col= len(grid), len(grid[0])
        minHeap= []
        heapq.heappush(minHeap, (0, 0, 0) )   # [(time, r, c)]
        visited= set()
        visited.add((0,0))
        while minHeap:
            time, r, c= heapq.heappop(minHeap)
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
            for nr, nc in directions:
                    if nr < 0 or nr >= row or nc <0 or nc >= col or (nr, nc) in visited:
                        continue
                    diff= (grid[nr][nc] - time) % 2== 0   # if even diff= 1 and if odd , diff= 1.  # waiting time.
                    minTimeToVisit= max(grid[nr][nc] + diff, time + 1)  # (time+1) was min time in which we can visit (nr, nc) but if not reachable then we have to wait . so mintime= max(grid[nr][nc] + diff, time + 1)
                    if nr== row-1 and nc== col-1:
                        return minTimeToVisit
                    heapq.heappush(minHeap, (minTimeToVisit, nr, nc))
                    visited.add((nr, nc))


# Java
"""
import java.util.*;

class Solution {
    public int minimumTime(int[][] grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }
        int row = grid.length, col = grid[0].length;
        // PriorityQueue storing (time, r, c), ordered by time
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        Set<String> visited = new HashSet<>();
        
        minHeap.offer(new int[] {0, 0, 0});
        visited.add("0,0");
        
        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int time = top[0], r = top[1], c = top[2];

            int[][] directions = {{r - 1, c}, {r + 1, c}, {r, c - 1}, {r, c + 1}}; // up, down, left, right
            for (int[] dir : directions) {
                int nr = dir[0], nc = dir[1];
                String key = nr + "," + nc;
                if (nr < 0 || nr >= row || nc < 0 || nc >= col || visited.contains(key)) {
                    continue;
                }
                // waiting time calculation
                int diff = (grid[nr][nc] - time) % 2 == 0 ? 1 : 0;
                int minTimeToVisit = Math.max(grid[nr][nc] + diff, time + 1);
                
                if (nr == row - 1 && nc == col - 1) {
                    return minTimeToVisit;
                }
                minHeap.offer(new int[] {minTimeToVisit, nr, nc});
                visited.add(key);
            }
        }
        
        return -1; // unreachable
    }
}


"""


# C++
"""
#include <vector>
#include <queue>
#include <set>
#include <tuple>
using namespace std;

class Solution {
public:
    int minimumTime(vector<vector<int>>& grid) {
        if (grid[0][1] > 1 && grid[1][0] > 1) {
            return -1;
        }
        int row = grid.size(), col = grid[0].size();

        // min-heap of (time, r, c)
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<>> minHeap;
        set<pair<int,int>> visited;

        minHeap.push({0, 0, 0});
        visited.insert({0, 0});

        while (!minHeap.empty()) {
            auto [time, r, c] = minHeap.top(); minHeap.pop();

            vector<pair<int,int>> directions = {{r-1, c}, {r+1, c}, {r, c-1}, {r, c+1}}; // up,down,left,right
            for (auto& [nr, nc] : directions) {
                if (nr < 0 || nr >= row || nc < 0 || nc >= col || visited.count({nr, nc})) {
                    continue;
                }
                // waiting time calculation
                bool diff = ((grid[nr][nc] - time) % 2 == 0);
                int minTimeToVisit = max(grid[nr][nc] + (diff ? 1 : 0), time + 1);

                if (nr == row - 1 && nc == col - 1) {
                    return minTimeToVisit;
                }
                minHeap.push({minTimeToVisit, nr, nc});
                visited.insert({nr, nc});
            }
        }

        return -1; // unreachable
    }
};


"""
