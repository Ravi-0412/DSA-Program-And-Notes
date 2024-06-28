# just find the inorder traversal and then apply the logic : "108. Convert Sorted Array to height Balanced Binary Search Tree"
# time: O(n)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        stack, ans = [], []
        cur = root
        while stack or cur:
            while cur:  # keep going left 
                stack.append(cur)
                cur = cur.left
            # if None, it means no left child then print the stack top and append the 'popped.right'
            # it means we have reached the leftmost node 
            temp = stack.pop()
            ans.append(temp.val)
            cur = temp.right
        return self.sortedArrayToBST(ans)
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        print(mid, "mid")
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


# Java
"""
public class Solution {
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        
        // In-order traversal to collect node values
        while (!stack.isEmpty() || cur != null) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            TreeNode temp = stack.pop();
            ans.add(temp.val);
            cur = temp.right;
        }
        
        return sortedArrayToBST(ans, 0, ans.size() - 1);
    }
    
    private TreeNode sortedArrayToBST(List<Integer> nums, int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode node = new TreeNode(nums.get(mid));
        node.left = sortedArrayToBST(nums, start, mid - 1);
        node.right = sortedArrayToBST(nums, mid + 1, end);
        return node;
    }
}
"""
