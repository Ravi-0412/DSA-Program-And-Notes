"""
We can get minimum from indirect conversion also : a -> any_between_char -> b 
It just we have to find the smallest cost for each char conversion , and for these optimal Algo is: Brute force
step: 1) Find the cost of conversion for each other to other character.
For this we can use Floydd warshall Algorithm.

2) After that go through source and target and if we can convert each char of source to target 
and keep adding cost.

Time complexity: O(N + E + V^3) , E = 2000, V = 26
Space : O(V^2) 
"""

class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Optimal approach using Floyd-Warshall for All-Pairs Shortest Path.
        Time Complexity: O(N + V^3) where N is string length and V is alphabet size (26).
        Space Complexity: O(V^2) for the distance matrix.
        """
        # 1. Initialize distance matrix with infinity
        # dist[i][j] will store the min cost to change char i to char j
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # Distance to self is always 0
        for i in range(26):
            dist[i][i] = 0
            
        # 2. Fill initial edges from given transformations
        for u, v, w in zip(original, changed, cost):
            u_idx = ord(u) - ord('a')
            v_idx = ord(v) - ord('a')
            # If multiple transformations exist for the same pair, take the minimum
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], w)
            
        # 3. Floyd-Warshall Algorithm: O(V^3)
        # Try every character 'k' as an intermediate step between 'i' and 'j'
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                        
        # 4. Calculate total cost for the source to target conversion
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            
            s_idx = ord(s) - ord('a')
            t_idx = ord(t) - ord('a')
            
            curr_cost = dist[s_idx][t_idx]
            if curr_cost == inf:
                return -1 # Transformation impossible
            
            total_cost += curr_cost
            
        return total_cost
    
# follow ups:
"""
1. "What if the character set was Unicode (thousands of characters)?"
-> Floyd-Warshall ($V^3$) would become too slow. In that case, you would use Dijkstra only for the characters that actually appear in the source and target strings. 
You would also use an adjacency list instead of a matrix.
"""
