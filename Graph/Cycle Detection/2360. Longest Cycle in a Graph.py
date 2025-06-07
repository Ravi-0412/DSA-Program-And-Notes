"""
Core logic
- Each node has at most one outgoing edge.
- So, a node can be part of only one cycle, not multiple.
- Once a node is visited, we don’t need to check it again.

Step by step working
- From each unvisited node, follow the path until:
  - You hit a visited node → check if it’s a cycle.
  - Or reach a dead end.
- Use a `seen[]` array to skip nodes already checked.

Time Complexity: O(n)

"""

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

Java Code
"""
class Solution {
    int ans = -1;

    public int longestCycle(int[] edges) {
        Set<Integer> seen = new HashSet<>();
        Map<Integer, Integer> visiting = new HashMap<>();

        for (int i = 0; i < edges.length; i++) {
            dfs(i, edges, seen, visiting, 0);
        }

        return ans;
    }

    private void dfs(int node, int[] edges, Set<Integer> seen, Map<Integer, Integer> visiting, int depth) {
        if (seen.contains(node)) return;

        if (visiting.containsKey(node)) {
            ans = Math.max(ans, depth - visiting.get(node));
        } else if (edges[node] != -1) {
            visiting.put(node, depth);
            dfs(edges[node], edges, seen, visiting, depth + 1);
            visiting.remove(node);
        }

        seen.add(node);
    }
}
"""

C++ Code
"""
class Solution {
public:
    int ans = -1;

    void dfs(int node, vector<int>& edges, unordered_set<int>& seen, unordered_map<int, int>& visiting, int depth) {
        if (seen.count(node)) return;

        if (visiting.count(node)) {
            ans = max(ans, depth - visiting[node]);
        } else if (edges[node] != -1) {
            visiting[node] = depth;
            dfs(edges[node], edges, seen, visiting, depth + 1);
            visiting.erase(node);
        }

        seen.insert(node);
    }

    int longestCycle(vector<int>& edges) {
        unordered_set<int> seen;
        unordered_map<int, int> visiting;

        for (int i = 0; i < edges.size(); ++i) {
            dfs(i, edges, seen, visiting, 0);
        }

        return ans;
    }
};

"""
