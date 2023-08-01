# Ans is same as catalan number.
# Reason: No of possible unique binary tree structure for 'n' nodes = catalan(n)
# And each structure can give the desired preorder, inorder or postorder. 

# Explanation in note, page no : 126

# Now, asking for no of bst given 'n' nodes means indirectly asking "no of tree structure that will be give [1,2,3...n] as inorder"
# And this i sequal to= catalan(n)
class Solution:
    def numTrees(self, n: int) -> int:
        return (math.comb(2*n, n))//(n+1)

#  Recursive way
# Method 2: 
# Note: in case of combination we use '*' not '+'.
class Solution:
    def numTrees(self, n: int) -> int:
        def solve(i , j):
            # if left with '0' nodes after selecting any node as root for cur subtree then ,
            # there will be only choice to make the subtree as 'None'. 
            if i >j:
                return 1
            ans = 0
            for k in range(i, j + 1):
                # if we choose 'k' as root then ele (i, k-1) will go to left subtree and
                # ele (k+1, j) will go to right subtree.
                ans +=  solve(i, k -1) * solve(k + 1, j)   # have to add all ways after selcting 'k' as root.
            return ans

        return solve(1 , n)   #[1, n]

# Methdo 3:
# vvi :No of BST will only depend in no of nodes so we can get ans using one parameter only.
# But above logic will work in Q : "95. Unique Binary Search Trees II".

# Just same as above method only.

# for more clarity read the DSA notes. page: 57, 58 and 67.
# logic in notes, page: 126

# vvi: Read this link for more clarity and to know how we are generating the subproblem.
# ans= program for finding nth catalan number only.
# https://leetcode.com/problems/unique-binary-search-trees/solutions/31666/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i/

# After fixing the root, we have to add all the possible combination of left and right part.
# How all possible combination?
# Ans: Beacause if 1st node from left is direct child of root then any of the number from right part can be the right child of root.
# Same for all numbers in left part.

# Note: in case of combination we use '*' not '+'.

class Solution:
    def numTrees(self, n: int) -> int:
        if n<= 1:
            # when we are left with '1' or '0' nodes.
            return 1
        ans= 0
        # we can choose any of the node as root. every num will be at root. 
        # After choosing root we have to find the BST which can form by taking that num as root.
        for k in range(1, n+1):
            ans+= self.numTrees(k-1) * self.numTrees(n-k)   # no of trees only depend on the number of nodes in left and right subproblem(not on the node we are considering).
            # after selecting 'i' as root no of nodes in left part will be 'i-1' and no of nodes in right part will be 'n-i'.
            # Also since BST nodes before left of 'i' will be left children and node after 'i' will be the right children.
        return ans
    

# Note vvi: if we do like this then we will get error because here we are not adding all combination when any ele can be root.
# Will always give ans = 1...
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        for k in range(1, n + 1):
            return 


# directly to Tabulation from Recursive
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)  # dp[i]: no of BST when no of nodes = 'i'.
        dp[0] = dp[1] = 1
        # we have to find no of BST when no of nodes will be '2, 3,....n'
        for j in range(2, n + 1):
            ans = 0
            for k in range(1, j + 1):
                ans += dp[k -1] * dp[j -k]
            dp[j] = ans
        return dp[n]

