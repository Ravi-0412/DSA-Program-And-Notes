# Method 1:
# Just store the preorder traversal in a list and ten connect all those to get the ans.
# space = time = O(n)


# Method 2: Space optimisation to O(1)
# Logic: Agar hm first time kisi node ko dekhte hi connect karenge tb wrong ans dega.
# Kyonki hm dusre node ko tabhi isse connect kar sakte h jb dusar node already flattened ho.
# Iske liye hm bottom up jana hoga.

# Now 1) current node ka right ko 'left' wale ke saath karna h agar 'left' is not None else 'right' wale child ke saath.
# 2) Then left wala ka last node se 'right' ko connect kar dena h.
# 3) cur node ka left ko null kar dena h.
# 4) cur node ko return kar dena h

# Not vvi: Aise Question me yhi logic lagana h , bhut simple h.
# e.g: in Q "430. Flatten a Multilevel Doubly Linked List"

# time: O(n)

class Solution(object):
    def flatten(self, root):
        if not root:
            return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        # first connect the next node that will come in preorder traversal 
        root.right = l if l else r   # if 'l' is not 'None' then it will come else 'r' will come
        # Now connect the right child with last node of left one. we only need to do this if both 'l' and 'r' are None
        if l and r:
            cur = l
            # 'l' and 'r' is already flattened so we need to tarverse with the help of 'right' pointer only.
            while cur.right:
                cur = cur.right
            cur.right = r  # 
        # Make 'cur' left pointer = None
        root.left = None  
        return root
    

# Undersatand other method later

# method 2: 
# in above one first we were going root then left then right like preorder only
# in this we are going opposite first root then right and then then left   # reverse postorder
# logic(ye sb type Q ke liye): jisko bad me add karna h usko phle visit karke 'pre' bna do

# point left(for ans 'right') to pre and this will automatically point to the 'preorder successor' 
# make left pointer= None

# pre will conatain the ans calculated till now
# so make pre point to root after each node .
# and at last return pre

# basically instead of using while loop for pointing the right side with last node of left , pre is working here
# as pre is storing the ans calculated till now.

 
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pre= None
        def dfs(root):
            if root== None:
                return  # not storing so simply return 
            dfs(root.right)
            dfs(root.left)
            root.right= self.pre
            root.left= None
            self.pre= root   # means we have visited till this root node
     
        dfs(root)
        return self.pre


# iterative one. just like do preorder only
# very simple: every time you get any node then add to the 'last of right' and make the last.left= None
# but extra space: o(n)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root== None:
            return root
        last= TreeNode(-1)  # can initialise with any val as it will start checking after we make connection from given root in the ans
        stack= [(root)]
        while stack:
            node= stack.pop()
            last.right= node
            last.left= None
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            last= node # to point the next node from the last added one

# go through the other more approaches in striver video and do by those
# https://www.youtube.com/watch?v=sWf7k1x9XR4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=39&t=61s
