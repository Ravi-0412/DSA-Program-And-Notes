# Logic: just store the nodes at a depth.
# But only increment depth for left child not for right child.

# At alst return the nodes in ascending order of depth.

from collections import defaultdict

class TreeNode:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def diagonal(self, root):
        def diagonalPrintUtil(root, d, diagonalPrintMap):
            if root is None:
                return

            # Store all nodes of same line together as a list
            diagonalPrintMap[d].append(root.data)

            # Increase the vertical distance for left child
            diagonalPrintUtil(root.left, d + 1, diagonalPrintMap)

            # Vertical distance remains the same for right child
            diagonalPrintUtil(root.right, d, diagonalPrintMap)
        
        diagonalPrintMap = defaultdict(list)
        diagonalPrintUtil(root, 0, diagonalPrintMap)
        
        # Sort the map by diagonal distance and prepare the output
        result = []
        for diagonal in sorted(diagonalPrintMap.keys()):
            result.extend(diagonalPrintMap[diagonal])
        
        return result


# Java
""""
class Tree {
    public ArrayList<Integer> diagonal(Node root) {
        // Map to store diagonal elements
        Map<Integer, ArrayList<Integer>> diagonalPrintMap = new HashMap<>();

        // Util function to fill the map
        diagonalPrintUtil(root, 0, diagonalPrintMap);

        // Result list to store diagonal traversal
        ArrayList<Integer> result = new ArrayList<>();

        // Sorting the map by diagonal distance and adding elements to result
        for (Integer key : new TreeMap<>(diagonalPrintMap).keySet()) {
            result.addAll(diagonalPrintMap.get(key));
        }

        return result;
    }

    private void diagonalPrintUtil(Node root, int d, Map<Integer, ArrayList<Integer>> diagonalPrintMap) {
        if (root == null) {
            return;
        }

        // Store all nodes of same line together as a list
        diagonalPrintMap.computeIfAbsent(d, k -> new ArrayList<>()).add(root.data);

        // Increase the vertical distance for left child
        diagonalPrintUtil(root.left, d + 1, diagonalPrintMap);

        // Vertical distance remains the same for right child
        diagonalPrintUtil(root.right, d, diagonalPrintMap);
    }
"""