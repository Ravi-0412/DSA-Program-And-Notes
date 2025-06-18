# method 1: 

# just store the path for both the nodes in two separate array 
# LCA: will be that node from that last where the path of both the nodes will match from the last.

# Now Q reduces to: "Given Two arrays, find the the first ele common in both the array from last".
# use Two pointer and for moving pointer: decr that index which is more. if equal decr both.
# time: O(n)= space

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q= [],[]
        # find the path for both p and q
        self.path(root, p.val, path_p)   # i was passing only p so was getting path_p and path_q as empty
        self.path(root, q.val, path_q)
        i,j= len(path_p)-1 , len(path_q)-1
        while i>=0 and j>=0:
            if path_p[i]== path_q[j]:
                return path_p[i]
            # in case didn't match.
            elif i > j:  # only decr 'i'. means no of ele in path1 is more
                i -= 1
            elif j > i:   # only decr 'j'. means no of ele in path2 is more
                j -= 1
            else:  # it means remainging no of ele in both is same. 
                i,j = i-1, j-1

    def path(self,root,key,ans):  
        if root== None:
            return False
        ans.append(root)  # simply add the node you visit   # when i am writing ans.append(root.val), it's giving error so chnegd liked thsio don't know why
        if root.val== key:
            return True
        if self.path(root.left,key,ans) or self.path(root.right,key,ans):  # means key has path from the given root
            return True
        # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
        ans.pop()
        return False



# 2nd method: 
# very better and very logical 
"""
Optimising the space complexity to O(1)
Here we are sure that both the nodes are present in the tree so we can utilise this.

LCA: wo node hoga jahan pe bottom se dono node 1st time differ karenge i.e means is node ka left subtree ek node ko contain karega 
and right subtree dusre node ko.
So just apply bottom up Approach and if at any node if its both the left and right subtree give not None , it means curr node is LCA.

One of the node can be the LCA also, so in this case one will have 'None'(doesn't contain any of the node) and other will have 'Not None'.
then in this case the node with 'not None' will be LCA.

Note: Here once we find the and then we will start returning ans from there itself.
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return None
        if root== p or root== q:  # then return that node to the parent
            return root
        # if not equal to the nodes value then search on both left and right side
        left_search=  self.lowestCommonAncestor(root.left, p , q)
        right_search= self.lowestCommonAncestor(root.right, p , q)
        # if left_search is None and then right subtree contains both the nodes
        if left_search== None:
            return right_search
        # if left_search is not None then left subtree conatins both the nodes
        if right_search== None:
            return left_search
        # now it means both of the 'left' and 'right' part is None means both contain one of the two node.
        # so root will be LCA only, from here both node has went to different subtree.
        return root 

# Java Code 
"""
// method 1: 


class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> path_p = new ArrayList<>();
        List<TreeNode> path_q = new ArrayList<>();
        // find the path for both p and q
        path(root, p.val, path_p);   // i was passing only p so was getting path_p and path_q as empty
        path(root, q.val, path_q);
        int i = path_p.size() - 1, j = path_q.size() - 1;
        while (i >= 0 && j >= 0) {
            if (path_p.get(i) == path_q.get(j)) {
                return path_p.get(i);
            }
            // in case didn't match.
            else if (i > j) {  // only decr 'i'. means no of ele in path1 is more
                i -= 1;
            } else if (j > i) {   // only decr 'j'. means no of ele in path2 is more
                j -= 1;
            } else {  // it means remainging no of ele in both is same. 
                i -= 1;
                j -= 1;
            }
        }
        return null;
    }

    public boolean path(TreeNode root, int key, List<TreeNode> ans) {
        if (root == null) {
            return false;
        }
        ans.add(root);  // simply add the node you visit   // when i am writing ans.append(root.val), it's giving error so chnegd liked thsio don't know why
        if (root.val == key) {
            return true;
        }
        if (path(root.left, key, ans) || path(root.right, key, ans)) {  // means key has path from the given root
            return true;
        }
        // if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
        ans.remove(ans.size() - 1);
        return false;
    }
}

// 2nd method: 

class Solution2 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        }
        if (root == p || root == q) {  // then return that node to the parent
            return root;
        }
        // if not equal to the nodes value then search on both left and right side
        TreeNode left_search = lowestCommonAncestor(root.left, p, q);
        TreeNode right_search = lowestCommonAncestor(root.right, p, q);
        // if left_search is None and then right subtree contains both the nodes
        if (left_search == null) {
            return right_search;
        }
        // if left_search is not None then left subtree conatins both the nodes
        if (right_search == null) {
            return left_search;
        }
        // now it means both of the 'left' and 'right' part is None means both contain one of the two node.
        // so root will be LCA only, from here both node has went to different subtree.
        return root;
    }
}
"""

# C++ Code 
"""
// method 1: 

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        vector<TreeNode*> path_p, path_q;
        // find the path for both p and q
        path(root, p->val, path_p);   // i was passing only p so was getting path_p and path_q as empty
        path(root, q->val, path_q);
        int i = path_p.size() - 1, j = path_q.size() - 1;
        while (i >= 0 && j >= 0) {
            if (path_p[i] == path_q[j]) {
                return path_p[i];
            }
            // in case didn't match.
            else if (i > j) {  // only decr 'i'. means no of ele in path1 is more
                i -= 1;
            } else if (j > i) {   // only decr 'j'. means no of ele in path2 is more
                j -= 1;
            } else {  // it means remainging no of ele in both is same. 
                i -= 1;
                j -= 1;
            }
        }
        return nullptr;
    }

    bool path(TreeNode* root, int key, vector<TreeNode*>& ans) {
        if (root == nullptr) {
            return false;
        }
        ans.push_back(root);  // simply add the node you visit   // when i am writing ans.append(root.val), it's giving error so chnegd liked thsio don't know why
        if (root->val == key) {
            return true;
        }
        if (path(root->left, key, ans) || path(root->right, key, ans)) {  // means key has path from the given root
            return true;
        }
        // if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
        ans.pop_back();
        return false;
    }
};

// 2nd method: 

class Solution2 {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == nullptr) {
            return nullptr;
        }
        if (root == p || root == q) {  // then return that node to the parent
            return root;
        }
        // if not equal to the nodes value then search on both left and right side
        TreeNode* left_search = lowestCommonAncestor(root->left, p, q);
        TreeNode* right_search = lowestCommonAncestor(root->right, p, q);
        // if left_search is None and then right subtree contains both the nodes
        if (left_search == nullptr) {
            return right_search;
        }
        // if left_search is not None then left subtree conatins both the nodes
        if (right_search == nullptr) {
            return left_search;
        }
        // now it means both of the 'left' and 'right' part is None means both contain one of the two node.
        // so root will be LCA only, from here both node has went to different subtree.
        return root;
    }
};
"""

# Related Q:
# 1) 235. Lowest Common Ancestor of a Binary Search Tree

