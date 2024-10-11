# to make the tree balance both left and right subtree should have equal nodes.
# So for this always select the mid ele as root for every subtree and
# ele before the mid will go to the left subtree and ele after mid will go to the right subtree.
# time: O(n)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid= len(nums)//2
        node= TreeNode(nums[mid])  
        node.left=  self.sortedArrayToBST(nums[:mid])     # this returned tree will be the left child for root.
        node.right= self.sortedArrayToBST(nums[mid+1:])   # this returned tree will be the right child for root.
        return node # will return Tree

# Java
"""
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) {
            return null;
        }
        return helper(nums, 0, nums.length - 1);
    }

    private TreeNode helper(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);

        node.left = helper(nums, left, mid - 1);   // recursively build left subtree
        node.right = helper(nums, mid + 1, right); // recursively build right subtree

        return node;
    }
}
"""
