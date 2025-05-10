"""
1st thought but it won't work.
If we store inorder in an array say array: inorder then, for query(i, j), we 
will check if index of 'j' > index of 'i' in inorder then ans = True else False.

But it won't work for multiple component and when there will be more than one node at the same level.
"""

# Method 1:

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
        List<Set<Integer>> reachable = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            reachable.add(new HashSet<>());
        }

        // Build direct reachability chains
        for (int[] pre : prerequisites) {
            int u = pre[0];
            int v = pre[1];
            reachable.get(v).add(u);  // 'u' is a prerequisite of 'v'
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
        boolean[][] prereq = new boolean[numCourses][numCourses];
        int[] inDegree = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            adj[i] = new ArrayList<>();
        }
        
        // Build graph and initialize direct prerequisites
        for (int[] edge : prerequisites) {
            int a = edge[0], b = edge[1];
            adj[a].add(b);
            prereq[b][a] = true;  // Direct prerequisite from a to b
            inDegree[b]++;
        }
        
        // Topological sort using Kahn's algorithm
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) q.add(i);
        }
        
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int v : adj[u]) {
                // Merge all prerequisites of u into v
                for (int i = 0; i < numCourses; i++) {
                    if (prereq[u][i]) prereq[v][i] = true;
                }
                if (--inDegree[v] == 0) q.add(v);
            }
        }
        
        // Answer queries using precomputed prerequisites
        List<Boolean> ans = new ArrayList<>();
        for (int[] query : queries) {
            int u = query[0], v = query[1];
            ans.add(prereq[v][u]);
        }
        return ans;
    }
}
"""

