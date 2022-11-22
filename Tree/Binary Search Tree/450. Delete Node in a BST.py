# don't getting why this is not working
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root== None:
            return root
        if root.val== key:
            # check if root is leaf
            if root.left== None and root.right== None:
                root= None
            # check if root has only one child
            elif root.left== None:
                root= root.right
                root.right= None
            elif root.right== None:
                root= root.left
                root.left= None
            # now it means both are not None
            else:
                print(root.val)
                # search for inorder successor(minimum ele on right subtree) or inorder predecessor(max on left subtree)
                # searching for inorder successor
                curr= root.right
                while curr.left:
                    curr= curr.left
                print(curr.val)
                root.val= curr.val
                curr= None
        elif root.val> key:
            self.deleteNode(root.left,key)
        else:
            self.deleteNode(root.right,key)
        return root


# same logic but working
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root== None:
            return root
        if root.val== key:
            # check if root is leaf
            if root.left== None and root.right== None:
                root= None
            # check if root has only one child
            elif root.left== None:
                root= root.right
            elif root.right== None:
                root= root.left
            # now it means both are not None
            else:
                # search for inorder successor(minimum ele on right subtree) or inorder predecessor(max on left subtree)
                # searching for inorder successor
                curr= root.right
                while curr.left:
                    curr= curr.left
                root.val= curr.val
                # now delete the inorder successsor(copied one) from right subtree and attach that to the right of root
                root.right= self.deleteNode(root.right,curr.val)
        elif root.val> key:  # we have to delete from left
            root.left= self.deleteNode(root.left,key)
        else:  # delete from right
            root.right= self.deleteNode(root.right,key)
        return root

