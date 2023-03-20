# time: exponential
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
                    rootNode= TreeNode(root, leftNode, rightNode)   # form the tree formed with root = root and all possible combination of leftNode and rightNode as left and right child.
                    ans.append(rootNode)   # add the formed tree to ans
        return ans


