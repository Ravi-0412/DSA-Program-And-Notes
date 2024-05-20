# just store the path for both the nodes in two separate array 
# LCA: will be that node from that last where the path of both the nodes will match from the last.

# Now Q reduces to: "Given Two arrays, find the the first ele common in both the array from last".
# use Two pointer and for moving pointer: decr that index which is more. if equal decr both.

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
            # in case didn't match.
            elif i > j:  # only decr 'i'. means no of ele in path1 is more
                i -= 1
            elif j > i:   # only decr 'j'. means no of ele in path2 is more
                j -= 1
            else:  # it means remainging no of ele in both is same. 
                i,j = i-1, j-1

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



# 2nd method: very better and very logical 
# optimising the space complexity to O(1)
# here we are sure that both the nodes are present in the tree so we can utilise this.

# LCA: wo node hoga jahan pe bottom se dono node 1st time differ karenge i.e means is node ka left subtree ek node ko contain karega and right subtree dusre node ko.
# so just apply bottom up Approach and if at any node if its both the left and right subtree give not None , it means curr node is LCA.

# one of the node can be the LCA also, so in this case one will have 'None'(doesn't contain any of the node) and other will have 'Not None'.
# then in this case the node with 'not None' will be LCA.

# Note: Here once we find the and then we will start returning ans from there itself.

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        if root== p or root== q:  # then return that node to the parent
            return root
        # if not equal to the nodes value then search on both left and right side
        left_search=  self.lowestCommonAncestor(root.left, p , q)
        right_search= self.lowestCommonAncestor(root.right, p , q)
        # if left_search is None and then right subtree contains both the nodes
        if left_search== None:
            return right_search
        # if left_search is not None then left subtree conatins both the nodes
        if right_search== None:
            return left_search
        # now it means both of the 'left' and 'right' part is None means both contain one of the two node.
        # so root will be LCA only, from here both node has went to different subtree.
        return root 


