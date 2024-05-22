# method 1:
# time: O(n^2). Because we are finding index each time 
# just do on pen and paper for visualisation like how slicing is doing perfect work.
# same logic as we used to do in GATE exam i.e:
# Preorder will decide the which ele will be the parent of the upcoming tree.
# preorder[0] will be the parent always.
# inorder will decide the which ele will go the left and right of the parent.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:  # or 'if preorder'
            root= TreeNode(preorder[0])   # this will be the root

            # find the index of 1st ele of prerorder in inorder to check all nodes will go the left of parent and right of parent.
            ind= inorder.index(preorder[0])
            # all the ele from index '1' till 'ind' will come to the left in preorder(1st ele already included.) and all the ele before the indx in inorder will come to the left subtree(ind ele already included)
            root.left=  self.buildTree(preorder[1:ind+1], inorder[:ind])
            # all the ele after the indx will come to right of both preorder and inorder.
            root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])                

            return root

# Method 2:
# We can optimise this to O(n) using map.
# Just store each element of inorder as key and its index as value in hashmap.

# Note vvi: if you will first add 'right' child than left then it won't work because
# you are taking help of preorder index and preorder index goes from left to right.
# Take any example and see.

class Solution:
    def __init__(self):
        self.preorderIndex = 0
        self.inorderIndexMap = {}

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Build a map to store value -> index relations from inorder array
        self.inorderIndexMap = {value: index for index, value in enumerate(inorder)}
        return self.buildTreeRecursive(preorder, 0, len(inorder) - 1)

    def buildTreeRecursive(self, preorder: List[int], left: int, right: int) -> Optional[TreeNode]:
        # Base case - no elements to construct the tree
        if left > right:
            return None

        # Select the preorderIndex element as the root and increment it
        rootValue = preorder[self.preorderIndex]
        self.preorderIndex += 1
        root = TreeNode(rootValue)

        # Build left and right subtree
        # Excluding inorderIndexMap[rootValue] element because it's the root
        root.left = self.buildTreeRecursive(preorder, left, self.inorderIndexMap[rootValue] - 1)
        root.right = self.buildTreeRecursive(preorder, self.inorderIndexMap[rootValue] + 1, right)

        return root
    

# Related Q:
# 1) 106. Construct Binary Tree from Inorder and Postorder Traversal


# Java
"""
// method 1: In O(n)
public class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (inorder == null || preorder == null || inorder.length == 0 || preorder.length == 0)
            return null;
        
        HashMap<Integer, Integer> inorderIndexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        
        return buildTreeRecursive(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1, inorderIndexMap);
    }
    
    private TreeNode buildTreeRecursive(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd, HashMap<Integer, Integer> inorderIndexMap) {
        if (preStart > preEnd || inStart > inEnd)
            return null;
        
        TreeNode root = new TreeNode(preorder[preStart]);
        int rootIndexInInorder = inorderIndexMap.get(root.val);
        int leftSubtreeSize = rootIndexInInorder - inStart;
        
        root.left = buildTreeRecursive(preorder, preStart + 1, preStart + leftSubtreeSize, inorder, inStart, rootIndexInInorder - 1, inorderIndexMap);
        root.right = buildTreeRecursive(preorder, preStart + leftSubtreeSize + 1, preEnd, inorder, rootIndexInInorder + 1, inEnd, inorderIndexMap);
        
        return root;
    }
}


// method 2:
class Solution {
    private int preorderIndex;
    private Map<Integer, Integer> inorderIndexMap;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preorderIndex = 0;
        inorderIndexMap = new HashMap<>();
        // Build a map to store value -> index relations from inorder array
        for (int i = 0; i < inorder.length; i++) {
            inorderIndexMap.put(inorder[i], i);
        }
        return buildTreeRecursive(preorder, 0, inorder.length - 1);
    }

    private TreeNode buildTreeRecursive(int[] preorder, int left, int right) {
        // Base case - no elements to construct the tree
        if (left > right) {
            return null;
        }

        // Select the preorderIndex element as the root and increment it
        int rootValue = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootValue);

        // Build left and right subtree
        // Excluding inorderIndexMap.get(rootValue) element because it's the root
        root.left = buildTreeRecursive(preorder, left, inorderIndexMap.get(rootValue) - 1);
        root.right = buildTreeRecursive(preorder, inorderIndexMap.get(rootValue) + 1, right);

        return root;
    }
}
"""