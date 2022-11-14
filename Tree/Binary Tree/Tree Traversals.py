def PreorderRecursive(self,root):
        if root== None:
            return
        print(root.data,end=" ")
        self.PreorderRecursive(root.left)
        self.PreorderRecursive(root.right)

# do by recursive inside the given function only and store the ans in a list(Leetcode q)
# do later like this
# https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/164175/Python-solution

# for returning the nas into list inside the given fn onlty, somehow we will have to replace the print statement by any condition
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        elif root.left==None and root.right== None:
            return [root.val]
        l= self.preorderTraversal(root.left)
        r= self.preorderTraversal(root.right)
        return [root.val] + l+ r      # just the meaning of preorder


# recursive way: returning the ans in a list inside same function 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.inorderTraversal(root.left)
        # if root.right== None:   # this will give the wrong ans as after processing the left part if it comes then 
                                    # pre all value will not get stored in the ans
        #     return [root.val]
        if root.left== None and root.right== None:
            return [root.val]
        r= self.inorderTraversal(root.right)
        return l+ [root.val] + r        # just the meaning of inorder

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


def InorderRecursive(self,root):
    if root== None:
        return
    self.InorderRecursive(root.left)
    print(root.data,end=" ")
    self.InorderRecursive(root.right)  

# easier one 
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
    
# another concise way of iterative approach of inorder traversal
def InorderIterative(self,root):
    if root== None:
        return 
    stack= []
    curr= root
    while True:
        # reach the left bottom most node
        if curr:
            stack.append(curr)
            curr= curr.left
        # if no left child then we have to print the stack top and append the 'poped.right'
        elif stack:
            temp= stack.pop()
            print(temp.data, end=" ")
            curr= temp.right
        else:
            break

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
    

def postorderIterative1(self, root):
    stack, ans= [], []
    if root== None:
        return root
    stack.append(root)
    while stack:
        curr= stack.pop()
        ans.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    # now print the 'ans' in the reverse order
    while ans:
        print(ans.pop(),end= " ")
    
# using only single stack(try later)
def PostorderIterative(self,root):
    if root== None:
        return 
    stack= []
    stack.append(root)
    curr, pre= root, None
    while stack :
        if curr.left== None:         
            if curr.right:
                stack.append(curr.right)
                pre= curr
                curr= curr.right
            else: # means curr.left== None and curr.right== None
                # print("pre data " ,pre.data)
                temp= stack.pop()
                print(temp.data, end=" ")
                curr= pre.right
                stack.append(curr)
                pre= None
                # print("curr data", curr.data)
        if curr.left:
            stack.append(curr.left)
            pre= curr
            curr= curr.left

            