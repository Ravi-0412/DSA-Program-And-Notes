# 1st method: Recursive
# logic in notes: 123,124

# lOgic: # we can cur at any of the given position in cuts so there must be something on leftmost and rightmost side 
# to calculate the length that's why appedning these number.
# so first insert '0' and 'n' and then sort. Then automatically '0' will come at furst and 'n' at last.
# why sorting?
# agla kon sa length pe cut karna h har part me, usko pta karne ke liye sort karna hoga

# After that apply same logic as 'MCM'.

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        return self.helper(cuts, 1, l-1)   # first valied -> 1 and first invalid -> l - 1
                                           # first_invalid - (1st_valid - 1)  will give length after each cut.
    
    def helper(self, cuts, i, j):
        if i==j:
            return 0
        mn= 9999999999
        for k in range(i, j):
            tempAns= self.helper(cuts, i, k) + self.helper(cuts, k+1, j) + cuts[j]- cuts[i-1]
            # tempAns= self.helper(cuts, i, k-1) + self.helper(cuts, k+1, j) + cuts[j]- cuts[i-1]   # i was writing this. last range should be invalid only and writing 'k-1' will make valid
        mn= min(mn, tempAns)
        return mn

# method 2: memoization
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        dp= [[-1 for j in range(l)] for i in range(l)]
        return self.helper(cuts, 1, l-1, dp)
    
    def helper(self, cuts, i, j, dp):
        if i==j:
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        mn= 9999999999
        for k in range(i, j):
            tempAns= self.helper(cuts, i, k, dp) + self.helper(cuts, k+1, j, dp) + cuts[j]- cuts[i-1]
            mn= min(mn, tempAns)
        dp[i][j]= mn
        return dp[i][j]


# Tabulation
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        dp= [[0 for j in range(l)]for i in range(l)]  # already get initialised with base case 
        for i in range(l-2, 0, -1):   # from last valid one to first valid one
            for j in range(i+1, l):   # for valid one 'j' must be greater than 'i' i.e 'j' should go till 'l-1'
                mn= 9999999999
                for k in range(i, j):
                    tempAns= dp[i][k] + dp[k+1][j] + cuts[j]- cuts[i-1]
                    mn= min(mn, tempAns)
                dp[i][j]= mn
        return dp[1][l-1]
