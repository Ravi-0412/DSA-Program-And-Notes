# Submitted on Lintcode

# Note: Have a lot of corner cases.

# Logic: If we see 'seqs' then for each 'seq' inside this
# Order should follow i.e seq[i] must come before seq[i + 1].

# from here we get idea of topological sort.

# And there should be only possible choice at a time otherwise we will get more than one ans also.
# I.e there shoule be only one topological order and that should be equal to nums.

import collections

class Solution:
    def sequence_reconstruction(self, org, seqs):
        n = len(org)
        adj = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        nodes = set()   # to find no of distinct nodes 
        for seq in seqs:
            nodes |= set(seq)   # to Handle when len(seq) == 1, we have to include that one ele
            for i in range(len(seq) -1):
                a , b = seq[i] , seq[i + 1]
                indegree[b] += 1
                adj[a].append(b)
                nodes.add(a)
                nodes.add(b)

        q = []  # No need to take deque since we only need to pop single element.
        for num in range(1, n + 1):
            if num not in indegree:
                # means for num indegree will be '0' if in seq 
                # and num is not in seq then also will get added but get handled by 'if len(q) > 1'.
                q.append(num)

        shortCommonSupersequence = []
        while q:
            if len(q) > 1:
                # Means we can make two choices from same num so there will be more than one ans possible.
                return False
            node = q.pop()
            shortCommonSupersequence.append(node)    
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        # first one to check cycle and 2nd one for uniqueness.
        return len(shortCommonSupersequence) == len(nodes) and org == shortCommonSupersequence  
