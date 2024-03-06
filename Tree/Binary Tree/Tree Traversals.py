def PreorderRecursive(self,root):
        if root== None:
            return
        print(root.data,end=" ")
        self.PreorderRecursive(root.left)
        self.PreorderRecursive(root.right)

# iterative way
# Logic: first push the right subtree in the stack as we have to 
# print 'left' side first and stack is LIFO
def PreorderIterative(self,root):
    if root== None:
        return 
    stack= []
    stack.append(root)
    while stack:
        curr= stack.pop()
        print(curr.data, end=" ")
        if curr.right: 
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

# do by recursive inside the given function only and store the ans in a list(Leetcode q)
# same way we can do for other traversals.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        if not root:
            return ans
        ans.append(root.val)
        ans+= self.preorderTraversal(root.left)
        ans+= self.preorderTraversal(root.right)
        return ans


# other way of writing above code
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left=  self.preorderTraversal(root.left)
        right= self.preorderTraversal(root.right)
        return [root.val] + left +  right   # just the logic of inorder traversal.
    

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
        r= self.inorderTraversal(root.right)
        return l+ [root.val] + r        # just the meaning of inorder

# Note vvi: iterative one
# easier one. just the conversion of iterative form when we start from root.left
# logic: just keep on going left and when left is none then pop the last added one(just same as recursive code, think little)

# class Solution:
#     def InOrder(self,root):
#         if root== None:
#             return []
#         ans=  []
#         stack= []
#         stack.append(root)
#         curr= root
#         while stack :
#             if curr.left== None:
#                 temp= stack.pop()
#                 ans.append(temp.data)
#                 if temp.right:
#                     curr= temp.right
#                     stack.append(temp.right)
#             else:
#                 stack.append(curr.left)
#                 curr= curr.left
#         return ans


# another concise way of iterative approach of inorder traversal. 
# just the conversion if we start from root. 
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
        # if None, it means no left child then print the stack top (just pop).
        # it means we have reached the leftmost node.
        curr= stack.pop()
        ans.append(curr.val)
        root= curr.right  # move the pointer to check the right child.
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
        return l + r + [root.val]     # just the meaning of postorder
    
# Direct karna difficult h but agar hm reverse way me print kar de to last me hm ans ko reverse karke final ans mil jayega i.e:
# agar [left, right, root] ke jagah -> [root, right, left] solve kar de and then last me ans ko reverse kar denge.

# or usko hm preorder jaisa solve kar sakte h.
# append left 1st than right because we want right before left .
    

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


