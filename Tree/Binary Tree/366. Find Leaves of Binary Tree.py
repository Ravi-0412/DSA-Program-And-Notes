"""
# LeetCode 366 — Find Leaves of Binary Tree

**Difficulty:** Medium  
**Topics:** Binary Tree, DFS, Tree Height, Postorder Traversal  
**Pattern:** Postorder DFS + Grouping by Height

## 1. Problem Statement

Given the root of a binary tree, repeatedly remove all leaf nodes from the tree until the tree becomes empty.

A leaf node is a node that has no left child and no right child.

After each removal operation, collect the values of all nodes removed in that round.

Return a list of lists where:
- The first list contains all nodes removed in the first round.
- The second list contains all nodes removed in the second round.
- Continue until every node has been removed.

The order of nodes within an individual round does not matter.

## 2. Example 1

**Input:**

```python
root = [1, 2, 3, 4, 5]
```

Tree:

```text
        1
       / \
      2   3
     / \
    4   5
```

**Output:**

```python
[[4, 5, 3], [2], [1]]
```

**Explanation:**

- Round 1: Nodes 4, 5, and 3 are leaf nodes. Remove them.
- Round 2: Node 2 becomes a leaf. Remove it.
- Round 3: Node 1 becomes a leaf. Remove it.

The tree is now empty.

## 3. Example 2

**Input:**

```python
root = [1]
```

**Output:**

```python
[[1]]
```

**Explanation:**

The tree contains only one node. Since it has no children, it is already a leaf and is removed in the first round.

## 4. Constraints

- The number of nodes in the tree is between 1 and 100.
- Each node's value is between -100 and 100.
- The tree is a valid binary tree.

## 5. Important Clarifications

1. A node is a leaf only when both its left and right children are absent.
2. Removing a leaf may cause its parent to become a leaf.
3. All leaves present at the beginning of a round must be grouped together.
4. The order of values within each round does not matter.

## 6. Expected LeetCode Function Signature

**Python:**

```python
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
```

**Java:**

```java
class Solution {
    public List<List<Integer>> findLeaves(TreeNode root) {
        
    }
}
```

## 7. Follow-up Thinking

Can you solve this problem without physically removing nodes from the tree?

Can you determine the removal round of each node using only one DFS traversal?

Hint: Think about the relationship between a node's height and the round in which it becomes a leaf.
"""

"""
1. Thought process and intuition
Core observation: Instead of physically removing leaf nodes repeatedly, calculate the height of every node. Nodes with the same height belong to the same removal round.
Step	Thought process
1. Identify the pattern	Repeatedly removing leaves suggests a relationship with tree height.
2. Avoid simulation	We don't need to modify the original tree or remove nodes repeatedly.
3. Use Postorder DFS	Calculate left and right subtree heights before calculating the current node's height.
4. Calculate height	height = 1 + max(left_height, right_height)
5. Base case	Return -1 for a null node. This makes a leaf node's height 0.
6. Group nodes	Store each node at result[height]. Nodes with the same height are removed in the same round.
7. Return result	The grouped lists represent the successive removal rounds.

Why does height determine the removal round?
Node type	Height	Removal round
Leaf node	0	1
Parent of leaf	1	2
Next parent	2	3
Next parent	3	4

\[
\text{Removal Round} = \text{Height} + 1
\]

Why Postorder DFS?
Postorder means Left → Right → Root.

We must calculate the heights of both children before calculating the parent's height.

For a null node, return -1:
\[
1+\max(-1,-1)=0
\]

Therefore, leaf nodes automatically receive height zero.
2. Time and space complexity
Let n be the number of nodes and h be the height of the tree.
Operation	Complexity	Explanation
DFS traversal	O(n)	Every node is visited exactly once.
Height calculation	O(1) per node	Only one max operation and addition.
Grouping nodes	O(1) per node	Append each value to its corresponding list.
Total time	O(n)	One traversal of the entire tree.
Auxiliary space	O(h)	Recursive call stack.
Output space	O(n)	Every node is stored exactly once.
Total space	O(n)	Including the output.

- Balanced tree: recursion stack O(log n).
- Skewed tree: recursion stack O(n).
"""



class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Stores nodes grouped by their removal round.
        # Index 0 = First round, index 1 = Second round, etc.
        result = []

        def dfs(node):

            # Null node has height -1.
            # Therefore, a leaf node will have height 0.
            if not node:
                return -1

            # Calculate the height of left and right subtrees.
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Current node's height is one more than
            # the maximum height of its children.
            height = 1 + max(left_height, right_height)

            # If this height doesn't have a group yet,
            # create a new list for this removal round.
            if height == len(result):
                result.append([])

            # Add the current node to its corresponding group.
            result[height].append(node.val)

            # Return height to help the parent calculate its height.
            return height

        # Start postorder DFS from the root.
        dfs(root)

        return result

# Java
"""

class Solution {

    List<List<Integer>> result;

    public List<List<Integer>> findLeaves(TreeNode root) {

        // Stores nodes grouped by their removal round.
        result = new ArrayList<>();

        // Start postorder DFS.
        dfs(root);

        return result;
    }

    private int dfs(TreeNode node) {

        // Null node has height -1.
        // This makes a leaf node's height 0.
        if (node == null) {
            return -1;
        }

        // Calculate left and right subtree heights first.
        int leftHeight = dfs(node.left);
        int rightHeight = dfs(node.right);

        // Calculate current node's height.
        int height = 1 + Math.max(leftHeight, rightHeight);

        // Create a new group if this height hasn't appeared yet.
        if (height == result.size()) {
            result.add(new ArrayList<>());
        }

        // Add current node to its corresponding removal round.
        result.get(height).add(node.val);

        // Return height to the parent node.
        return height;
    }
}

"""
