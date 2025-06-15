# Method : 1

# step: 1) Find the cost of conversion for each other to other character.
# For this we can use Floydd warshall Algorithm.

# 2) After that go through source and target and if we can convert each char of source to target 
# and keep adding cost.

# Time complexity: O(n^3)
#  where 'n' is the number of unique characters that can exist in our string. 
# Since we only use lowercase english characters this is just O(26^3).


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dist = [ [inf for _ in range(26)] for _ in range(26) ]
		# zero cost to "change" a char to itself
        for i in range(26):
            dist[i][i] = 0
        for uc, vc, w in zip(original, changed, cost):
            u = ord(uc) - ord("a")
            v = ord(vc) - ord("a")
            dist[u][v] = min(dist[u][v], w)
        
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
					# shortest path from i to j is the minimum between i to j or 
					# i to k AND then going k to j
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        n = len(source)
        res = 0
        for i in range(n):
            u = ord(source[i]) - ord('a')
            v = ord(target[i]) - ord('a')
			# attempt to match chars
            if dist[u][v] == inf:
                return -1
            res += dist[u][v]
        return res


# java
"""
import java.util.*;

class Solution {
    public int minimumCost(String source, String target, List<String> original, List<String> changed, List<Integer> cost) {
        int[][] dist = new int[26][26];
        int inf = Integer.MAX_VALUE / 2;

        // initialize with infinity
        for (int i = 0; i < 26; i++) {
            Arrays.fill(dist[i], inf);
        }

        // zero cost to "change" a char to itself
        for (int i = 0; i < 26; i++) {
            dist[i][i] = 0;
        }

        // build the initial direct costs
        for (int i = 0; i < original.size(); i++) {
            int u = original.get(i).charAt(0) - 'a';
            int v = changed.get(i).charAt(0) - 'a';
            dist[u][v] = Math.min(dist[u][v], cost.get(i));
        }

        // Floyd-Warshall for all pairs shortest path
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    // shortest path from i to j is the minimum between i to j or i to k and then k to j
                    if (dist[i][k] < inf && dist[k][j] < inf)
                        dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int n = source.length();
        int res = 0;
        for (int i = 0; i < n; i++) {
            int u = source.charAt(i) - 'a';
            int v = target.charAt(i) - 'a';
            // attempt to match chars
            if (dist[u][v] == inf) {
                return -1;
            }
            res += dist[u][v];
        }
        return res;
    }
}

"""


# C++
"""
#include <iostream>
#include <vector>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        int n = source.length();
        int inf = INT_MAX / 2;
        vector<vector<int>> dist(26, vector<int>(26, inf));

        // zero cost to "change" a char to itself
        for (int i = 0; i < 26; i++) {
            dist[i][i] = 0;
        }

        // build the initial direct costs
        for (int i = 0; i < original.size(); i++) {
            int u = original[i][0] - 'a';
            int v = changed[i][0] - 'a';
            dist[u][v] = min(dist[u][v], cost[i]);
        }

        // Floyd-Warshall for all pairs shortest path
        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    // shortest path from i to j is the minimum between i to j or i to k and then k to j
                    if (dist[i][k] < inf && dist[k][j] < inf)
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
                }
            }
        }

        int res = 0;
        for (int i = 0; i < n; i++) {
            int u = source[i] - 'a';
            int v = target[i] - 'a';
            // attempt to match chars
            if (dist[u][v] == inf) {
                return -1;
            }
            res += dist[u][v];
        }
        return res;
    }
};
"""