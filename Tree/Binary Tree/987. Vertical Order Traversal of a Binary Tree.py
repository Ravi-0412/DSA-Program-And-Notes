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

# Java
"""
class Solution {
    private int minHD, maxHD;
    private Map<Integer, List<int[]>> map = new HashMap<>();
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        minHD = 0;
        maxHD = 0;
        dfs(root, 0, 0);
        
        List<List<Integer>> ans = new ArrayList<>();
        for (int hori = minHD; hori <= maxHD; hori++) {
            List<int[]> nodes = map.getOrDefault(hori, new ArrayList<>());
            nodes.sort((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
            List<Integer> level = new ArrayList<>();
            for (int[] node : nodes) {
                level.add(node[1]);
            }
            ans.add(level);
        }
        return ans;
    }
    
    private void dfs(TreeNode root, int lvl_h, int lvl_v) {
        if (root == null) {
            return;
        }
        minHD = Math.min(minHD, lvl_h);
        maxHD = Math.max(maxHD, lvl_h);
        
        map.putIfAbsent(lvl_h, new ArrayList<>());
        map.get(lvl_h).add(new int[]{lvl_v, root.val});
        
        dfs(root.left, lvl_h - 1, lvl_v + 1);
        dfs(root.right, lvl_h + 1, lvl_v + 1);
    }
}
"""

# Java code using 'Treemap and Heap'
"""
import java.util.*;

class Solution {
    // TreeMap to store nodes based on horizontal distance (lvl_h) and vertical distance (lvl_v)
    private Map<Integer, TreeMap<Integer, PriorityQueue<Integer>>> map = new TreeMap<>();
    
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        // Perform DFS traversal to populate the map
        dfs(root, 0, 0);
        
        List<List<Integer>> ans = new ArrayList<>();
        // Iterate over horizontal distances in sorted order
        for (TreeMap<Integer, PriorityQueue<Integer>> ys : map.values()) {
            List<Integer> level = new ArrayList<>();
            // Iterate over vertical levels in sorted order
            for (PriorityQueue<Integer> nodes : ys.values()) {
                // Extract nodes in sorted order (since PriorityQueue sorts them automatically)
                while (!nodes.isEmpty()) {
                    level.add(nodes.poll());
                }
            }
            ans.add(level); // Add sorted nodes for this horizontal level to the answer
        }
        return ans;
    }
    
    private void dfs(TreeNode root, int lvl_h, int lvl_v) {
        if (root == null) {
            return;
        }
        
        // Insert node into the map at the correct (horizontal, vertical) position
        map.putIfAbsent(lvl_h, new TreeMap<>());
        map.get(lvl_h).putIfAbsent(lvl_v, new PriorityQueue<>());
        map.get(lvl_h).get(lvl_v).offer(root.val);
        
        // Recursively traverse left and right children
        dfs(root.left, lvl_h - 1, lvl_v + 1); // Move left: decrease horizontal level, increase vertical level
        dfs(root.right, lvl_h + 1, lvl_v + 1); // Move right: increase horizontal level, increase vertical level
    }
}

"""

# C++ Code 
"""
class Solution {
public:
    int minHD, maxHD;
    unordered_map<int, vector<pair<int, int>>> map;  // {horizontal level -> list of {vertical level, node value}}

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        minHD = 0;
        maxHD = 0;
        dfs(root, 0, 0);

        vector<vector<int>> ans;
        for (int hori = minHD; hori <= maxHD; ++hori) {
            vector<pair<int, int>>& nodes = map[hori];
            sort(nodes.begin(), nodes.end());  // sort by vertical level, then by node value
            vector<int> level;
            for (auto& node : nodes) {
                level.push_back(node.second);
            }
            ans.push_back(level);
        }
        return ans;
    }

    void dfs(TreeNode* root, int lvl_h, int lvl_v) {
        if (!root) return;
        minHD = min(minHD, lvl_h);
        maxHD = max(maxHD, lvl_h);

        map[lvl_h].emplace_back(lvl_v, root->val);

        dfs(root->left, lvl_h - 1, lvl_v + 1);
        dfs(root->right, lvl_h + 1, lvl_v + 1);
    }
};

"""

# C++ code using 'Treemap and Heap'
"""
class Solution {
public:
    // map<horizontal level, map<vertical level, min-heap of node values>>
    map<int, map<int, priority_queue<int, vector<int>, greater<int>>>> map;

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        dfs(root, 0, 0);

        vector<vector<int>> ans;
        for (auto& [lvl_h, verticalMap] : map) {
            vector<int> level;
            for (auto& [lvl_v, pq] : verticalMap) {
                while (!pq.empty()) {
                    level.push_back(pq.top());
                    pq.pop();
                }
            }
            ans.push_back(level);
        }
        return ans;
    }

    void dfs(TreeNode* root, int lvl_h, int lvl_v) {
        if (!root) return;

        map[lvl_h][lvl_v].push(root->val);

        dfs(root->left, lvl_h - 1, lvl_v + 1);  // Move left: decrease horizontal level, increase vertical level
        dfs(root->right, lvl_h + 1, lvl_v + 1); // Move right: increase horizontal level, increase vertical level
    }
};

"""
# do by iterative way later all the view based q

# Related Q:
# 1) Top View of Binary Tree
# ans: you have to print the 1st node at each horizontal level from top(minimum x_coodinate)

# 2) Bottom View of Binary Tree
# Ans: you have to print the 1st node at each horizonatl level from bottom(maximum x_coordinate)
