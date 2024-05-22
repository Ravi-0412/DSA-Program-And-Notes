# Method 1:

# just same logic as Q: 105
# only difference in indexing because of working of postorder and inorder together
# time:O(n^2)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder: return None
        root= TreeNode(postorder[-1])   # this will the parent for the cur subtree.
        # now find its child i.e which all nodes will come to the left and right.
        # find the index of last ele of postorder in inorder
        ind= inorder.index(postorder[-1])  
        
        # all the ele before the indx in inorder will come to the left subtree.
        # and all nodes till index 'ind' in postorder will come to the left subtree
        root.left=  self.buildTree(inorder[:ind], postorder[:ind])
        
        # all the ele after the index ind in inorder will come to the right subtree
        # and all from the index 'ind' and excluding the last one in postorder will come to the right subtree
        root.right= self.buildTree(inorder[ind+1:], postorder[ind :-1])  
        return root


# Method 2:
# Optimising to O(n)

# Note: if you will call first for 'left' rather than right then it won't work
# because we are taking help of postorder index (using pop) and 
# postorder goes from right to left.
class Solution:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): 
            map_inorder[val] = i
        # low, high: leftmost/ rightmost index of ele in inorder for current subtree
        def recur(low, high): 
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x

        return recur(0, len(inorder) -1)


# Java
"""
// method 1: in O(n)

public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null || inorder.length == 0 || postorder.length == 0)
            return null;
        
        HashMap<Integer, Integer> inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        
        return buildTreeRecursive(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1, inorderIndexMap);
    }
    
    private TreeNode buildTreeRecursive(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd, HashMap<Integer, Integer> inorderIndexMap) {
        if (inStart > inEnd || postStart > postEnd)
            return null;
        
        TreeNode root = new TreeNode(postorder[postEnd]);
        int rootIndexInInorder = inorderIndexMap.get(root.val);
        int leftSubtreeSize = rootIndexInInorder - inStart;
        
        root.left = buildTreeRecursive(inorder, inStart, rootIndexInInorder - 1, postorder, postStart, postStart + leftSubtreeSize - 1, inorderIndexMap);
        root.right = buildTreeRecursive(inorder, rootIndexInInorder + 1, inEnd, postorder, postStart + leftSubtreeSize, postEnd - 1, inorderIndexMap);
        
        return root;
    }
}

// method 2:
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null || inorder.length == 0 || postorder.length == 0)
            return null;
        
        HashMap<Integer, Integer> inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        
        return buildTreeRecursive(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1, inorderIndexMap);
    }
    
    private TreeNode buildTreeRecursive(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd, HashMap<Integer, Integer> inorderIndexMap) {
        if (inStart > inEnd || postStart > postEnd)
            return null;
        
        TreeNode root = new TreeNode(postorder[postEnd]);
        int rootIndexInInorder = inorderIndexMap.get(root.val);
        int leftSubtreeSize = rootIndexInInorder - inStart;
        
        root.right = buildTreeRecursive(inorder, rootIndexInInorder + 1, inEnd, postorder, postStart + leftSubtreeSize, postEnd - 1, inorderIndexMap);
        root.left = buildTreeRecursive(inorder, inStart, rootIndexInInorder - 1, postorder, postStart, postStart + leftSubtreeSize - 1, inorderIndexMap);
        
        return root;
    }
}

"""