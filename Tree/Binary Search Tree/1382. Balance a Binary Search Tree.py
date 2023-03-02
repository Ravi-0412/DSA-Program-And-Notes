# just find the inorder traversal and then apply the logic : "108. Convert Sorted Array to height Balanced Binary Search Tree"
# time: O(n)
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack, ans= [], []
        while stack or root:
            while root:  # keep going left 
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node 
            curr= stack.pop()
            ans.append(curr.val)
            root= curr.right
        print(ans)
        return self.sortedArrayToBST(ans)
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid= len(nums)//2
        print(mid, "mid")
        node= TreeNode(nums[mid])
        node.left=  self.sortedArrayToBST(nums[:mid])
        node.right= self.sortedArrayToBST(nums[mid+1:])
        return node
