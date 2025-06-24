# Brute force
# Just check maximum possible length from each node.

# Note: Here making adjacency list like undirected graph.

# Time : O(n^2)

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = collections.defaultdict(list)
        for i , par in enumerate(parent):
            if i == 0:
                continue
            adj[par].append(i)
            adj[i].append(par)

        def dfs(node):
            visited.add(node)
            # Take max of all its adjacent node and add '1'.
            ans = 1
            for nei in adj[node]:
                if nei not in visited and s[node] != s[nei]:
                    ans = max(ans, 1 + dfs(nei))
            return ans

        n = len(parent)
        visited = set()
        res = 0
        for i in range(n):
            res = max(res, dfs(i))
            # print(res, i, "res")
            visited.clear()
        return res

# Java Code 
"""
import java.util.*;

class Solution {
    public int longestPath(int[] parent, String s) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 1; i < parent.length; i++) {
            adj.computeIfAbsent(parent[i], k -> new ArrayList<>()).add(i);
            adj.computeIfAbsent(i, k -> new ArrayList<>()).add(parent[i]);
        }

        Set<Integer> visited = new HashSet<>();
        int res = 0;
        for (int i = 0; i < parent.length; i++) {
            res = Math.max(res, dfs(i, adj, s, visited));
            visited.clear();
        }
        return res;
    }

    private int dfs(int node, Map<Integer, List<Integer>> adj, String s, Set<Integer> visited) {
        visited.add(node);
        // Take max of all its adjacent node and add '1'.
        int ans = 1;
        for (int nei : adj.getOrDefault(node, new ArrayList<>())) {
            if (!visited.contains(nei) && s.charAt(node) != s.charAt(nei)) {
                ans = Math.max(ans, 1 + dfs(nei, adj, s, visited));
            }
        }
        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestPath(vector<int>& parent, string s) {
        unordered_map<int, vector<int>> adj;
        for (int i = 1; i < parent.size(); ++i) {
            adj[parent[i]].push_back(i);
            adj[i].push_back(parent[i]);
        }

        unordered_set<int> visited;
        int res = 0;
        for (int i = 0; i < parent.size(); ++i) {
            res = max(res, dfs(i, adj, s, visited));
            visited.clear();
        }
        return res;
    }

    int dfs(int node, unordered_map<int, vector<int>>& adj, const string& s, unordered_set<int>& visited) {
        visited.insert(node);
        // Take max of all its adjacent node and add '1'.
        int ans = 1;
        for (int nei : adj[node]) {
            if (!visited.count(nei) && s[node] != s[nei]) {
                ans = max(ans, 1 + dfs(nei, adj, s, visited));
            }
        }
        return ans;
    }
};
"""

# Optimising to O(n)

"""
Just an extension of "543. Diameter of Binary Tree".
Only differnce one node can have more than 2 children.

Logic: In a generic tree there are more than 2 nodes however 
the longest path, can only be found from 2 of the longest paths for each node.

So for each node, keep track of 2 longest path going through that node 
then ans for that node = best + second_best + 1.

Implementation is similar to ""543. Diameter of Binary Tree".

Note: Here we are making directed graph and after finding ans for children , forwarding that to parent & so on.

Time = O(n)
"""

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = collections.defaultdict(list)
        for i , par in enumerate(parent):
            if i == 0:
                continue
            adj[par].append(i)
            # adj[i].append(par)
        
        self.ans = 1

        # dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
        def dfs(node):
            # We want to keep track of the 2 longest paths starting from this node,
            # So that we can compute the longest path going through this node 
            # in the sub-tree rooted at this node.
            best , second_best = 0, 0   # these will come from all possible children
            for nei in adj[node]:
                length = dfs(nei)
                if s[node] != s[nei]:
                    # length = dfs(nei)  # writing here will wrong ans because if characters are same 
                    # then, function call will never happen for 'nei' node but we can get the maximum ans starting from 'nei' node also.
                    # update best and second_best
                    if length > best:
                        second_best = best
                        best = length
                    elif length > second_best:
                        second_best = length
            
            # Update ans
            # best + second_best + 1 means the length of the longest valid path 
            # going through this node in the sub-tree rooted at this node.
            self.ans = max(self.ans, best + second_best + 1)  # '1' for cur node
            # But it will return only one length i.e maximum possible one. Parent can only take one of the path so take best one
            return best + 1

        dfs(0)
        return self.ans

# Java Code 
"""
import java.util.*;

class Solution {
    int ans = 1;

    public int longestPath(int[] parent, String s) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 1; i < parent.length; i++) {
            adj.computeIfAbsent(parent[i], k -> new ArrayList<>()).add(i);
            // adj.computeIfAbsent(i, k -> new ArrayList<>()).add(parent[i]);
        }

        dfs(0, adj, s);
        return ans;
    }

    // dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
    private int dfs(int node, Map<Integer, List<Integer>> adj, String s) {
        // We want to keep track of the 2 longest paths starting from this node,
        // So that we can compute the longest path going through this node
        // in the sub-tree rooted at this node.
        int best = 0, secondBest = 0;

        for (int nei : adj.getOrDefault(node, new ArrayList<>())) {
            int length = dfs(nei, adj, s);
            if (s.charAt(node) != s.charAt(nei)) {
                // update best and secondBest
                if (length > best) {
                    secondBest = best;
                    best = length;
                } else if (length > secondBest) {
                    secondBest = length;
                }
            }
        }

        // Update ans
        // best + secondBest + 1 means the length of the longest valid path
        // going through this node in the sub-tree rooted at this node.
        ans = Math.max(ans, best + secondBest + 1);
        // Parent can only take one of the path so take best one
        return best + 1;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
using namespace std;

class Solution {
public:
    int ans = 1;

    int longestPath(vector<int>& parent, string s) {
        unordered_map<int, vector<int>> adj;
        for (int i = 1; i < parent.size(); ++i) {
            adj[parent[i]].push_back(i);
            // adj[i].push_back(parent[i]);
        }

        dfs(0, adj, s);
        return ans;
    }

    // dfs will return the longest valid path starting from this node in the sub-tree rooted at this node.
    int dfs(int node, unordered_map<int, vector<int>>& adj, const string& s) {
        // We want to keep track of the 2 longest paths starting from this node,
        // So that we can compute the longest path going through this node
        // in the sub-tree rooted at this node.
        int best = 0, secondBest = 0;

        for (int nei : adj[node]) {
            int length = dfs(nei, adj, s);
            if (s[node] != s[nei]) {
                // update best and secondBest
                if (length > best) {
                    secondBest = best;
                    best = length;
                } else if (length > secondBest) {
                    secondBest = length;
                }
            }
        }

        // Update ans
        // best + secondBest + 1 means the length of the longest valid path
        // going through this node in the sub-tree rooted at this node.
        ans = max(ans, best + secondBest + 1);
        // Parent can only take one of the path so take best one
        return best + 1;
    }
};
"""