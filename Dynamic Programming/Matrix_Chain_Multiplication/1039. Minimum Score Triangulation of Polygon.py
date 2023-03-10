# first understand the meaning of triangulation.
# meaning: polygon triangulation is the partition of a polygonal area (simple polygon) P into a set of triangles,[1] i.e., 
# finding a set of triangles with pairwise non-intersecting interiors whose union is P.
# note: Any edge should not intersect .
#  logic in notes: page 125

# my mistakes:
# i didn't understand the meaning of triangulation and did like this.
# i thought keep the 1st and 2nd vertices as edge for all triangle to get minimum.
# But in this edges will intersect.
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n= len(values)
        values.sort()
        ans= values[0] * values[1] *values[2]
        firstTwoEleMultiplication= values[0]*values[1]
        for i in range(3, n):
            ans+= firstTwoEleMultiplication * values[i]
        return ans

# correct one
# logic:
# keep th 1st and last vertex as common edge and for all remaining node take possibility like we used in MCM type Q.
# # By doing this only, it will form a valid triangulation.
# note: 'k' will be from 'i+1' to 'j-1' since we have already included 'i' and 'j' vertices.
# for every subProblem fixed the 1st and last vertex as common base.

# method 1: Recursive
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def minScore(i, j):
            # if j- i +1 < 3:  # less than 3 vertices  
            #     return 0
            if i+1== j:   # means 2 vertices
                return 0
            score= float('inf')
            for k in range(i+1, j):
                tempAns= minScore(i, k) + minScore(k, j) + values[i]*values[k]*values[j]
                score= min(score, tempAns)
            return score
    
        n= len(values)
        i, j= 0, n-1
        return minScore(i, j)

# method 2:
# memoisation: using '@lru_cache(None)'.
# note: for using lru_cache' before any function call, the parameter in fucntion must be only the changing variables (no any extra varaible).
# time: O(n^3)
# space :O(n^2 )
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @lru_cache(None)
        def minScore(i, j):
            if i+1== j:   # means 2 vertices
                return 0
            score= float('inf')
            for k in range(i+1, j):
                tempAns= minScore(i, k) + minScore(k, j) + values[i]*values[k]*values[j]
                score= min(score, tempAns)
            return score
    
        n= len(values)
        i, j= 0, n-1
        return minScore(i, j)

# memoisation using arrays.
# sometimes it is better to use hashing than making array for memoisation.
# one doubt: dp of (n * n-1) is not working. i don't know why.
# like seeing the base case . i+1== j:
# range of i : 0 to n-2 ,  j: n-1 to 1. so max 'i' can go till 'n-2' and 'j' till 'n-1'. so size (n-1 *n)

# time: O(n^3), space: O(n^2)
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def minScore(i, j, dp):
            # if j- i +1 < 3:  # less than 3 vertices  
            #     return 0
            if i+1== j:   # means 2 vertices
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]
            score= float('inf')
            for k in range(i+1, j):
                tempAns= minScore(i, k, dp) + minScore(k, j, dp) + values[i]*values[k]*values[j]
                score= min(score, tempAns)
            dp[i][j]= score
            return dp[i][j]
   
        n= len(values)
        dp= [[-1  for j in range(n)] for i in range(n-1)]
        i, j= 0, n-1
        return minScore(i, j, dp)


# Tabulation.
# Rules: calling function se just ulta start karte h hmesha.
# 'i': 0 to n-2 (forward) including base case . so in tabulation i: n-3 to 0 (backward).
# 'j': n-1 to '1' (backward) including base case. so in tabulation: i+2 to 'n-1' (forawrd).
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n= len(values)
        dp= [[0 for j in range(n)] for i in range(n-1)]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                score= float('inf')
                for k in range(i+1, j):
                    tempAns= dp[i][k]+ dp[k][j] + values[i]*values[k]*values[j]
                    score= min(score, tempAns)
                dp[i][j]= score
        return dp[0][n-1]


# best one and easy one to understand
# https://www.youtube.com/watch?v=Eo4G_LPCgX8&t=1292s