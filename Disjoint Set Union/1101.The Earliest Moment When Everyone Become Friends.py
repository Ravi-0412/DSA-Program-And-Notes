# method 1: 

# Read this carefully:
# 'person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B'.

# In simple word, it means a person 'A' can know other person 'B' if 'A' is friend of 'B' or
# 'A' knows someone who is friend of 'B'.

# This is recursive statement in itself when you will draw on paper.

# note: we have to find minimum cost to connect all people.
# i.e from all possible path take the maximum time and that will be answer. 

# Other way to ask this question is: "find the max edge cost from a MST".
# Just 'MST' logic only. Here no need to add just take maximum of all edge weight.

import heapq
from collections import defaultdict
def minTime(logs, n):
    if len(logs) < n -1:  # we need at least 'n-1' edge to connect 'n' nodes
        return -1
    edges = defaultdict(list)
    for w, u, v in logs:
        edges[u].append((v, w))
        edges[v].append((u, w))
    visited = set()
    min_time = 0
    min_heap = [(0,0)]  # we can start from any node. strarted with smallest one
    # Here changed from 'while len(visited) < n'. Because all may be not connected also.
    while min_heap:  
        w1,n1= heapq.heappop(min_heap)
        if n1 in visited:  
            continue
        visited.add(n1)
        min_time = max(min_time, w1)  # taking max of all edge weight
        for n2,w2 in edges[n1]:
            if n2 not in visited:
                heapq.heappush(min_heap,(w2, n2))
        
    return min_time if len(visited)== n else -1


# Java
"""
import java.util.*;

public class Solution {
    public int minTime(int[][] logs, int n) {
        if (logs.length < n - 1)  // we need at least 'n-1' edge to connect 'n' nodes
            return -1;

        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int[] log : logs) {
            int w = log[0], u = log[1], v = log[2];
            edges.computeIfAbsent(u, k -> new ArrayList<>()).add(new int[]{v, w});
            edges.computeIfAbsent(v, k -> new ArrayList<>()).add(new int[]{u, w});
        }

        Set<Integer> visited = new HashSet<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        int minTime = 0;
        minHeap.offer(new int[]{0, 0});  // we can start from any node. started with smallest one

        // Here changed from 'while visited.size() < n'. Because all may be not connected also.
        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int w1 = top[0], n1 = top[1];
            if (visited.contains(n1)) continue;

            visited.add(n1);
            minTime = Math.max(minTime, w1);  // taking max of all edge weight

            for (int[] neighbor : edges.getOrDefault(n1, new ArrayList<>())) {
                int n2 = neighbor[0], w2 = neighbor[1];
                if (!visited.contains(n2)) {
                    minHeap.offer(new int[]{w2, n2});
                }
            }
        }

        return visited.size() == n ? minTime : -1;
    }
}

"""

# C++
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minTime(vector<vector<int>>& logs, int n) {
        if (logs.size() < n - 1)  // we need at least 'n-1' edge to connect 'n' nodes
            return -1;

        unordered_map<int, vector<pair<int, int>>> edges;
        for (auto& log : logs) {
            int w = log[0], u = log[1], v = log[2];
            edges[u].emplace_back(v, w);
            edges[v].emplace_back(u, w);
        }

        unordered_set<int> visited;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
        int minTime = 0;
        minHeap.push({0, 0});  // we can start from any node. started with smallest one

        // Here changed from 'while visited.size() < n'. Because all may be not connected also.
        while (!minHeap.empty()) {
            auto [w1, n1] = minHeap.top(); minHeap.pop();
            if (visited.count(n1)) continue;

            visited.insert(n1);
            minTime = max(minTime, w1);  // taking max of all edge weight

            for (auto& [n2, w2] : edges[n1]) {
                if (!visited.count(n2)) {
                    minHeap.push({w2, n2});
                }
            }
        }

        return visited.size() == n ? minTime : -1;
    }
};
"""



# Method 2:
# Logic: when we see problems related to connectivity, we should think of applying DSU. 
# This problem asks us to find the first instance where the graph formed by friendships is connected. 
# To accomplish this, we'll first sort the friendships by timestamp

# If for one log, the two people belong to different groups, then merge the people of the two groups into one group
# and keep decreasing '1'.
# Once 'n' becomes 1, everyone becomes friends, so return the timestamp.

# Time: m*logm (m= len(logs))

import heapq
from collections import defaultdict
def minTime(logs, n):
    
    parent = [i for i in range(n)]  # list(range(n))
    size =   [1 for i in range(n)]

    def findParent(x):
        if x == parent[x]:
            return x
        parent[x] = findParent(parent[x])
        return parent[x]
    
    def unionBySize(n1, n2):
        p1, p2= findParent(n1), findParent(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return False
        if size[p1] < size[p2]:
            parent[p1]= p2  
            size[p2]+= size[p1]   
        else :   # rank[p1]>= rank[p2]
            parent[p2]= p1   
            size[p1]+= size[p2]
        return True
    
    logs.sort()
    print(logs)
    for w, u, v in logs:
        if unionBySize(u, v):
            n -= 1
            if n== 1:
                return w
    return -1

# logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]] 
# N = 6

# logs = [[2,0,1],[3,1,2],[4,2,3]]
# N = 4

logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
N = 4
print(minTime(logs, N))


# Java
"""
import java.util.*;

public class Solution {
    public int minTime(int[][] logs, int n) {
        int[] parent = new int[n];
        int[] size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        Arrays.sort(logs, Comparator.comparingInt(a -> a[0]));
        // System.out.println(Arrays.deepToString(logs));

        for (int[] log : logs) {
            int w = log[0], u = log[1], v = log[2];
            if (unionBySize(u, v, parent, size)) {
                n -= 1;
                if (n == 1) {
                    return w;
                }
            }
        }
        return -1;
    }

    private int findParent(int x, int[] parent) {
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x], parent);  // Path compression
    }

    private boolean unionBySize(int u, int v, int[] parent, int[] size) {
        int pu = findParent(u, parent);
        int pv = findParent(v, parent);
        if (pu == pv) return false;  // we can't do union since they belong to the same component

        if (size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        return true;
    }
}

"""


# C++
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minTime(vector<vector<int>>& logs, int n) {
        vector<int> parent(n), size(n, 1);
        for (int i = 0; i < n; ++i) parent[i] = i;

        sort(logs.begin(), logs.end());
        // for (auto& log : logs) cout << log[0] << "," << log[1] << "," << log[2] << "\n";

        for (auto& log : logs) {
            int w = log[0], u = log[1], v = log[2];
            if (unionBySize(u, v, parent, size)) {
                n -= 1;
                if (n == 1) return w;
            }
        }
        return -1;
    }

private:
    int findParent(int x, vector<int>& parent) {
        if (x == parent[x]) return x;
        return parent[x] = findParent(parent[x], parent);  // Path compression
    }

    bool unionBySize(int u, int v, vector<int>& parent, vector<int>& size) {
        int pu = findParent(u, parent);
        int pv = findParent(v, parent);
        if (pu == pv) return false;  // we can't do union since they belong to the same component

        if (size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        return true;
    }
};


"""