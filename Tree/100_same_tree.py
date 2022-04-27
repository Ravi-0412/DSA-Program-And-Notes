# on gfg
# time: O(min(m,n))
def isIdentical(self,root1, root2):
        if (root1!= None and root2== None) or (root1== None and root2!= None):
            return False
        if root1==None and root2== None:
            return True
        return (root1.data==root2.data) and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)