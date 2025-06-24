# when you will append any new child node then it always will get added with num= 1 as for chils
# it's 1st time so num = 1.
# and for node just check the one next child that comes in meaning of that traversal after printing the root like:
# for preorder next will be 'left', for inorder next will be 'right' and for postorder next will be nothing

# after updating num, add the poped node into the stack with updated num  and 
# check for next child that comes in meaning of that traversal,
# if child then add its child with num= num+1   

# VVI: basically 'num' means the curr node will be added '3-num' times more including all the ans
# since any node can be added max '3' times including all the three traversal.(as it has to come one time in each traversal)
# so for any node if num= 1 means this node has been added '1' time and '3-1' times it will be  added more

# and according to the print statement position(that's what num mean) we decide in what traversal we have to add that node at present time
# like for preorder(root,left,right), print statement comes first. so we have to add any node in ans when num==1 and so on.

# stack will be initialised with (root,1), where num= 1
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre, inorder,post,stack= [],[],[],[(root,1)]
        while stack:
            curr, num= stack.pop()  # every time pop first and check the value of num
            # preorder i.e num == 1 means this node is printed for the 1st time. 
            if num== 1:  # add in preorder and make num= 2(to make this node get included in inorder) 
                        # and then again append curr in stack with updated num
                pre.append(curr.val)
                num= 2
                stack.append((curr,num))
                # if left child exixt then append that with num= 1
                if curr.left:
                    num= 1
                    stack.append((curr.left,num))
            # Inorder case 
            elif num== 2:  # add in inorder and make num= 3 and then again append curr in stack with updated num
                inorder.append(curr.val)
                num= 3
                stack.append((curr,num))
                # if right child exixt then append that with num= 1
                if curr.right:
                    num= 1
                    stack.append((curr.right,num))
            # postorder
            elif num==3:
                post.append(curr.val)
        
        print(pre,inorder,post)

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Pair {
    TreeNode node;
    int num;
    Pair(TreeNode node, int num) {
        this.node = node;
        this.num = num;
    }
}

class Solution {
    public void postorderTraversal(TreeNode root) {
        List<Integer> pre = new ArrayList<>();
        List<Integer> inorder = new ArrayList<>();
        List<Integer> post = new ArrayList<>();
        Stack<Pair> stack = new Stack<>();

        if (root != null) {
            stack.push(new Pair(root, 1));
        }

        while (!stack.isEmpty()) {
            Pair p = stack.pop();  // every time pop first and check the value of num
            TreeNode curr = p.node;
            int num = p.num;

            // preorder i.e num == 1 means this node is printed for the 1st time. 
            if (num == 1) {  // add in preorder and make num= 2(to make this node get included in inorder) 
                             // and then again append curr in stack with updated num
                pre.add(curr.val);
                num = 2;
                stack.push(new Pair(curr, num));
                // if left child exixt then append that with num= 1
                if (curr.left != null) {
                    num = 1;
                    stack.push(new Pair(curr.left, num));
                }
            }

            // Inorder case 
            else if (num == 2) {  // add in inorder and make num= 3 and then again append curr in stack with updated num
                inorder.add(curr.val);
                num = 3;
                stack.push(new Pair(curr, num));
                // if right child exixt then append that with num= 1
                if (curr.right != null) {
                    num = 1;
                    stack.push(new Pair(curr.right, num));
                }
            }

            // postorder
            else if (num == 3) {
                post.add(curr.val);
            }
        }

        System.out.println(pre + " " + inorder + " " + post);
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void postorderTraversal(TreeNode* root) {
        vector<int> pre, inorder, post;
        stack<pair<TreeNode*, int>> stack;

        if (root != nullptr) {
            stack.push({root, 1});
        }

        while (!stack.empty()) {
            auto [curr, num] = stack.top(); stack.pop();  // every time pop first and check the value of num

            // preorder i.e num == 1 means this node is printed for the 1st time. 
            if (num == 1) {  // add in preorder and make num= 2(to make this node get included in inorder) 
                             // and then again append curr in stack with updated num
                pre.push_back(curr->val);
                num = 2;
                stack.push({curr, num});
                // if left child exixt then append that with num= 1
                if (curr->left) {
                    num = 1;
                    stack.push({curr->left, num});
                }
            }

            // Inorder case 
            else if (num == 2) {  // add in inorder and make num= 3 and then again append curr in stack with updated num
                inorder.push_back(curr->val);
                num = 3;
                stack.push({curr, num});
                // if right child exixt then append that with num= 1
                if (curr->right) {
                    num = 1;
                    stack.push({curr->right, num});
                }
            }

            // postorder
            else if (num == 3) {
                post.push_back(curr->val);
            }
        }

        for (int v : pre) cout << v << " "; cout << endl;
        for (int v : inorder) cout << v << " "; cout << endl;
        for (int v : post) cout << v << " "; cout << endl;
    }
};
"""