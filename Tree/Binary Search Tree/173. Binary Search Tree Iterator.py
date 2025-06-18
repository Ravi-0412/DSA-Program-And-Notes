
# Method 1:

"""
reducing the space complexity to O(H)
first push all the left ele of root i.e inorder traversal rule
for 'next' just pop the node and push its right. like we do in inorder iterative traversal.

here we only pushing all the left node not all the nodes initially and when 'next' is called,
this will make sure that space complexity doesn't go beyond O(H).

Just similar way as "230. Kth smallest element in BST"

Here we need to 'pop' last inserted one for 'next' so we will use stack.

space: O(H)
time: O(1) average case. we are pushing 'n' ele and we are calling 'next' function 'n' times

"""
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack= []
        self.PushLeft(root)
        
    def next(self) -> int:
        temp= self.stack.pop()
        self.PushLeft(temp.right)  # we have already pushed the all the 'left' nodes so we only need to push the right one
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack!= []
    
    def PushLeft(self, root):
        # push everything that comes on the left of root including root
        curr= root
        while curr:
            self.stack.append(curr)
            curr= curr.left

# Java
"""
class BSTIterator {
    Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        PushLeft(root);
    }

    public int next() {
        TreeNode temp = stack.pop();
        PushLeft(temp.right);  // we have already pushed the all the 'left' nodes so we only need to push the right one
        return temp.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }

    public void PushLeft(TreeNode root) {
        // push everything that comes on the left of root including root
        TreeNode curr = root;
        while (curr != null) {
            stack.push(curr);
            curr = curr.left;
        }
    }
}


"""

#C++ Code 
"""
class BSTIterator {
public:
    stack<TreeNode*> stack;

    BSTIterator(TreeNode* root) {
        PushLeft(root);
    }
    
    int next() {
        TreeNode* temp = stack.top();
        stack.pop();
        PushLeft(temp->right);  // we have already pushed the all the 'left' nodes so we only need to push the right one
        return temp->val;
    }
    
    bool hasNext() {
        return !stack.empty();
    }
    
    void PushLeft(TreeNode* root) {
        // push everything that comes on the left of root including root
        TreeNode* curr = root;
        while (curr) {
            stack.push(curr);
            curr = curr->left;
        }
    }
};

"""

# the above approach can be used to solve:

# 1) 230.kth smallest ele in BST
# just count the no of function call for 'next' function for 1st one 

# 2) 653. Two Sum IV - Input is a BST




