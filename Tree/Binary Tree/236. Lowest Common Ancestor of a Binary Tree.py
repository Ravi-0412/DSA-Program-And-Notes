# just store the path for both the nodes in two separate array 
# LCA: will be that node from that last where the path of both the nodes will matchj from the last
# for this compare both the arrays from last 
# for comapring you have to check few cases before decrementing any index

# method 1: very basic
# time: O(n)= space
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q= [],[]
        # find the path for both p and q
        self.path(root, p.val, path_p)   # i was passing only p so was getting path_p and path_q as empty
        self.path(root, q.val, path_q)
        i,j= len(path_p)-1 , len(path_q)-1
        while i>=0 and j>=0:
            if path_p[i]== path_q[j]:
                return path_p[i]
            elif i>j:  # only decr 'i'
                i-= 1
            elif j>i:   # only decr 'j'
                j-= 1
            else:  # both are equal so decr both by 1
                i,j= i-1, j-1

    def path(self,root,key,ans):  
        if root== None:
            return False
        ans.append(root)  # simply add the node you visit   # when i am writing ans.append(root.val), it's giving error so chnegd liked thsio don't know why
        if root.val== key:
            return True
        if self.path(root.left,key,ans) or self.path(root.right,key,ans):  # means key has path from the given root
            return True
        # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
        ans.pop()
        return False



# 2nd method: optimising the space complexity to O(1)
# here we are sure that both the nodes are present in the tree so we can utilise this 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        if root== p or root== q:  # then return that node to the parent
            return root
        # if not equal to the nodes value then search on both left and right side
        left_search=  self.lowestCommonAncestor(root.left, p , q)
        right_search= self.lowestCommonAncestor(root.right, p , q)
        # if left_search is None and right is not None  at last then right subtree conatins both the nodes
        if left_search== None:
            return right_search
        # if left_search is not None and right is  None  at last then left subtree conatins both the nodes
        if right_search== None:
            return left_search
        # if both is None then that None will be automatically get returned in any of the above if condition
        
        # so now condition left is both left_search and right_search is not None, an if both is not none then it means
        # both node 'p' and 'q' have path from this node 
        # i.e we have found the ans so simply return the node
        return root 
