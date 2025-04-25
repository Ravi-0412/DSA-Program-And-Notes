# steps to do:
# 1) find the inorder traversal of both the tree and store in separate arrays.
# 2) Now merge two arrays(sorted form) and store them into a list.
# 3) Now Q reduces to "Given a sorted array convert into a balanced BST"

# Time : O(m+ n) = space
class Solution:
    
    def merge(self, root1, root2):
        inorder1= self.InorderIterative(root1)
        inorder2= self.InorderIterative(root2)
        # print(inorder1, inorder2)
        merged_array= self.mergeSortedArray(inorder1, len(inorder1), inorder2, len(inorder2))
        # return merged_array   # not a good way to return. form bst then return.
        root= self.sortedArrayToBST(merged_array)  # this will be give the root of the merged BST.
        return self.InorderIterative(root)
    
    def InorderIterative(self,root):
        if root== None:
            return 
        stack, ans= [], []
        while stack or root:
            while root:  # keep going left 
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node 
            curr= stack.pop()
            ans.append(curr.data)
            root= curr.right
        return ans
    
    def mergeSortedArray(self, nums1, m, nums2, n):
        i,j= 0,0
        ans= []
        while(i<m and j <n):
            if nums1[i] >= nums2[j]:
                ans.append(nums2[j])
                j += 1
            else: 
                ans.append(nums1[i])
                i += 1
        while(i < m):
            ans.append(nums1[i])
            i += 1
        while(j<n):
            ans.append(nums2[j])
            j += 1
        return ans
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid= len(nums)//2
        node= Node(nums[mid])
        node.left=  self.sortedArrayToBST(nums[:mid])
        node.right= self.sortedArrayToBST(nums[mid+1:])
        return node

# Java
"""
import java.util.*;

class Node {
    int data;
    Node left, right;

    Node(int val) {
        this.data = val;
        left = right = null;
    }
}

class Solution {

    public List<Integer> merge(Node root1, Node root2) {
        List<Integer> inorder1 = inorderIterative(root1);
        List<Integer> inorder2 = inorderIterative(root2);
        List<Integer> mergedArray = mergeSortedArray(inorder1, inorder2);
        Node root = sortedArrayToBST(mergedArray, 0, mergedArray.size() - 1);
        return inorderIterative(root);
    }

    public List<Integer> inorderIterative(Node root) {
        List<Integer> ans = new ArrayList<>();
        Stack<Node> stack = new Stack<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            Node curr = stack.pop();
            ans.add(curr.data);
            root = curr.right;
        }
        return ans;
    }

    public List<Integer> mergeSortedArray(List<Integer> nums1, List<Integer> nums2) {
        List<Integer> ans = new ArrayList<>();
        int i = 0, j = 0;
        int m = nums1.size(), n = nums2.size();

        while (i < m && j < n) {
            if (nums1.get(i) >= nums2.get(j)) {
                ans.add(nums2.get(j++));
            } else {
                ans.add(nums1.get(i++));
            }
        }

        while (i < m) {
            ans.add(nums1.get(i++));
        }

        while (j < n) {
            ans.add(nums2.get(j++));
        }

        return ans;
    }

    public Node sortedArrayToBST(List<Integer> nums, int start, int end) {
        if (start > end) return null;
        int mid = (start + end) / 2;
        Node node = new Node(nums.get(mid));
        node.left = sortedArrayToBST(nums, start, mid - 1);
        node.right = sortedArrayToBST(nums, mid + 1, end);
        return node;
    }
}
"""
