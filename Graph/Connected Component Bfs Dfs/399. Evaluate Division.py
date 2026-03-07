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

# Better and easier one than 'Union -find' for follow ups

from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the Graph (Adjacency List)
        # We store both the forward and reciprocal relationships
        graph = defaultdict(list)
        variables = set()
        
        for i, (u, v) in enumerate(equations):
            val = values[i]
            graph[u].append((v, val))      # u / v = val
            graph[v].append((u, 1.0 / val)) # v / u = 1 / val
            variables.add(u)
            variables.add(v)
            
        # Step 2: Pre-compute Roots and Ratios (Star Topology)
        # norm_map stores: { variable: (root_variable, value_relative_to_root) }
        norm_map = {}
        visited = set()
        
        for var in variables:
            if var not in visited:
                # New component (island) found. Pick this 'var' as the Root.
                root = var
                # Queue stores (current_node, current_ratio_to_root)
                # Initial ratio for root is 1.0 because root/root = 1.0
                queue = deque([(root, 1.0)])
                visited.add(root)
                
                while queue:
                    curr, ratio = queue.popleft()
                    norm_map[curr] = (root, ratio)
                    
                    for neighbor, weight in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            # MATH LOGIC:
                            # We want neighbor_ratio = neighbor / root
                            # We know curr_ratio = curr / root
                            # We know weight = curr / neighbor  =>  neighbor = curr / weight
                            # Therefore: neighbor / root = (curr / weight) / root = (curr / root) / weight
                            queue.append((neighbor, ratio / weight))
                            
        # Step 3: Answer Queries in O(1) each
        # This part handles the 10 million queries efficiently
        results = []
        for c, d in queries:
            # Case 1: One or both variables never appeared in equations
            if c not in norm_map or d not in norm_map:
                results.append(-1.0)
            else:
                root_c, ratio_c = norm_map[c]
                root_d, ratio_d = norm_map[d]
                
                # Case 2: Variables are in different "islands" (not convertible)
                if root_c != root_d:
                    results.append(-1.0)
                # Case 3: Variables share a root, return the relative ratio
                else:
                    # (c/root) / (d/root) = c/d
                    results.append(ratio_c / ratio_d)
                    
        return results

# Google asked Exact same Question
"""
Q) Question: You are writing the Google Search unit converter. You are given a list of unit conversion factors and a query. The conversion factor is the value needed to convert from unit A to unit B.
Write a function that takes a list of conversion factors and 2 units (a and b) and outputs the conversion factor from a -> b.

12 inches is 1 foot
(meter, centimeter, 100)

a and b are strings
con_factors is a list of tuples, where each tuple is a (string, string, float)

"""

from collections import defaultdict, deque

class UnitConverter:
    def convert(self, con_factors, start_unit, end_unit):
        # Step 1: Build the Adjacency List (The Graph)
        graph = defaultdict(list)
        
        for u1, u2, factor in con_factors:
            # u1 to u2: multiply by factor
            graph[u1].append((u2, factor))
            # u2 back to u1: divide by factor (1/factor)
            graph[u2].append((u1, 1 / factor))
            
        # If units don't exist in our records at all
        if start_unit not in graph or end_unit not in graph:
            return -1.0

        # Step 2: BFS to find the path from start_unit to end_unit
        # Queue stores (current_node, cumulative_multiplier)
        queue = deque([(start_unit, 1.0)])
        visited = {start_unit}
        
        while queue:
            curr_node, curr_val = queue.popleft()
            
            # Destination reached
            if curr_node == end_unit:
                return curr_val
            
            for neighbor, weight in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    # Accumulate the conversion by multiplying weights
                    queue.append((neighbor, curr_val * weight))
                    
        return -1.0 # No path found

# follow ups 1: Follow ups:
"""
Q) Suppose conversion factors only change 1x a week, but users query the conversion factor function 10000x per second. How could you refactor to make this more efficient?
Pre-computation (The "All-Pairs" Strategy)
Instead of running BFS for every query, you calculate the conversion factor between every possible pair of units within a "connected component"
(e.g., all distance units) and store them in a Matrix or a Nested Hash Map.

Logic: Use the Floyd-Warshall Algorithm or run BFS from every node once a week when the data updates.
1. Weekly Update (rebuild_cache):
        Phase 1: Map out all unique units.
        Phase 2: Initialize a nested dictionary where cache[u1][u2] is the conversion factor.
        Phase 3 (Floyd-Warshall): For every pair of units (i, j), check if there is an intermediate 
        unit k that can connect them.The Formula: i -> j = (i -> k) * (k -> j). 
2. Querying:Simply look up self.cache[a][b]. If it exists, return it. Otherwise, return -1.0.

Complexity Analysis
Query Time: O(1) average case (Hash map lookup).
Pre-computation Time: O(V^3) where V is the number of units.
Space Complexity: O(V^2) to store all possible pair-wise combinations.
"""

class UnitConverterSystem:
    def __init__(self, con_factors):
        # Nested dictionary: self.cache[unit_a][unit_b] = factor
        self.cache = {}
        self.rebuild_cache(con_factors)

    def rebuild_cache(self, factors):
        """
        Runs once a week. 
        Uses Floyd-Warshall logic to find all-pairs conversions.
        """
        new_cache = {}
        
        # Step 1: Identity and Direct Conversions
        for u1, u2, val in factors:
            if u1 not in new_cache: new_cache[u1] = {u1: 1.0}
            if u2 not in new_cache: new_cache[u2] = {u2: 1.0}
            
            new_cache[u1][u2] = float(val)
            new_cache[u2][u1] = 1.0 / float(val)

        # Step 2: The Triple Loop (Transitive Closure)
        # We try to use unit 'k' as a bridge between 'i' and 'j'
        units = list(new_cache.keys())
        for k in units:
            for i in units:
                for j in units:
                    # If i can reach k AND k can reach j
                    if k in new_cache[i] and j in new_cache[k]:
                        # Then i can reach j via k
                        # i -> j = (i -> k) * (k -> j)
                        new_cache[i][j] = new_cache[i][k] * new_cache[k][j]
        
        self.cache = new_cache

    def get_conversion(self, unit_a, unit_b):
        """
        Handles 10,000 queries per second.
        O(1) Time Complexity.
        """
        if unit_a in self.cache and unit_b in self.cache[unit_a]:
            return self.cache[unit_a][unit_b]
        return -1.0

# follow ups 2
"""
"What if the graph is extremely sparse (many units, but few possible conversions)? O(V^2) space might be too much."
Ans : I would use the Base-Unit Normalization (Union-Find style). 
Instead of connecting every unit to every other unit, we pick one Root unit for every category (e.g., "Meter" for length, "Second" for time). 
Every other unit just remembers its relationship to that one root.
Space becomes O(V), 
and queries are still O(1) because you just divide two pre-calculated 'ratio-to-root' values."
Note : In a system with 10,000 units, Floyd-Warshall creates a matrix of 100,000,000 entries. Normalization only stores 10,000 entries.

To convert A to B:
        Find A's value relative to Root (A_ratio).  => A = ratioA * Root   - (i)
        Find B's value relative to Root (B_ratio).  => B = ratioB * Root   - (ii)
        The Math: A / B = (A / Root) / (B / Root)   = ratioA / ratioB

Build Time (Weekly): O(V + E) where V is units and E is factors. 
This is much faster than Floyd-Warshall's O(V^3).
Query Time: O(1).
Space: O(V) to store the conversion_map.
"""

from collections import defaultdict, deque

class EfficientConverter:
    def __init__(self, con_factors):
        # self.conversion_map stores: { unit: (root_name, ratio_to_root) }
        # Example: { "cm": ("meter", 0.01), "km": ("meter", 1000) }
        self.conversion_map = self.precompute_base_units(con_factors)

    def precompute_base_units(self, factors):
        # 1. Build a standard adjacency list first
        graph = defaultdict(list)
        all_units = set()  # Collect every single unique unit name from the input tuples
        for u1, u2, val in factors:
            graph[u1].append((u2, val))
            graph[u2].append((u1, 1.0 / val))
            all_units.update([u1, u2])   # add these two units if not present. set operations

        results = {}
        visited = set()

        # 2. Traverse every connected component, master list
        for unit in all_units:
            # If we haven't seen this unit during a previous BFS, 
            # it must be the start of a brand new category (like 'Time' or 'Mass')
            if unit not in visited:
                # We start a new BFS and pick this unit as the "Root" for its group
                root = unit
                # BFS to normalize everyone in this group to this root
                queue = deque([(root, 1.0)]) # (current_node, ratio_to_root)
                visited.add(root)
                
                while queue:
                    curr, ratio = queue.popleft()
                    results[curr] = (root, ratio) # Store which "category" this unit belongs to and its ratio to that category's root.
                    
                    for neighbor, weight in graph[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            # MATH LOGIC:
                            # We want neighbor_ratio = neighbor / root
                            # We know curr_ratio = curr / root
                            # We know weight = curr / neighbor  =>  neighbor = curr / weight
                            # Therefore: neighbor / root = (curr / weight) / root = (curr / root) / weight
                            queue.append((neighbor, ratio /  weight))
        return results

    def query(self, a, b):
        """
        Calculates conversion in O(1) time.
        """
        # Step 1: Check if units even exist
        if a not in self.conversion_map or b not in self.conversion_map:
            return -1.0
            
        root_a, ratio_a = self.conversion_map[a]
        root_b, ratio_b = self.conversion_map[b]
        
        # Step 2: Ensure they belong to the same category (e.g., both are 'Length')
        if root_a != root_b:
            return -1.0
            
        # Step 3: Return the relative ratio
        # Example: (km/m) / (cm/m) = 1000 / 0.01 = 100,000
        return ratio_a / ratio_b

# Example Usage:
# factors = [("meter", "centimeter", 100), ("kilometer", "meter", 1000)]
# system = EfficientConverter(factors)
# print(system.query("kilometer", "centimeter")) # Output: 100000.0
