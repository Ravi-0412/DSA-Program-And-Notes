# applied the exactly same logic as " 430. Flatten a Multilevel Doubly Linked List"
# time: O(n)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root== None:
            return root
        remaining_left= None
        temp= root.right
        if root.left:
            remaining_left= self.flatten(root.left)
            root.right= remaining_left   # we have to always add the node with rigth pointer only in the ans
        if temp:  # if root.right!= None
            remaining_right= self.flatten(temp)
            if remaining_left:  # if there is node on left side of root, then add the ans in right part to the last node in left side ans
                curr= remaining_left
                while curr.right:     # we have to check in ans , so rigth pointer only
                    curr= curr.right
                curr.right= remaining_right
            else:  # if no node on left side of root then directly add the ans got for right part to the root
                root.right= remaining_right
        root.left= None   # while traversing back make left pointer as None
        return root

# method 2: 
# in above one first we were going root then left then right like preorder only
# in this we are going opposite first root then right and then then left   # reverse postorder
# after calculating for right side make the right of curr node = already calculated till right
# then go for left side 
# and point left with pre and this will automatically point to the 'preorder successor' 

# pre will conatain the ans calculated till now
# and at last return pre

# basically instead of using while loop for pointing the right side with last node of left , pre is working here
# as pre is storing the ans calculated till now
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pre= None
        def dfs(root):
            if root== None:
                return 
            dfs(root.right)
            dfs(root.left)
            root.right= self.pre
            root.left= None
            self.pre= root    
     
        dfs(root)
        return self.pre

# go through the other more approaches in striver video and do by those
# https://www.youtube.com/watch?v=sWf7k1x9XR4&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=39&t=61s
