# Method 2:
"""
logic: just simple bfs to find the cost from src to destination.
Difficult part to think how we can do by graph.

expalanation:
Given:
a/b = 2.0, b/c = 3.0
We can build a directed graph:
a --> 2.0 --> b -- 3.0 --> c
If we were asked to find a/c, we have:
a/c = a/b * b/c = 2.0 * 3.0
In the graph, it is the product of costs of edges.

Do notice that, 2 edges need to added into the graph with one given equation,
because with a/b we also get result of b/a, which is the reciprocal of a/b.
in short using reciprocal we can also get ans .

e.g: If asked to find 'c/a' then reciprocal will only help.
c -- 0.333 --> b -- 0.5 --> a

how to do?
FOr each query [a, b], run a bfs starting from 'a' and keep multiplying the edges that is adjacent 
And once you reach 'b', return ans. (a and b can be equal also)

time: n * (E+ V), n= len(queries)
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj= collections.defaultdict(list)
        # form adjacency list (directed graph with values for that eqn)
        for i, eq in enumerate(equations):
            a, b= eq
            adj[a].append((b, values[i]))  # 'a/b' = values[i]
            adj[b].append((a, 1 / values[i]))  # for reverse value will also reverse. 'b/a' = 1/values[i]
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            q= collections.deque()
            visited= set()   # we are adding reverse also so there will be cycle . so take visited.
            q.append((src, 1))   # [variable, values_till_now]
            visited.add(src)
            while q:
                a, w= q.popleft()
                if a== target:
                    return w
                for nei, weight in adj[a]:
                    if nei not in visited:
                        q.append((nei, w *weight))
                        visited.add(nei)
            # Both src and destination is present but there is no way we can find src/target.
            return -1
        
        ans= []
        for q in queries:
            curAns= bfs(q[0], q[1])
            ans.append(curAns)
        return ans

# Java
"""
import java.util.*;

public class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // Adjacency list to represent the graph
        Map<String, List<Pair>> graph = new HashMap<>();

        // Build the graph: for each equation a / b = val, also store b / a = 1/val
        for (int i = 0; i < equations.size(); i++) {
            List<String> eq = equations.get(i);
            String a = eq.get(0), b = eq.get(1);
            double val = values[i];

            graph.putIfAbsent(a, new ArrayList<>());
            graph.putIfAbsent(b, new ArrayList<>());

            graph.get(a).add(new Pair(b, val));       // a -> b with weight val
            graph.get(b).add(new Pair(a, 1.0 / val)); // b -> a with weight 1/val
        }

        // Prepare result array
        double[] results = new double[queries.size()];

        // Process each query using BFS
        for (int i = 0; i < queries.size(); i++) {
            String src = queries.get(i).get(0);
            String dest = queries.get(i).get(1);
            results[i] = bfs(src, dest, graph);
        }

        return results;
    }

    // Helper function to perform BFS
    private double bfs(String src, String dest, Map<String, List<Pair>> graph) {
        if (!graph.containsKey(src) || !graph.containsKey(dest)) {
            return -1.0;
        }

        Queue<Pair> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.offer(new Pair(src, 1.0));
        visited.add(src);

        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            String node = current.variable;
            double valueSoFar = current.value;

            if (node.equals(dest)) {
                return valueSoFar;
            }

            for (Pair neighbor : graph.get(node)) {
                if (!visited.contains(neighbor.variable)) {
                    visited.add(neighbor.variable);
                    queue.offer(new Pair(neighbor.variable, valueSoFar * neighbor.value));
                }
            }
        }

        // If no path was found
        return -1.0;
    }

    // Helper class to store pairs of (variable, value)
    static class Pair {
        String variable;
        double value;

        Pair(String variable, double value) {
            this.variable = variable;
            this.value = value;
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        // form adjacency list (directed graph with values for that eqn)
        unordered_map<string, vector<pair<string, double>>> adj;
        for (int i = 0; i < (int)equations.size(); i++) {
            string a = equations[i][0], b = equations[i][1];
            adj[a].push_back({b, values[i]});          // 'a/b' = values[i]
            adj[b].push_back({a, 1.0 / values[i]});    // reverse value: 'b/a' = 1/values[i]
        }

        auto bfs = [&](string src, string target) -> double {
            if (adj.find(src) == adj.end() || adj.find(target) == adj.end()) {
                return -1.0;
            }
            queue<pair<string, double>> q;
            unordered_set<string> visited;   // visited to avoid cycles
            q.push({src, 1.0});              // [variable, values_till_now]
            visited.insert(src);

            while (!q.empty()) {
                auto [a, w] = q.front(); q.pop();
                if (a == target) {
                    return w;
                }
                for (auto& [nei, weight] : adj[a]) {
                    if (visited.find(nei) == visited.end()) {
                        q.push({nei, w * weight});
                        visited.insert(nei);
                    }
                }
            }
            // Both src and destination are present but no path found
            return -1.0;
        };

        vector<double> ans;
        for (auto& q : queries) {
            ans.push_back(bfs(q[0], q[1]));
        }
        return ans;
    }
};

"""

"""
Follow ups: What if you have 10 million queries and only 1,000 equations? How would you optimize?
BFS will be too slow.

for better understanding:
"""
Imagine three people with different heights: Alice (A), Bob (B), and Chris (C).

Equation 1: 
A/B =2.0 (Alice is twice Bob’s height)

Equation 2: 
B/C=3.0 (Bob is three times Chris’s height)

The Union-Find structure forms a chain: 
𝐴→𝐵→𝐶
parent[A] = B, weights[A] = 2.0  
parent[B] = C, weights[B] = 3.0  
parent[C] = C, weights[C] = 1.0   # C is the root

When find(A) is called, the goal is to compress the path so Alice points directly to Chris and we know 
A/C immediately.

Step 1: Recursion
find(A) calls find(B) because A’s parent is B.

Step 2: Resolve B
find(B) sees that C is the root and returns (C, 3.0), meaning 
B/C=3.0.

Step 3: Update Alice’s weight
Now for Alice:

existing 
A/B=2.0

received factor 
B/C=3.0

Update:
A/C=(A/B)×(B/C)=2.0×3.0=6.0

So weights[A] becomes 6.0.

Step 4: Path compression
Set parent[A] = C. Now Alice points directly to the root, and we instantly know 
A/C=6.0.
"""

1. Core Data Structures

self.parent: Tracks the parent of each node. Initially, every node is its own parent (each node is its own root).

self.weights: Stores the ratio between a node and its parent.
Specifically, weights[A] represents the value of : 𝐴 / parent[𝐴]​

If parent[A] = B and weights[A] = 2.0, it means:

𝐴 = 2.0 × 𝐵

2. find(i) — Path Compression

This function does two things:

finds the ultimate root

flattens the tree for faster future queries

Example chain: 
A→B→C
A/B=2.0⇒weights[A]=2.0
B/C=3.0⇒weights[B]=3.0

When you call find(A):

It recursively calls find(B).

find(B) discovers that 
C is the root and returns (C,3.0).

Back in find(A), we compress the path so A points directly to C.

Weight update math
A=2.0×B,B=3.0×C
A=(2.0×3.0)×C=6.0×C

So we set:

parent[A] = C
weights[A] = 6.0

3. union(i, j, value) — Merging Sets
This adds a new equation A/B=value.
If A and B belong to different roots, we connect:
root 𝐴 →root 𝐵
We know:
𝐴 = weight 𝐴 × root 𝐴
B = weight B × root B​
𝐴 =value × 𝐵

Substitute:
weight A * root A = value * (weight B * root B)

Solve for the ratio between roots: root 𝐴 / root B
root 𝐴 / root B = (value * weight B) / weight A
That’s exactly what the code sets: 
weights[root_A] = value * weight_B / weight_A
parent[root_A] = root_B

4. calcEquation Query

To compute 𝐶 / 𝐷 :
Find root and weight of C
𝐶 = 𝑊eight C * root C
Find root and weight of D
D = 𝑊eight D * root D​​

If roots differ: → not connected → return −1.0

If roots are the same:
C/ D = (weight C * root) / (weight D * root) = weight C / weight D​

This gives the final answer.

Complexity Analysis:
Time Complexity: O((N + M) * alpha(V))
Preprocessing: O(N *alpha(V)), where alpha is the Inverse Ackermann function (effectively constant).
Query: O(M * alpha(V)). For M queries, this is significantly faster than BFS (M * V).

Space Complexity: O(V) to store the parent and weight mappings.
"""

class UnionFind:
    def __init__(self, variables: set[str]):
        # Every node is its own parent initially (a forest of single-node trees)
        self.parent = {v: v for v in variables}
        # weights[i] stores the ratio: i / parent[i]
        # Since parent[i] is i, i/i is always 1.0
        self.weights = {v: 1.0 for v in variables}

    def find(self, i: str) -> tuple[str, float]:
        """
        Finds the root of node 'i' and applies path compression.
        Returns: (root_name, ratio_of_i_to_root)
        """
        if self.parent[i] == i:
            return i, 1.0
        
        # Path compression: recursively find the ultimate root
        root, parent_to_root_ratio = self.find(self.parent[i])
        
        # Update current node's parent to the ultimate root (flattening the tree)
        self.parent[i] = root
        
        # Update weight: (i / old_parent) * (old_parent / root) = i / root
        self.weights[i] *= parent_to_root_ratio
        
        return self.parent[i], self.weights[i]

    def union(self, i: str, j: str, value: float):
        """Connects i and j such that i / j = value."""
        root_i, weight_i = self.find(i)
        root_j, weight_j = self.find(j)
        
        if root_i != root_j:
            """
            Connect root_i to root_j
            i / root_i = weight_i  => root_i = i / weight_i --  (i)
            j / root_j = weight_j  => root_j = j / weight_j --- (ii)
            given: i / j = value ----- (iii)
            we want : root_i / root_j  = ?  why : because we are making root_j parent of root_i & according to definition of weight we need to get root_i / root_j
            putting (i), (ii) in (iii), we get : 
            (root_i * weight_i) / (root_j * weight_j) = value
            root_i / root_j = value * weight_j / weight_i
            """
            self.parent[root_i] = root_j
            self.weights[root_i] = value * weight_j / weight_i
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # 1. Collect all unique variables to initialize Union-Find upfront
        variables = set()
        for dividend, divisor in equations:
            variables.add(dividend)
            variables.add(divisor)
            
        uf = UnionFind(variables)
        
        # 2. Build the relationship graph (Union operations)
        for i in range(len(equations)):
            dividend, divisor = equations[i]
            ratio_value = values[i]
            uf.union(dividend, divisor, ratio_value)
            
        # 3. Process queries
        results = []
        for query_dividend, query_divisor in queries:
            # Case 1: Variable never seen before
            if query_dividend not in variables or query_divisor not in variables:
                results.append(-1.0)
                continue
            
            root_a, ratio_a_to_root = uf.find(query_dividend)
            root_b, ratio_b_to_root = uf.find(query_divisor)
            
            # Case 2: Variables are not connected (different roots)
            if root_a != root_b:
                results.append(-1.0)
            else:
                # Case 3: Calculate ratio via common root
                # (a / root) / (b / root) = a / b
                results.append(ratio_a_to_root / ratio_b_to_root)
                
        return results
