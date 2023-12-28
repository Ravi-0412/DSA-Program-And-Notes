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
    