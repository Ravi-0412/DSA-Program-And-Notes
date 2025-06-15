# Method 1: 

# My mistake
"""
1st thought but it won't work.
If we store inorder in an array say array: inorder then, for query(i, j), we 
will check if index of 'j' > index of 'i' in inorder then ans = True else False.

But it won't work for multiple component and when there will be more than one node at the same level.
"""


# Logic:
"""
1) Add the direct given prerequisite say 'reachable' adjacency set
2) Now traverse again all pairs(i, j) and check if 'i' is in prerequisite of 'j' then, 
it means all courses that are prerequisite of 'i' will be prerequisite of 'j.
So add set of reachable courses of 'i' to 'j'.

3) Now traverse all query(i, j) and check if 'i' is in reachable set of 'j'or not.
"""

# Update() function in python set
"""
In Python, the set's update() function allows you to add multiple elements to the set from another iterable (like a list, tuple, or another set).
syntax : set1.update(iterable)

# Create a set
s = {1, 2, 3}

# Add elements from a list
s.update([4, 5, 6])
print(s)  # Output: {1, 2, 3, 4, 5, 6}

# Add elements from another set
s.update({7, 8})
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# You can also add individual elements
s.update([9])
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

"""
# Time: O(n^2)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        # Initialize the reachability map
        reachable = {i: set() for i in range(numCourses)}   # node: setofPreReq

       # Build direct reachability chains
        for u, v in prerequisites:
            reachable[v].add(u)     # 'v' ka preReq 'U' h

        # Propagate reachability to account for indirect prerequisites
        for i in range(numCourses):
            for j in range(numCourses):
                if i in reachable[j]:
                    reachable[j].update(reachable[i])

        # Answer the queries
        result = []
        for u, v in queries:
            result.append(u in reachable[v])

        return result

# Java
"""
import java.util.*;

class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        // Initialize the reachability map
        Map<Integer, Set<Integer>> reachable = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            reachable.put(i, new HashSet<>()); // node: set of PreReq
        }

        // Build direct reachability chains
        for (int[] pre : prerequisites) {
            int u = pre[0];
            int v = pre[1];
            reachable.get(v).add(u); // 'v' ka preReq 'u' hai
        }

        // Propagate reachability to account for indirect prerequisites
        for (int i = 0; i < numCourses; i++) {
            for (int j = 0; j < numCourses; j++) {
                if (reachable.get(j).contains(i)) {
                    reachable.get(j).addAll(reachable.get(i));
                }
            }
        }

        // Answer the queries
        List<Boolean> result = new ArrayList<>();
        for (int[] query : queries) {
            int u = query[0];
            int v = query[1];
            result.add(reachable.get(v).contains(u));
        }

        return result;
    }
}

"""


# C++
"""
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        // Initialize the reachability map
        vector<unordered_set<int>> reachable(numCourses);  // node: set of PreReq

        // Build direct reachability chains
        for (const auto& pre : prerequisites) {
            int u = pre[0];
            int v = pre[1];
            reachable[v].insert(u);  // 'v' ka preReq 'u' hai
        }

        // Propagate reachability to account for indirect prerequisites
        for (int i = 0; i < numCourses; ++i) {
            for (int j = 0; j < numCourses; ++j) {
                if (reachable[j].count(i)) {
                    reachable[j].insert(reachable[i].begin(), reachable[i].end());
                }
            }
        }

        // Answer the queries
        vector<bool> result;
        for (const auto& query : queries) {
            int u = query[0];
            int v = query[1];
            result.push_back(reachable[v].count(u));
        }

        return result;
    }
};

"""


# Method 2:
"""
Just use bitset for marking prerequisite instead of set.
Time:
  Graph construction: O(E) (edges).
  Topological sort: O(N + E).
  Query handling: O(Q).
Space: O(N^2) (bitsets for N courses, each with N bits).
"""

from collections import deque

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        adj = [[] for _ in range(numCourses)]
        prereq = [0] * numCourses  # Bitmask for prerequisites
        in_degree = [0] * numCourses
        
        # Build graph and initialize direct prerequisites
        for a, b in prerequisites:
            adj[a].append(b)
            prereq[b] |= 1 << a  # Set the a-th bit for course b
            in_degree[b] += 1
        
        # Topological sort using Kahn's algorithm
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                prereq[v] |= prereq[u]  # Merge u's prerequisites into v's
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        
        # Answer queries using bitmask checks
        ans = []
        for u, v in queries:
            ans.append((prereq[v] & (1 << u)) != 0)
        return ans


# Java
"""
import java.util.*;

class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        List<Integer>[] adj = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            adj[i] = new ArrayList<>();
        }

        int[] prereq = new int[numCourses]; // Bitmask for prerequisites
        int[] inDegree = new int[numCourses];

        // Build graph and initialize direct prerequisites
        for (int[] edge : prerequisites) {
            int a = edge[0], b = edge[1];
            adj[a].add(b);
            prereq[b] |= 1 << a; // Set the a-th bit for course b
            inDegree[b]++;
        }

        // Topological sort using Kahn's algorithm
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.offer(i);
            }
        }

        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                prereq[v] |= prereq[u]; // Merge u's prerequisites into v's
                inDegree[v]--;
                if (inDegree[v] == 0) {
                    q.offer(v);
                }
            }
        }

        // Answer queries using bitmask checks
        List<Boolean> ans = new ArrayList<>();
        for (int[] query : queries) {
            int u = query[0], v = query[1];
            ans.add((prereq[v] & (1 << u)) != 0);
        }

        return ans;
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
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<int>> adj(numCourses);
        vector<int> prereq(numCourses, 0); // Bitmask for prerequisites
        vector<int> in_degree(numCourses, 0);

        // Build graph and initialize direct prerequisites
        for (const auto& edge : prerequisites) {
            int a = edge[0], b = edge[1];
            adj[a].push_back(b);
            prereq[b] |= 1 << a; // Set the a-th bit for course b
            in_degree[b]++;
        }

        // Topological sort using Kahn's algorithm
        queue<int> q;
        for (int i = 0; i < numCourses; ++i) {
            if (in_degree[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int v : adj[u]) {
                prereq[v] |= prereq[u]; // Merge u's prerequisites into v's
                in_degree[v]--;
                if (in_degree[v] == 0) {
                    q.push(v);
                }
            }
        }

        // Answer queries using bitmask checks
        vector<bool> ans;
        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            ans.push_back((prereq[v] & (1 << u)) != 0);
        }

        return ans;
    }
};


"""