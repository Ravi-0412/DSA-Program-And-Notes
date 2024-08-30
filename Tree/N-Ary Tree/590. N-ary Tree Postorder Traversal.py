# Logic:
"""
    PREorder:  ROOT|Left|Right
    INorder:   Left|ROOT|Right
    POSTorder: Left|Right|ROOT

In case of an N-ary Tree, POSTorder is: Child1|Child2|...|ChildN|ROOT
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        ans = []
        for child in root.children:
            ans += self.postorder(child)
        return ans + [root.val]


# java
"""
class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        for (Node child : root.children) {
            ans.addAll(postorder(child));
        }
        ans.add(root.val);
        return ans;
    }
}
"""

# Iterative way 
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            
            # Append the children in reverse order
            for child in curr.children:
                stack.append(child)
        
        # Reverse the list to get the correct postorder traversal
        return ans[::-1]

# java
"""
class Solution {
    public List<Integer> postorder(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }

        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            Node curr = stack.pop();
            ans.add(curr.val);  // Add current node's value to the list

            // Push all the children onto the stack
            for (Node child : curr.children) {
                stack.push(child);
            }
        }

        // Reverse the list to get the correct postorder traversal
        Collections.reverse(ans);

        return ans;
    }
}
"""