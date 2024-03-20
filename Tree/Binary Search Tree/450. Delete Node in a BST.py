


# since we are not directly deleting any node in all cases i.e we are modifying the structure also .
# so we can't simply call the fucntion like above, we have to store at proper position like we were doin while inserting the node.
# i means we can call like deletenode(root,key), we have to call like 'node.left(right)= deletenode(root,key)'.
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


# My mistake:
# Was deleting the copie value from 'root.right'
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

            # now it means both are not None. means has both the child
            else:
                print(root.val)
                # search for inorder successor(minimum ele on right subtree) or inorder predecessor(max on left subtree).
                # searching for inorder successor, min on right side
                curr= root.right
                while curr.left:
                    curr= curr.left
                root.val= curr.val
                curr= None         # we have to delete 'cur.val' from 'root.right' also for correct ans
        elif root.val> key:
            self.deleteNode(root.left,key)
        else:
            self.deleteNode(root.right,key)
        return root