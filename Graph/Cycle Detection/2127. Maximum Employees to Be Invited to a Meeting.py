# Logic:
"""
1. Large Cycles (Size >2)
Example:
A → B → C → A (cycle of 3)
Explanation:

Each person must sit next to their favorite.
Seating: A next to B, B next to C, C next to A (circular).
All 3 can attend.
Result:
Maximum invitations = cycle length (3).

2. Mutual Pairs (Cycle of 2) with Chains
Example:
A ↔ B (mutual favorites), with chains:
C → A and D → E → B
Explanation:

A and B sit together.
Chain C → A adds 1 person (C sits next to A).
Chain D → E → B adds 2 people (D next to E, E next to B).
Seating: C-A-B-E-D (circular).
Result:
Total = 2 (pair) + 1 (C) + 2 (D,E) = 5.

Q) Why Cycle Length 2 is Special
Mutual pairs (A ↔ B) allow combining two independent chains.
Larger cycles (like A→B→C→A) can't add external people—every seat is already taken by cycle members.

Link: https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/solutions/6329874/scenario-analysis-topological-sorting-cycle-detection-with-example/?envType=daily-question&envId=Invalid%20Date
"""

# Time: O(n)

from collections import deque

class Solution(object):
    def maximumInvitations(self, favorite):
        n = len(favorite)
        in_deg = [0] * n
        chain_len = [0] * n
        visited = [False] * n
        q = deque()
        
        # Count how many people favor each employee
        for f in favorite:
            in_deg[f] += 1
        
        # Start with employees no one favorites (chain starters)
        for i in range(n):
            if in_deg[i] == 0:
                q.append(i)
        
        # Process chains to calculate max chain lengths
        while q:
            u = q.popleft()
            visited[u] = True
            v = favorite[u]
            chain_len[v] = max(chain_len[v], chain_len[u] + 1)
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)
              
        # print(chain_len, "chain_len", in_deg)
        max_cycle, pair_chains = 0, 0
        
        # Detect cycles and calculate results
        for i in range(n):
            if visited[i]:
                continue
            cycle_len = 0
            current = i
            # Measure cycle length
            while not visited[current]:
                visited[current] = True
                current = favorite[current]
                cycle_len += 1
            if cycle_len == 2:  # Mutual pair
                # print(i, chain_len[i],chain_len[favorite[i]])
                pair_chains += 2 + chain_len[i] + chain_len[favorite[i]]
            else:
                max_cycle = max(max_cycle, cycle_len)
        
        return max(max_cycle, pair_chains)
