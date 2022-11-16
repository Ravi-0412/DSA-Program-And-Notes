# logic is same as we search for element
# this is for bst
# but not working
def Ancestors(self, root,target):
        if root== None or root.data== target:
            return
        if target < root.data and root.left!= None:
            self.Ancestors(root.left,target)
            print(root.left.data, end=" ")
        elif target > root.data and root.right!= None:
            self.Ancestors(root.right,target)
            print(root.right.data, end=" ")


# this i don't know why not working , giving error on gfg
# this is for binary tree
def Ancestors(self, root,target):
        if root== None: 
            return False
        if root.data== target: 
            return True
        if (self.Ancestors(root.left,target) or self.Ancestors(root.right,target)):
            print(root.data,end=" ")
            return True
        return False