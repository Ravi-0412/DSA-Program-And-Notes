# method 1: 

# Brute force :
"""
find the minimum horizontal distance and maximum horizontal distance, 
by taking distance of left child as '-1' and for right child as '+1'.
Minimum will be for leftmost leaf node and max will be rightmost leaf node

vvi: for coordinates: just stand at root(assume root as origin as given also) (0,0) and reverse the axis i.e row -> x and col -> y.
horizontal -> y axis and vertical is x-axis.
Same way we convert the coordinates into matrix.

so just think we are printing horizonatlly from min_horizontal to max_horizontal

now for each horizonatl distance in range find all the nodes matching to given horizontal distance and add into the ans
time: O(n^2) , for each horizontal level we find the nodes that matches with given horizonatl level
Note: this will not print the node in sorted value when they belong to same vertical and horizonatl level (work on GFG but not on leetcode).
"""

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.min_h, self.max_h= 0, 0
        # find the minimum and maximum horizontal distance in the tree
        # min will be at leftmost root and maximum will be at rightmost root
        self.FindHD(root, self.minHD, self.maxHD,0)  # also a traversal only  preorder
        print(self.minHD, self.maxHD)
        
        # now print the node from minHD to maxHD which matches with the given horizontal distance
        ans= []
        for line in range(self.minHD, self.maxHD +1):
            level= []
            self.PrintNode(root, level, line, 0)      # it just a traversal totally preorder
            ans.append(level)
        return ans
    
    # hd: taking horizontal distance of left child to be -1 and for right child +1
    def FindHD(self, root, minHD, maxHD, hd):
        if root== None:
            return
        # update minHd and maxHD every time
        minHD= min(minHD,hd)
        maxHD= max(maxHD,hd)
        self.FindHD(root.left, minHD, maxHD, hd-1)
        self.FindHD(root.right, minHD, maxHD, hd+1)
    
    # if node level hd matches with level just add that into the ans
    # just a preorder traversal(you can apply any but preorder will be more easier and readable)
    def PrintNode(self, root, level, line , hd):
        if root== None:
            return 
        if hd== line:
            level.append(root.val)
        self.PrintNode(root.left, level, line , hd-1)
        self.PrintNode(root.right, level, line , hd+1)

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int minHD = 0, maxHD = 0;

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        // find the minimum and maximum horizontal distance in the tree
        // min will be at leftmost root and maximum will be at rightmost root
        FindHD(root, 0);  // also a traversal only  preorder
        System.out.println(minHD + " " + maxHD);

        // now print the node from minHD to maxHD which matches with the given horizontal distance
        List<List<Integer>> ans = new ArrayList<>();
        for (int line = minHD; line <= maxHD; line++) {
            List<Integer> level = new ArrayList<>();
            PrintNode(root, level, line, 0);  // it just a traversal totally preorder
            ans.add(level);
        }
        return ans;
    }

    // hd: taking horizontal distance of left child to be -1 and for right child +1
    void FindHD(TreeNode root, int hd) {
        if (root == null) {
            return;
        }
        // update minHd and maxHD every time
        minHD = Math.min(minHD, hd);
        maxHD = Math.max(maxHD, hd);
        FindHD(root.left, hd - 1);
        FindHD(root.right, hd + 1);
    }

    // if node level hd matches with level just add that into the ans
    // just a preorder traversal(you can apply any but preorder will be more easier and readable)
    void PrintNode(TreeNode root, List<Integer> level, int line, int hd) {
        if (root == null) {
            return;
        }
        if (hd == line) {
            level.add(root.val);
        }
        PrintNode(root.left, level, line, hd - 1);
        PrintNode(root.right, level, line, hd + 1);
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int minHD = 0, maxHD = 0;

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        // find the minimum and maximum horizontal distance in the tree
        // min will be at leftmost root and maximum will be at rightmost root
        FindHD(root, 0);  // also a traversal only  preorder
        cout << minHD << " " << maxHD << endl;

        // now print the node from minHD to maxHD which matches with the given horizontal distance
        vector<vector<int>> ans;
        for (int line = minHD; line <= maxHD; ++line) {
            vector<int> level;
            PrintNode(root, level, line, 0);  // it just a traversal totally preorder
            ans.push_back(level);
        }
        return ans;
    }

    // hd: taking horizontal distance of left child to be -1 and for right child +1
    void FindHD(TreeNode* root, int hd) {
        if (!root) return;
        // update minHd and maxHD every time
        minHD = min(minHD, hd);
        maxHD = max(maxHD, hd);
        FindHD(root->left, hd - 1);
        FindHD(root->right, hd + 1);
    }

    // if node level hd matches with level just add that into the ans
    // just a preorder traversal(you can apply any but preorder will be more easier and readable)
    void PrintNode(TreeNode* root, vector<int>& level, int line, int hd) {
        if (!root) return;
        if (hd == line) {
            level.push_back(root->val);
        }
        PrintNode(root->left, level, line, hd - 1);
        PrintNode(root->right, level, line, hd + 1);
    }
};
"""

# method 2:
"""
time; O(n*logn). for hashmap buliding its O(n) only but for adding into ans we have to sort the node at each level so n*logn.

hashmap will store all the nodes at same horizontal level with (vertical_level, node_val)
since we have to print horizontally(from min_x to max_x) so made horizonatl_level as key. 

And while printing, we will print the node from top to bottom at each level i.e min_vertical to max_vertical.
That's why we are adding "vertical_level value" also with node value.

and in case of  same x and y , we have to take the node with minimum value x.
for this, so before adding any value to the ans sort the each key pair by vertical_level

"""
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.min_h, self.max_h= 0, 0  # minimum horizonatl level and maximum horizontal level
        dic= collections.defaultdict(list)   # [horizontal_level:(vertcial_level, node.val)]

        # level horizontal, level vertical.. just preorder logic only. same we did in above method to find the horizontal range
        def dfs(root, lvl_h, lvl_v):   
            if root== None:
                return
            self.min_h= min(self.min_h, lvl_h)
            self.max_h= max(self.max_h, lvl_h)
            dic[lvl_h].append((lvl_v, root.val))
            dfs(root.left, lvl_h-1, lvl_v+1)     # left node lies at (col-1,row+1), horizontal level->column and vertical level -> row
            dfs(root.right, lvl_h+1, lvl_v+1)    # right node lies at (col-1,row+1)
        
        dfs(root,0,0)   # just a traversla can say preorder

        ans, level= [],[]
        # now print the all nodes horizonatl level wise, and store the value by key before adding into ans for same vertcial level
        for hori in range(self.min_h, self.max_h + 1):
            for key, val in sorted(dic[hori]):    # will sort the the value according to the 1st ele in value
                level.append(val)
            ans.append(level) 
            level = []  # make level empty after each horizontal level to store the ans for next level
        return ans

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int min_h = 0, max_h = 0;  // minimum horizonatl level and maximum horizontal level
    Map<Integer, List<int[]>> map = new HashMap<>();  // [horizontal_level:(vertcial_level, node.val)]

    public List<List<Integer>> verticalTraversal(TreeNode root) {
        dfs(root, 0, 0);   // just a traversla can say preorder

        List<List<Integer>> ans = new ArrayList<>();
        // now print the all nodes horizonatl level wise, and store the value by key before adding into ans for same vertcial level
        for (int hori = min_h; hori <= max_h; hori++) {
            List<int[]> pairs = map.get(hori);
            Collections.sort(pairs, (a, b) -> a[0] == b[0] ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]));
            List<Integer> level = new ArrayList<>();
            for (int[] p : pairs) {
                level.add(p[1]);
            }
            ans.add(level); 
        }
        return ans;
    }

    // level horizontal, level vertical.. just preorder logic only. same we did in above method to find the horizontal range
    void dfs(TreeNode root, int lvl_h, int lvl_v) {
        if (root == null) {
            return;
        }
        min_h = Math.min(min_h, lvl_h);
        max_h = Math.max(max_h, lvl_h);
        map.computeIfAbsent(lvl_h, k -> new ArrayList<>()).add(new int[]{lvl_v, root.val});
        dfs(root.left, lvl_h - 1, lvl_v + 1);  // left node lies at (col-1,row+1), horizontal level->column and vertical level -> row
        dfs(root.right, lvl_h + 1, lvl_v + 1); // right node lies at (col+1,row+1)
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int min_h = 0, max_h = 0;  // minimum horizonatl level and maximum horizontal level
    map<int, vector<pair<int, int>>> dic;   // [horizontal_level:(vertcial_level, node.val)]

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        dfs(root, 0, 0);   // just a traversla can say preorder

        vector<vector<int>> ans;
        // now print the all nodes horizonatl level wise, and store the value by key before adding into ans for same vertcial level
        for (int hori = min_h; hori <= max_h; ++hori) {
            vector<pair<int, int>>& vec = dic[hori];
            sort(vec.begin(), vec.end());  // will sort the the value according to the 1st ele in value
            vector<int> level;
            for (auto& [v, val] : vec) {
                level.push_back(val);
            }
            ans.push_back(level);
        }
        return ans;
    }

    // level horizontal, level vertical.. just preorder logic only. same we did in above method to find the horizontal range
    void dfs(TreeNode* root, int lvl_h, int lvl_v) {
        if (!root) return;
        min_h = min(min_h, lvl_h);
        max_h = max(max_h, lvl_h);
        dic[lvl_h].emplace_back(lvl_v, root->val);
        dfs(root->left, lvl_h - 1, lvl_v + 1);  // left node lies at (col-1,row+1)
        dfs(root->right, lvl_h + 1, lvl_v + 1); // right node lies at (col+1,row+1)
    }
};
"""