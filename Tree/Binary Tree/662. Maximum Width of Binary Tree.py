# my mistaek: i didn't get the q properly

# logic: just you have to find the max width at each level.
# And if we number all the nodes using array notation then,
# width at that level= num(right most node i.e last node at that level)- num(leftmost node i.e first node) + 1

# for this we can use Level Order Traversal. easiest one

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q= collections.deque([(root, 1)])
        ans= 1  # minimum can be this ans.
        while q:
            n= len(q)
            ans= max(ans, q[n -1][1] - q[0][1] + 1)     # width at each level= num(right most node i.e last node at that level)- num(leftmost node i.e first node) + 1
            for i in range(n):  # we have to print level by level in a list
                curr, ind= q.popleft()
                if curr.left: 
                    q.append((curr.left, 2*ind))    # left node will at 2*i in '1' based indexing
                if curr.right:
                    q.append((curr.right, 2*ind + 1))  # right node will at 2*i + 1 in '1' based indexing
        return ans