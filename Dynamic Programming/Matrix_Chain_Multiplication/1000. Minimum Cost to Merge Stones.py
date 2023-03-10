# method 1: Recursive
# logic: merging into one piles is equal to merging into k piles then only we can merge those 'k' piles into one pile.\
# https://leetcode.com/problems/minimum-cost-to-merge-stones/solutions/327340/python-dp-solution-with-thinking-process/
# https://leetcode.com/problems/minimum-cost-to-merge-stones/solutions/247657/java-bottom-up-top-down-dp-with-explaination/
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n= len(stones)
        if (n-1)% (k-1)!= 0:  # we can't merge
            return -1
        # calculate prefix sum to find sum[i..j] easily
        sum= 0
        prefixSum= []
        for i in range(n):
            sum+= stones[i]
            prefixSum.append(sum)
        i, j= 0, n-1
        return self.minCost(i, j, 1, k, prefixSum)
    
    def minCost(self, i, j, piles, k, prefix):
        if i== j and piles== 1:
            return 0
        if i==j:
            return float('inf')
        
        if piles== 1:
            return self.minCost(i, j, k, k, prefix) + (prefix[j] if i== 0 else (prefix[j] - prefix[i-1]) )
        else:
            cost= float('inf')
            for t in range(i, j):
                tempAns= self.minCost(i, t, 1, k, prefix) +self.minCost(t+1, j, piles-1, k, prefix)
                cost= min(cost, tempAns)
            return cost

# method 2: memoisation
# time: O(n^3)= space
# using hashmap for memoisation

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n= len(stones)
        if (n-1)% (k-1)!= 0:  # we can't merge
            return -1
        # calculate prefix sum to find sum[i..j] easily
        sum= 0
        prefixSum= [0]*(n+1)   # doing like this to avoid checking if i== 0 in recursive call.
        for i in range(n):
            prefixSum[i+1]= prefixSum[i]+ stones[i]
        i, j= 0, n-1
        # dp= [[[-1 for t in range(k+1)] for j in range(n)] for i in range(n)]
        dp= {}
        return self.minCost(i, j, 1, k, prefixSum, dp)
    
    def minCost(self, i, j, piles, k, prefix, dp):
        if i== j and piles== 1:
            return 0
        if i==j:
            return float('inf')
        if (i, j, piles) in dp:
            return dp[(i, j, piles)]
        if piles== 1:
            dp[(i, j, piles)]= self.minCost(i, j, k, k, prefix, dp) + prefix[j +1] - prefix[i]
            return dp[(i, j, piles)]
        else:
            cost= float('inf')
            for t in range(i, j):
                tempAns= self.minCost(i, t, 1, k, prefix, dp) + self.minCost(t+1, j, piles-1, k, prefix, dp)
                cost= min(cost, tempAns)
            dp[(i, j, piles)]= cost
            return dp[(i, j, piles)]


# using 3D array for memoisation
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n= len(stones)
        if (n-1)% (k-1)!= 0:  # we can't merge
            return -1
        # calculate prefix sum to find sum[i..j] easily
        sum= 0
        prefixSum= [0]*(n+1)   # doing like this to avoid checking if i== 0 in recursive call.
        for i in range(n):
            prefixSum[i+1]= prefixSum[i]+ stones[i]
        i, j= 0, n-1
        dp= [[[-1 for t in range(k+1)] for j in range(n)] for i in range(n)]
        return self.minCost(i, j, 1, k, prefixSum, dp)
    
    def minCost(self, i, j, piles, k, prefix, dp):
        if i== j and piles== 1:
            return 0
        if i==j:
            return float('inf')
        if dp[i][j][piles]!= -1:
            return dp[i][j][piles]
        if piles== 1:
            dp[i][j][piles]= self.minCost(i, j, k, k, prefix, dp) + prefix[j +1] - prefix[i]
            return dp[i][j][piles]
        else:
            cost= float('inf')
            for t in range(i, j):
                tempAns= self.minCost(i, t, 1, k, prefix, dp) + self.minCost(t+1, j, piles-1, k, prefix, dp)
                cost= min(cost, tempAns)
            dp[i][j][piles]= cost
            return dp[i][j][piles]


# method 2: 
# https://leetcode.com/problems/minimum-cost-to-merge-stones/solutions/327340/python-dp-solution-with-thinking-process/
# https://leetcode.com/problems/minimum-cost-to-merge-stones/solutions/247567/java-c-python-dp/?orderBy=most_votes
# Analyse both the solution sproperly and keep in mnd.