# Note vvi: This problem get reduced to 
# "Is is possible to partition the matchsticks into 4 subsets such that sum of all subsets is equal?".

# And above reduced one is exactly same as "698. Partition to K Equal Sum Subsets".
# Just replace k ->4.

# Time: O(n^4)

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        edgesSum= [0]*4  # will store the sum of length of each edge.
        edgeLength = sum(matchsticks) // 4  # All edges length should be this only.
        matchsticks.sort(reverse=True)  # optimisation to reach base case inside the loop faster.
        n = len(matchsticks)
        
        def canPartition(i):
            # If we've placed all of the items, we're done.
            # check if we correctly made 4 edges each of length = edgeLength
            if i == n:
                return len(set(edgesSum)) == 1
            # cur ele can go to any of the edges
            for j in range(4):
                # Try adding the current element to it
                edgesSum[j] += matchsticks[i]
                # If it's a valid placement and we correctly placed the next element, we're
                # done placing the current element.
                if edgesSum[j] <= edgeLength and canPartition(i+1):  # optimisation
                    return True
                edgesSum[j] -= matchsticks[i]
				
                if edgesSum[j] == 0:  # optimisation, no need to try other empty bucket
                    return False
            return False        
        
        return canPartition(0)
    

# Later try by DP + Bit masking
