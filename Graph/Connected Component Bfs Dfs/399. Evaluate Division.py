# Method 1: 

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
        visited.add(src);    // we are adding reverse also so there will be cycle . so take visited.

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
            unordered_set<string> visited;   // we are adding reverse also so there will be cycle . so take visited.
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

