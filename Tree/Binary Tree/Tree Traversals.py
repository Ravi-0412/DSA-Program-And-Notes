def PreorderRecursive(self,root):
        if root== None:
            return
        print(root.data,end=" ")
        self.PreorderRecursive(root.left)
        self.PreorderRecursive(root.right)

# iterative way 
def PreorderIterative(self,root):
    if root== None:
        return 
    stack= []
    stack.append(root)
    while stack:
        curr= stack.pop()
        print(curr.data, end=" ")
        if curr.right: # first push the right subtree in the stack as we have to 
                       # print 'left' side first and stack is LIFO
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

# do by recursive inside the given function only and store the ans in a list(Leetcode q)
# do later like this
# https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/164175/Python-solution

# for returning the ans into list inside the given fn only, somehow we will have to replace the print statement by any condition
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None: # it will reach this condition in case of one child
            return []
        elif root.left==None and root.right== None:  # if leaf node
            return [root.val]
        l= self.preorderTraversal(root.left)
        r= self.preorderTraversal(root.right)
        return [root.val] + l+ r      # just the meaning of preorder



def InorderRecursive(self,root):
    if root== None:
        return
    self.InorderRecursive(root.left)
    print(root.data,end=" ")
    self.InorderRecursive(root.right)  

# recursive way: returning the ans in a list inside same function 
# just same as preorder,only change of meaning
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.inorderTraversal(root.left)
        if root.left== None and root.right== None:
            return [root.val]
        r= self.inorderTraversal(root.right)
        return l+ [root.val] + r        # just the meaning of inorder

# iterative one
# easier one. just the conversion of iterative form when we start from root.left
# logic: just keep on going left and when left is none then pop the last added one(just same as recursive code, think little)
# def InorderIterative(self,root):
#     if root== None:
#         return 
#     stack= []
#     stack.append(root)
#     curr= root
#     while stack :
#         if curr.left== None:
#             temp= stack.pop()
#             print(temp.data, end=" ")
#             if temp.right:
#                 curr= temp.right
#                 stack.append(temp.right)
#         if curr.left:
#             stack.append(curr.left)
#             curr= curr.left


# another concise way of iterative approach of inorder traversal. 
# just the conversion if we start from root 
# logic: if root is not None we append and move to the left 
# if none then we print the last added ele into the stack and move to right

# better one. This will help in solving a lot of problem of BST
#  by just adding few lines or modifying few lines 
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
    return ans



def PostorderRecursive(self,root):
    if root== None:
        return
    self.InorderRecursive(root.left) 
    self.InorderRecursive(root.right)
    print(root.data,end=" ")

# returning the ans inside a list in same function
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.postorderTraversal(root.left)
        r= self.postorderTraversal(root.right)
        if root.left== None and root.right== None:
            return [root.val]
        return l + r + [root.val]     # just the meaning of postorder
    
# just same as preorder
# only diff append the left one first then right one as ans will be in reverse order then only right will first get added into the ans(after poping)
# and when we will reverse it we will get in the form (left,right,root)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return 
        stack, ans= [], []
        stack.append(root)
        while stack:
            curr= stack.pop()
            ans.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans[::-1]


