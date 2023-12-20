# Logic: Since the number of nodes is at most 10, we can check all possible sets of branches.
# There are exactly 2^n possible sets, which is at most 2^10=1024.

# Time complexity: O(2^n×n^3)
# Space complexity: O(n^3)


class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        
        def check(D,included):
            # Just Floydd warshall only
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        # Before updating 1st check if we can take them or not
                        if D[i][k] < inf and D[k][j] <inf: 
                            D[i][j] = min(D[i][j],D[i][k]+D[k][j])

            # Now check the minimum distance of all nodes from each (node one by one)
            # is <= maxDistance or not.          
            for x in included:
                for y in included:
                    if x == y:continue  # there can be duplicate since we stored in list.
                    if D[x][y] > maxDistance: 
                        return False
            return True
        
        dist = [[float(inf)]*n for _ in range(n)]
        
        for u,v,w in roads:
            # there can be multiple edge so take minimum possible length.
            dist[u][v] = min(dist[u][v],w)
            dist[v][u] = min(dist[v][u],w)

        comb = 1 << n  # 2^n possible combination         
        ans = 0 
        # checking all possible 2^n combination.
        for mask in range(comb):
            # Every time we have to start with 'dist' matrix i.e given one only.
            newDist = [dist[i].copy() for i in range(n)]  
            
            included = []  # will store all the nodes that were included for current combination(set)
                           # Storing in list because we can't take all combination in set.
            for i in range(n):
                # if 'i'th node is not included then make length of all connected node = 'inf' from both side
                if (mask >> i) & 1 == 0:
                    for j in range(n):
                        newDist[i][j] = inf
                        newDist[j][i] = inf
                else:
                    # Add in included one
                    included.append(i)
            # Now check if distance between all pairs of currently included node is <= maxDistance or not.
            if check(newDist, included):
                # <= maxDistance then we can take this combination of node
                ans+=1
        return ans