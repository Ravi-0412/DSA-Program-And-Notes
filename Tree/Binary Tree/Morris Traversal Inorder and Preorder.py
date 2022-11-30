# 1st inorder: 
# checked on leetcode, working fine
# time:O(n), space: O(1)
# uses the concept of threaded binary tree. 
# point the rightmost child of left subtree to inorder successor.By doing this we don't have to traverse back to reach the next node
# we can reach that directly. after rightmost node of left subtree we will have to come to the root only. so make a thread between these two.
# Keep making the thread as in inorder first you have to go till left then only print the node. And
# if left child is None or we reach the root by thread  then print the root. it means that this node should be added to the inorder now.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr= root
        while curr:
            if curr.left== None:
                print(curr.val,end=" ")
                curr= curr.right    # if none means traversal is complete
            
            else:  # curr.left!= None
                pre= curr.left
                # seacrh for inorder successor of righmost ele of left subtree and make a thread 
                while pre.right and pre.right!= curr: 
                    pre= pre.right
                
                if pre.right== None: # form a thread, join pre with its inorder successor i.e curr
                    pre.right= curr   # forming the thread
                    curr= curr.left    # repeat for other node . This i was missing
                else:  # pre.right== curr  # if already thread is there then delete that thread 
                    # it means you have traversed the left portion so print the curr and move to right
                    # means you are visiting the node for 2nd time
                    pre.right= None  # breaking the thread 
                    print(curr.val,end=" ")
                    curr= curr.right    # if none means traversal is complete else left part is complete move to the left subtree


# 2: Preorder
# only diff: if left child is None or we make the thread  then print the root 
# i.e we add while making the thread instead we visit the node by already formed thread. Because in preorder
# first we have to print the curr node value then we can only move to the next one.
# submitted on leetcode
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        curr= root
        while curr:
            if curr.left== None:
                ans.append(curr.val)
                curr= curr.right
            
            else:  # curr.left!= None
                pre= curr.left
                # seacrh for inorder successor of righmost ele of left subtree and make a thread 
                while pre.right and pre.right!= curr: 
                    pre= pre.right
                
                if pre.right== None: # form a thread, join pre with its inorder successor i.e curr
                    ans.append(curr.val)   # only diff here from inorder.. just one line change.. 
                    pre.right= curr   # making the thread
                    curr= curr.left    # repeat for other node . This i was missing
                else:  # pre.right== curr  # if already thread is there then delete that thread 
                    # it means you have traversed the left portion so print the curr and move to right
                    # means you are visiting the node for 2nd time
                    pre.right= None   # breaking the thread
                    curr= curr.right
        return ans




