# Ans is same as catalan number.
# for more clarity read the DSA notes. page: 57, 58 and 67.
# logic in notes, page: 126

# vvi: Read this link for more clarity and to know how we are generating the subproblem.
# ans= program for finding nth catalan number only.
# https://leetcode.com/problems/unique-binary-search-trees/solutions/31666/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/

class Solution:
    def numTrees(self, n: int) -> int:
        if n<= 1:
            return 1
        ans= 0
        # we can choose any of the node as root. every num will be at root. 
        # After choosing root we have to find the BST which can form by taking that num as root.
        for i in range(1, n+1):
            ans+= self.numTrees(i-1) * self.numTrees(n-i)   # no of trees only depend on the number of nodes in left and right subproblem(not on the node we are considering).
            # after selecting 'i' as root no of nodes in left part will be 'i-1' and no of nodes in right part will be 'n-i'.
            # Also since BST nodes before left of 'i' will be left children and node after 'i' will be the right children.
        return ans


# directly to Tabulation from Recursive
class Solution:
    def numTrees(self, n: int) -> int:
        if n<= 1:
            return 1
        dp= [0]* (n+1)
        dp[0]= dp[1]= 1
        # we can choose any of the node as root. every num will be at root. 
        # After choosing root we have to find the BST which can form by taking that num as root.
        for j in range(2, n+1):   # constarint for which we were calling the recursive function.
            for i in range(1, j+1):    # we were starting from '1' and was going till 'n' (called fun parameter)
                dp[j]+= dp[i-1]*dp[j-i]
        return dp[n]


# most concise.
# finally the ans= catalan(n)
# the above tabulation is code for catalan(n) only.

# using math libaray to find the catalan number.
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 2:
            return n
        return (math.comb(2*n, n))//(n+1)   # used the formula for catalan number
