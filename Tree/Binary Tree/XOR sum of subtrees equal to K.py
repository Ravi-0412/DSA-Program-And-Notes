"""
Q) Assign a value (0 or 1) to each node in a Binary Tree such that the sum of the "XOR-costs" of all subtrees equals a target value K.
"""

"""
Thought Process & Logic:
The "Path" Insight:
A value assigned to node u contributes to the XOR-sum of u itself, its parent, its grandparent, and every ancestor up to the root.
If node u is at depth d (root = depth 1), its value is included in exactly d subtree XOR-sums.

The "Independence" Strategy:
To keep the math simple and avoid 1 ^ 1 = 0 (which happens if you pick two nodes in the same vertical path), we use a Greedy Leaf-to-Root approach:
1. If we pick a node u at depth d and set it to 1, and ensure no nodes in its subtree are 1, then the XOR-sum of u and all its ancestors becomes 1.
2. This adds exactly d to our Total Cost.
3. Once we "use" a node to satisfy part of K, we cannot use any of its ancestors or descendants, because that would flip the XOR-sums back to 0 or complicate the sum.

Summary:
Observation: A node at depth d contributes its value to exactly d subtrees.
Constraint: The XOR property (1 ^ 1 = 0) means if we pick two nodes on the same path, they "cancel" each other out for all common ancestors.
Greedy Solution: To avoid cancellation, we pick a node and "lock" its entire path to the root. 
  We prefer deeper nodes first to satisfy larger portions of K quickly.
Complexity: O(N * log N) for sorting or O(N) with bucket sort. The ancestor marking is O(N *H), where H is the tree height.

Common doubts :
1) it is just that you are marking every leaf node as '1' since we are starting from deepest first?
-> we usually start with leaves, but we don't only use leaves. if remaining target < depth of leave then we skip, in this way we take middle nodes also.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def solve(self, root, n, k):
        # 1. Map out the tree structure
        depths = [] # (depth, node_id, node_ptr)
        parents = {}
        
        def dfs_info(node, d, p):
            if not node: return
            depths.append((d, node.val, node))
            parents[node] = p
            dfs_info(node.left, d + 1, node)
            dfs_info(node.right, d + 1, node)
            
        dfs_info(root, 1, None)
        
        # 2. Sort by depth descending (process deepest nodes first)
        depths.sort(key=lambda x: x[0], reverse=True)
        
        res = [0] * n
        used_in_path = [False] * n # Tracks if a node's XOR contribution is "locked"
        
        # 3. Greedy approach to reach target K
        target = k
        for d, node_id, node_ptr in depths:
            # If this node hasn't been affected by a child and depth fits in remaining K
            if not used_in_path[node_id] and d <= target:
                res[node_id] = 1
                target -= d
                
                # Mark this node and ALL its ancestors as 'used'
                # This ensures we don't pick another node on this path 
                # which would flip the XOR result (1^1=0)
                curr = node_ptr
                while curr:
                    used_in_path[curr.val] = True
                    curr = parents[curr]
                    
        return res if target == 0 else "Impossible"

# Helper to verify the total cost
def calculate_actual_cost(node, assignments):
    total = 0
    def dfs(u):
        nonlocal total
        if not u: return 0
        current_xor = assignments[u.val] ^ dfs(u.left) ^ dfs(u.right)
        total += current_xor
        return current_xor
    dfs(node)
    return total
# --- YOUR CODE END ---

def run_test(name, root, n, k):
    print(f"--- Running Test: {name} ---")
    print(f"Target K: {k}")
    sol = Solution()
    result = sol.solve(root, n, k)
    
    if result == "Impossible":
        print("Result: Impossible (As expected or failed to find solution)")
    else:
        print(f"Assignments (Node ID: Value): {result}")
        actual = calculate_actual_cost(root, result)
        print(f"Verified XOR Total Cost: {actual}")
        print("Success!" if actual == k else "FAILED!")
    print("\n")

# --- BUILDING TEST CASES ---

# Case 1: Linear Tree (Path) 0 -> 1 -> 2 -> 3
# Depths: 0(1), 1(2), 2(3), 3(4)
root1 = TreeNode(0)
root1.left = TreeNode(1)
root1.left.left = TreeNode(2)
root1.left.left.left = TreeNode(3)
# We want K = 3 (Should pick node at depth 3)
run_test("Linear Tree (Target K=3)", root1, 4, 3)
# We want K = 4 (Should pick node at depth 4)
run_test("Linear Tree (Target K=4)", root1, 4, 4)

# Case 2: Balanced Tree
#      0 (1)
#    /   \
#   1(2)  2(2)
#  / \    / \
# 3(3)4(3)5(3)6(3)
root2 = TreeNode(0)
root2.left, root2.right = TreeNode(1), TreeNode(2)
root2.left.left, root2.left.right = TreeNode(3), TreeNode(4)
root2.right.left, root2.right.right = TreeNode(5), TreeNode(6)

# K = 5: Deepest is 3. 5-3 = 2. Then pick a node at depth 2 in other branch.
run_test("Balanced Tree (Target K=5)", root2, 7, 5)
# K = 1: Should just pick the root.
run_test("Balanced Tree (Target K=1)", root2, 7, 1)

# Case 3: Impossible Case
run_test("Impossible Case (K=100)", root2, 7, 100)

if __name__ == "__main__":
    pass # run_test calls are already above

# Other Parts: 
"""
Part 2: 
Q) Assign a value (0 or 1) to each node in a Binary Tree such that the sum of the "XOR-costs" of all subtrees equals a target value 1.
Ans : Make root node value = 1 , keeping all other nodes value = '0'.
"""

"""
Part 3: 
Q) Assign a value (0 or 1) to each node in a Binary Tree such that the sum of the "XOR-costs" of all subtrees equals a target value 0.
-> Make all node values = 0 including root.
"""

"""
Part 3 VVI: 
Q) Assign a value (0 or 1) to each node in a Binary Tree such that the "XOR-costs" of all every individual subtree = 1.
Ans : Make all leaves values = 1 since that is the only way to make leaevs subtrees value = 1 and then update the parent values based on other two children values going bottom to up.
At each parent (node):
1. If leaf : node value = 1
2. Else : node value = 1 ^(left child value + right child value) since we want opposite from xor sum of children to make XOR sum at current node = 1

for handling this in better way , we can return '0' when root == None as default 
And a dfs to assign values to other nodes going bottom to top.

mathematically:
current node value say V, it's left child value say : L & it's right child value say : R
for each node:
V ^ L ^ R = 1 (this what we want)
To get V, XOR both side by : L ^ R, we get:
V = 1 ^ L ^ R

Since we are building the tree specifically so that every child's subtree XOR-sum is 1, we can simplify:
If it's a leaf : L = 0, R = 0 => V = 1 ^ 0 ^ 0 = 1
If it has one child : L = 1, R = 0 => V = 1 ^ 1 ^ 0 = 1
if it has two child : L = 1, R = 1 => V = 1 ^ 1 ^ 1 = 1

Summary of the Rule
Leaf nodes are always 1.
Nodes with 1 child are always 0.
Nodes with 2 children are always 1.

Time : O(N)
"""

class TreeNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.left = None
        self.right = None

class Solution:
    def solve(self, root):
        """
        Assigns 0 or 1 to each node such that every subtree's XOR-sum is 1.
        """
        assignments = {}

        def dfs(node):
            if not node:
                # Base Case: Empty subtree XOR result is 0
                return 0
            
            # Post-order: Process children first to get their subtree XOR results
            # (Which we are forcing to be 1 if they exist)
            left_xor = dfs(node.left)
            right_xor = dfs(node.right)
            
            # Goal: node_val ^ left_xor ^ right_xor = 1
            # Solving for node_val: node_val = 1 ^ left_xor ^ right_xor
            assigned_val = 1 ^ left_xor ^ right_xor
            
            assignments[node.node_id] = assigned_val
            
            # We return 1 to the parent because we've guaranteed this subtree XORs to 1
            return 1

        dfs(root)
        return assignments

# --- Verification & Testing Utility ---

def verify_and_report(name, root, assignments):
    print(f"--- {name} ---")
    errors = []
    total_cost = 0

    def check(node):
        nonlocal total_cost
        if not node: return 0
        
        # Calculate XOR sum of current node and its two subtrees
        res = assignments[node.node_id] ^ check(node.left) ^ check(node.right)
        
        if res != 1:
            errors.append(f"Node {node.node_id} failed! XOR sum was {res}")
        
        total_cost += res
        return res

    check(root)
    
    if errors:
        for err in errors: print(f"❌ {err}")
    else:
        print(f"✅ All subtree XOR-sums are 1.")
        print(f"📊 Total Nodes (N): {len(assignments)} | Total XOR Cost: {total_cost}")
        print(f"💡 Values assigned: {assignments}")
    print("-" * 40)

# --- Test Case Construction ---

if __name__ == "__main__":
    sol = Solution()

    # 1. Full Binary Tree (3 nodes)
    #      0
    #    /   \
    #   1     2
    root1 = TreeNode(0)
    root1.left, root1.right = TreeNode(1), TreeNode(2)
    res1 = sol.solve(root1)
    verify_and_report("Full Binary Tree", root1, res1)

    # 2. Skewed Path Tree (3 nodes)
    #   0 -> 1 -> 2
    root2 = TreeNode(0)
    root2.left = TreeNode(1)
    root2.left.left = TreeNode(2)
    res2 = sol.solve(root2)
    verify_and_report("Skewed Path Tree", root2, res2)

    # 3. Asymmetrical Tree (5 nodes)
    #        0
    #       / \
    #      1   2
    #     / \
    #    3   4
    root3 = TreeNode(0)
    root3.left, root3.right = TreeNode(1), TreeNode(2)
    root3.left.left, root3.left.right = TreeNode(3), TreeNode(4)
    res3 = sol.solve(root3)
    verify_and_report("Asymmetrical Tree", root3, res3)

"""
Part 4: 
Q) Assign a value (0 or 1) to each node in a Binary Tree such that the sum(normal sum not XOR) of the cost all subtrees equals a target value K.

Thought Process & Logic: 
1. The Node's "Weight"
In a tree where we want to sum subtree costs, the contribution of any node i with a value of 1 is exactly its depth (d_i).
  Why? Because that node is part of d_i different subtrees (itself and all ancestors).
  This transforms the problem into: "Pick a subset of nodes whose depths sum to K."  => Subset Sum problem

2. Decision Tracking (The has_included Table):
Standard space-optimized DP (using only one or two rows) tells you if K is possible, but it "forgets" which nodes were used.
  We use a 2D boolean table has_included[node_index][current_sum].
  If we decide to include node i to reach a sum j, we mark this cell as True.

3. The Backtracking Phase:
Once the table is filled, we start at the final state: (Total Nodes, Target K).
  If has_included[i][current_sum] is True:
    Node i was part of the solution. Assign it 1.
    Move to the previous node (i-1) and reduce the target sum by that node's depth.
If False:
  Node i was not used. Assign it 0.
  Move to the previous node ($i-1$) with the same target sum.

Time : O(N * K) = space
"""

class TreeNode:
    def __init__(self, node_id, left=None, right=None):
        self.node_id = node_id  # Unique ID from 0 to n-1
        self.left = left
        self.right = right

class Solution:
    def findAssignments(self, root: TreeNode, n: int, K: int):
        """
        Goal: Assign 0 or 1 to each node such that sum of subtree costs = K.
        Complexity: Time O(N*K), Space O(N*K) for the decision table.
        """
        # --- Step 1: Extract Depths (Weights) ---
        # We need both the depth (the value we sum) and the node_id (the identity)
        node_metadata = [] # List of (depth, node_id)
        
        def traverse(node, depth):
            if not node:
                return
            node_metadata.append((depth, node.node_id))
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
            
        traverse(root, 1)

        # --- Step 2: Build the DP Table ---
        # dp[i][j] -> Can we reach sum 'j' using the first 'i' nodes?
        dp = [[False] * (K + 1) for _ in range(n + 1)]
        # has_included[i][j] -> Did we use node 'i' to achieve sum 'j'?
        has_included = [[False] * (K + 1) for _ in range(n + 1)]

        # Base case: A sum of 0 is always possible (by picking nothing)
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            node_depth, node_id = node_metadata[i-1]
            for current_target in range(1, K + 1):
                # Option A: Exclude this node. 
                # Check if the previous state (i-1) could already achieve this sum.
                dp[i][current_target] = dp[i-1][current_target]
                
                # Option B: Include this node (if it fits in the current_target).
                # Check if the previous state could achieve the 'remaining sum'.
                if node_depth <= current_target:
                    if dp[i-1][current_target - node_depth]:
                        dp[i][current_target] = True
                        has_included[i][current_target] = True

        # --- Step 3: Backtrack to find specific node values ---
        if not dp[n][K]:
            return "Impossible" # Target sum K cannot be formed by any node combination

        final_assignments = [0] * n
        remaining_k = K
        
        # Move backwards from the last node to the first
        for i in range(n, 0, -1):
            if has_included[i][remaining_k]:
                node_depth, node_id = node_metadata[i-1]
                final_assignments[node_id] = 1 # Mark node as 'used'
                remaining_k -= node_depth # Reduce the sum we are looking for
        
        return final_assignments


