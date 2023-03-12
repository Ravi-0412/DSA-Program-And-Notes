
# just same as we did for Bst "q no: 96".
# difference: 1) if n is even then full binary tree is not possible because we will not not able to make every root with either '0' or '2' children only.
# 2) we have to divide our subproblem in such a way that left and right part contain odd no of nodes(since with even no we will not generate full binary tree).
# so selacting only even number in range to split the left part with odd number of nodes.
# 3) here only number of node will matter in left and right subpart not their values. # only structure will matter.
# so no need to pass any extra parameter like BST.
# And also no need to exchange the left and right part since we can get the same structure exhnage automatically at later stage.
# e.g: for n= 5, let root = 2 then in left we have '1' node and in right we have '3' node.  
# now let root= 4 then in left we have '3' node and in right we have '1' node. 
# so we will get the exchanged struture later .

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1== 0:  # if no of nodes is even then full binary tree is not possible
            return None
        return self.generate(n)
    
    def generate(self, n):
        if n== 1:
            return [TreeNode(0)]
        ans= []
        for i in range(2, n+1, 2):   # choose root at even position only to get odd number of node in left and right subpart.
            leftNodes=  self.generate(i- 1)
            rightNodes= self.generate(n - i)
            for left in leftNodes:
                for right in rightNodes:
                    rootNode= TreeNode(0, left, right)
                    ans.append(rootNode)
        return ans


# as we saw in above example subproblem is repeating so we can memoising.
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n & 1== 0:  # if no of nodes is even then full binary tree is not possible
            return None
        return self.generate(n)
        
    @lru_cache(None)
    def generate(self, n):
        if n== 1:
            return [TreeNode(0)]
        ans= []
        for i in range(2, n+1, 2):
            leftNodes=  self.generate(i- 1)
            rightNodes= self.generate(n - i)
            for left in leftNodes:
                for right in rightNodes:
                    rootNode= TreeNode(0, left, right)
                    ans.append(rootNode)
        return ans
