# Method 1: 

"""
can be done by dfs but it will take o(m*n)^2 as for evey cell you have to run the dfs

method 2: using multisource bfs from gate to room.
reverse the problem and find the distance of room starting from all the gates.
since telling to fill each empty room with the nearest distance to any gate.
So add all 'gates' in queue and apply multisource bfs.

how came with this: since using bfs we can mark all the grid at level one in 1st iteration , at level 2 in 2nd and so on and this only we have to do
by doing with multisource bfs we can get the optimal ans directly for each grid 
if you do with single source bfs then it won't work in time O(m*n)

No need to make visited set , grid will behave as visited set automatically 
when we will check the value.. if value is changed then visited else not
but it is always better to don't change the data given to you in terms of industry point of view.
"""


from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        row, col = len(rooms), len(rooms[0])
        q = deque()
        distance = 0

        for r in range(row):
            for c in range(col):  # appending all the gates into the 'Q'
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            distance += 1  # all room at level 1 will have distance 1
            for i in range(len(q)):
                r1, c1 = q.popleft()
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r, c = r1 + dr, c1 + dc
                    # if a[r][c] is not 'inf' means if already marked then that will be minimum distance only so not checking that condition
                    if 0 <= r < row and 0 <= c < col and rooms[r][c] == 2147483647:
                        rooms[r][c] = distance
                        q.append((r, c))  # for next iteration

# Java
"""
import java.util.*;

class Solution {
    public void wallsAndGates(int[][] rooms) {
        int row = rooms.length, col = rooms[0].length;
        Queue<int[]> q = new LinkedList<>();
        int distance = 0;

        // Appending all the gates into the 'Q'
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (rooms[r][c] == 0) {
                    q.offer(new int[]{r, c});
                }
            }
        }

        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};  // up, down, left, right

        while (!q.isEmpty()) {
            distance++;  // all room at level 1 will have distance 1
            int size = q.size();

            for (int i = 0; i < size; i++) {
                int[] cell = q.poll();
                int r1 = cell[0], c1 = cell[1];

                for (int[] dir : directions) {
                    int r = r1 + dir[0], c = c1 + dir[1];
                    // if a[r][c] is not 'inf' means if already marked then that will be minimum distance only so not checking that condition
                    if (r >= 0 && r < row && c >= 0 && c < col && rooms[r][c] == Integer.MAX_VALUE) {
                        rooms[r][c] = distance;
                        q.offer(new int[]{r, c});  // for next iteration
                    }
                }
            }
        }
    }
}


"""


# C++
"""
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int row = rooms.size(), col = rooms[0].size();
        queue<pair<int, int>> q;
        int distance = 0;

        // Appending all the gates into the 'Q'
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (rooms[r][c] == 0) {
                    q.push({r, c});
                }
            }
        }

        vector<vector<int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};  // up, down, left, right

        while (!q.empty()) {
            distance++;  // all room at level 1 will have distance 1
            int size = q.size();

            for (int i = 0; i < size; ++i) {
                auto [r1, c1] = q.front(); q.pop();

                for (auto& dir : directions) {
                    int r = r1 + dir[0], c = c1 + dir[1];
                    // if a[r][c] is not 'inf' means if already marked then that will be minimum distance only so not checking that condition
                    if (r >= 0 && r < row && c >= 0 && c < col && rooms[r][c] == INT_MAX) {
                        rooms[r][c] = distance;
                        q.push({r, c});  // for next iteration
                    }
                }
            }
        }
    }
};


"""

