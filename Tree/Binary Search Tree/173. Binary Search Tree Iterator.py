# did but space: O(n)
# just store the inorder in any list
# for 'next' function just return the last ele from the 'inorder   # was not able to do by deque so stored in reverse order
# to get the 1st ele of inorder tarversal in O(1)
# ask someone why giving error when using deque

# for 'hasnext' if inorder is not empty return True else False

class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode]):
        self.inorder= self.InorderIterative(root)
        

    def next(self) -> int:
        return self.inorder.pop()
        

    def hasNext(self) -> bool:
        if self.inorder:
            return True
        return False
            
    
    
    def InorderIterative(self,root):
        if root== None:
            return 
        stack, ans= [], []
        while stack or root:
            while root:  # keep going left 
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node 
            curr= stack.pop()
            ans.append(curr.val)
            root= curr.right
        return ans[::-1]     # not able to do when making 'inorder' array as deque
                            # so did like this to avoid the time complexity of pop()


# reducing the space complexity to O(n)
# first push all the left ele of root i.e inorder traversal rule
# for 'next' just pop the node and push its right

# here we only pushing all the left node not all the nodes initially and when 'next' is called
# this will make sure that space complexity doesn't go beyond O(H)
# space: O(n)
# time: O(1) average case. we are pushing 'n' ele and we are calling 'next' function 'n' times

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack= []
        self.PushLeft(root)
        
    def next(self) -> int:
        temp= self.stack.pop()
        self.PushLeft(temp.right)  # we have already pushed the all the 'left' nodes so we only need to push the right one
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack!= []
    
    def PushLeft(self, root):
        # push everything that comes on the left of root
        curr= root
        while curr:
            self.stack.append(curr)
            curr= curr.left

# the above approach can be used to solve "kth smallest ele in BST" and "653. Two Sum IV - Input is a BST". 
# just count the no of function call for 'next' function for 1st one 

# for 2nd Q: store the poped node and check if its value is already present in the hashmap
# if present means sum exists alse add into the hashmap



# for getting the 'prev' just push all the right ele first and for any node you pop
# just the opposite of inorder i.e Right,Root,Left
# doing opposite of inorder will sort the array in descending order
# 'prev' will give the elements in from last of inorder


