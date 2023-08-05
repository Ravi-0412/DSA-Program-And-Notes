# time: exponential
# Just same as method 2 of Q : "95. Unique Binary Search Trees II".
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Matrix_Chain_Multiplication/96.%20Unique%20Binary%20Search%20Trees.py

# Just replace (i->left , j -> right and k->root)
# logic in notes, page: 127, 128
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate(1, n)
    
    def generate(self, left, right):
        if left > right:
            return [None]
        ans= []
        for root in range(left, right +1):
            leftNodes=  self.generate(left, root -1)
            rightNodes= self.generate(root + 1, right)
            for leftNode in leftNodes:
                for rightNode in rightNodes:
                    # form the tree formed with root = root and all possible combination of leftNode and rightNode as left and right child.
                    rootNode= TreeNode(root, leftNode, rightNode)  
                    ans.append(rootNode)   # add the formed tree to ans
        return ans


# Similar Q:
# 1) 96. Unique Binary Search Trees
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Matrix_Chain_Multiplication/96.%20Unique%20Binary%20Search%20Trees.py



# 2) 894. All Possible Full Binary Trees
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Matrix_Chain_Multiplication/894.%20All%20Possible%20Full%20Binary%20Trees.py

# 3) 241. Different Ways to Add Parentheses

# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Matrix_Chain_Multiplication/241.%20Different%20Ways%20to%20Add%20Parentheses.py