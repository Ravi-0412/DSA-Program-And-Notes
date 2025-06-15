# logic: 
"""
When you see that given a source/index , you can go to some other point/ index &&
using those next points you can go some other point and so on.
Then must think of bfs / multisource bfs or dfs.

Time: O(V+ E), space: O(V). Just same as bfs
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        dq = deque()
        visited = set()
        dq.append(0)
        visited.add(0)
        while dq:
            key = dq.popleft()
            for room in rooms[key]:
                if room not in visited:
                    dq.append(room)
                    visited.add(room)
        return len(visited) == n   # if len(visited) == n then, we can enter all rooms.

# Java code 
"""
import java.util.*;

class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        Deque<Integer> dq = new ArrayDeque<>();
        Set<Integer> visited = new HashSet<>();
        dq.add(0);
        visited.add(0);
        while (!dq.isEmpty()) {
            int key = dq.poll();
            for (int room : rooms.get(key)) {
                if (!visited.contains(room)) {
                    dq.add(room);
                    visited.add(room);
                }
            }
        }
        return visited.size() == n;  // if len(visited) == n then, we can enter all rooms.
    }
}

"""
# C++ Code 
"""
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        queue<int> dq;
        unordered_set<int> visited;
        dq.push(0);
        visited.insert(0);
        while (!dq.empty()) {
            int key = dq.front();
            dq.pop();
            for (int room : rooms[key]) {
                if (visited.find(room) == visited.end()) {
                    dq.push(room);
                    visited.insert(room);
                }
            }
        }
        return visited.size() == n;  // if len(visited) == n then, we can enter all rooms.
    }
};

"""