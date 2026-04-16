"""
To make the tree balance both left and right subtree should have equal nodes.
So for this always select the mid ele as root for every subtree and
ele before the mid will go to the left subtree and ele after mid will go to the right subtree.
time: O(N * logN) , logN : because of slicing each time
So avoid slicing and use indexes to reduce the complexity. 
Relace slicing by indexes in all questions and must avoid in interviews.

See below one without slicing and in O(N)
"""

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid= len(nums)//2
        node= TreeNode(nums[mid])  
        node.left=  self.sortedArrayToBST(nums[:mid])     # this returned tree will be the left child for root.
        node.right= self.sortedArrayToBST(nums[mid+1:])   # this returned tree will be the right child for root.
        return node # will return Tree


# Method 2:
# Time : O(N) 
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        
        def buildBST(left, right):
            # Base Case: If the range is empty, return None (leaf's child)
            if left > right:
                return None
            
            # Find the middle element to ensure the tree remains balanced.
            mid = left + (right - left) // 2
            
            # Create the root node for this specific sub-range
            node = TreeNode(nums[mid])
            
            # Recursively build the left subtree using the left half of the current range
            node.left = buildBST(left, mid - 1)
            
            # Recursively build the right subtree using the right half of the current range
            node.right = buildBST(mid + 1, right)
            
            # Return the node to link it to its parent
            return node
            
        return buildBST(0, n - 1)
