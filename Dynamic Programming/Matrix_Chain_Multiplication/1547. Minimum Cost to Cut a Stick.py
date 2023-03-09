# 1st method: Recursive
# logic in notes: 123,124
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # we can cur at any of th egiven position in cuts so there must be something on leftmost and rightmost side to calculate the length that's why appedning these number.
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()  # agla kon sa length pe cut karna h har part me, usko pta karne ke liye sort karna hoga
        l= len(cuts)
        return self.helper(cuts, 1, l-1)
    
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
        cuts.insert(0,0)   # list.insert(pos, elmnt)
        cuts.append(n)
        cuts.sort()
        l= len(cuts)
        dp= [[-1 for j in range(l)]for i in range(l)]
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
        cuts.insert(0,0)
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
