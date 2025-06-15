# Method 1: 

# here we are also checking from each node only.
# but it will in O(n) because after any node is 'seen' then we will skip simply.

# Main thing: "each node has at most one outgoing edge.". 
# This means any node can be part of only one cycle , can't be part of more than one cycle like "2608. Shortest Cycle in a Graph".
# so when we will find any cycle we can remove the extra node which was not the part of cycle.("-")
# only because of that statement we are able to do like this and in o(n).

# time: O(n)

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        self.ans= -1

        def dfs(node):
            if node not in seen:  # if seen then simply skip. we already calculated the cycle for this node before only(in previous iteration)
                # check if node in visiting. if it is, then means cycle
                # cycle length= no of node visited till now in current cycle - distance at which we visited this node
                if node in visiting: 
                    self.ans= max(self.ans, len(visiting)- visiting[node])   # '-' for removing extra node which is not part of cycle.
                # now traverse the adj node of curr node if there is outgoing edge.
                elif edges[node] != -1:
                    visiting[node]= len(visiting)  # distance only
                    # seen.add(node)  # marking here seen will give incorrect ans as we have not fully traversed from the node from which we started.
                    dfs(edges[node])
                    visiting.pop(node)   # now this node won't be in current cycle
                
                seen.add(node)  # means we have completed the traversal from current node. so mark as seen.

        seen= set()
        visiting= {}  # [node: distance]will tell if node is visited in current cycle or not.
                      # if visited then when it is visited(distance from node from which we started dfs). 
                      #just like we detect cycle in directed graph.
        for node in range(len(edges)):
            dfs(node)
        
        return self.ans


# Java
"""

import java.util.*;

public class Solution {
    int ans = -1;
    Map<Integer, Integer> visiting;  // node -> distance
    Set<Integer> seen;
    int[] edges;

    public int longestCycle(int[] edges) {
        this.edges = edges;
        visiting = new HashMap<>();
        seen = new HashSet<>();

        for (int node = 0; node < edges.length; node++) {
            dfs(node);
        }

        return ans;
    }

    void dfs(int node) {
        // if seen then simply skip. we already calculated the cycle for this node before only (in previous iteration)
        if (!seen.contains(node)) {
            // check if node in visiting. if it is, then means cycle
            // cycle length = no of node visited till now in current cycle - distance at which we visited this node
            if (visiting.containsKey(node)) {
                ans = Math.max(ans, visiting.size() - visiting.get(node));  // '-' for removing extra node which is not part of cycle
            }
            // now traverse the adj node of current node if there is outgoing edge
            else if (edges[node] != -1) {
                visiting.put(node, visiting.size());  // distance only
                // seen.add(node); // marking here seen will give incorrect ans as we have not fully traversed from the node from which we started
                dfs(edges[node]);
                visiting.remove(node);  // now this node won't be in current cycle
            }

            seen.add(node);  // means we have completed the traversal from current node. so mark as seen
        }
    }
}
"""


# C++
"""
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int ans = -1;
    unordered_map<int, int> visiting; // node -> distance
    unordered_set<int> seen;
    vector<int> edges;

    int longestCycle(vector<int>& edges) {
        this->edges = edges;

        for (int node = 0; node < edges.size(); ++node) {
            dfs(node);
        }

        return ans;
    }

    void dfs(int node) {
        // if seen then simply skip. we already calculated the cycle for this node before only (in previous iteration)
        if (!seen.count(node)) {
            // check if node in visiting. if it is, then means cycle
            // cycle length = no of node visited till now in current cycle - distance at which we visited this node
            if (visiting.count(node)) {
                ans = max(ans, (int)visiting.size() - visiting[node]);  // '-' for removing extra node which is not part of cycle
            }
            // now traverse the adj node of current node if there is outgoing edge
            else if (edges[node] != -1) {
                visiting[node] = visiting.size(); // distance only
                // seen.insert(node); // marking here seen will give incorrect ans as we have not fully traversed from the node from which we started
                dfs(edges[node]);
                visiting.erase(node); // now this node won't be in current cycle
            }

            seen.insert(node);  // means we have completed the traversal from current node. so mark as seen
        }
    }
};
"""