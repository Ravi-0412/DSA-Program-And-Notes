# my mistaek: i didn't get the q properly

# logic: just you have to find the max width at each level
# for this we can number all the node using array notation of tree
# width at each level= num(right most node i.e last node at that level)- num(leftmost node i.e first node) + 1
# take max of all width

# for this we can use Level Order Traversal. easiest one
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q= collections.deque()
        q.append((root,0))   # using 0 based indexing for numbering each node
        ans= 0
        while q:
            # keep updating the max at each level
            ans= max(ans,q[-1][1]- q[0][1] + 1) # max width at each level= num(right most node i.e last node at that level)- num(leftmost node i.e first node) + 1
            for i in range(len(q)):
                node, num= q.popleft()
                if node.left: q.append((node.left,   2*num +1))     # left node will at 2*i+1 in '0' based indexing
                if node.right: q.append((node.right, 2*num +2))     # right node will at 2*i+2 in '0' based indexing
        return ans

