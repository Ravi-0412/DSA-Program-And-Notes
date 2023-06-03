# method 1: Brute force
# steps: 1) find the inorder traversal and store them into an array say 'inorder'.
# 2) search for index of each root.val in 'inorder' array , using binary search say 'idx'.
# 3 ) Find the suffix sum to get the sum from the above index to last in o(1).
# then root.val= suffix[idx]

# time: O(n*logn), searching index of each ele .

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # Find the inorder Traversal 
        inorder= []
        stack, cur= [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur= cur.left
            temp= stack.pop()
            inorder.append(temp.val)
            cur= temp.right

        # search the index of 'num' in sorted array i.e 'inorder' to find all numbers greater than num.
        # Binary Search
        def search(num):
            start, end= 0, len(inorder) -1
            while start < end:
                mid= start + (end - start)//2
                if inorder[mid] >= num:
                    end= mid
                else:
                    start= mid + 1
            return start
        
        # calculate the suffix sum to find sum of greater ele in O(1)
        n= len(inorder)
        suffix= [0]*n
        suffix[n-1]= inorder[n-1]
        for i in range(n-2, -1, -1):
            suffix[i]= suffix[i + 1] + inorder[i]
        
        # function to change the value of nodes
        def preorder(root):
            if not root:
                return 
            idx= search(root.val)
            print(root.val, idx)
            root.val= suffix[idx]
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return root
    

# method 2:

# logic: We need to do the work from biggest to smallest, right to left.
# pre will record the previous value the we get, which the total sum of bigger values.
# For each node, we update root.val with root.val + pre.

# time: O(n)
# space: O(height)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.pre= 0  # will store the sum of all values > root.val 

        def ReverseInorder(root):
            if root.right:
                ReverseInorder(root.right)
            # update the pre, and cur root val
            self.pre= root.val= root.val + self.pre
            if root.left:
                ReverseInorder(root.left)
        
        ReverseInorder(root)
        return root

