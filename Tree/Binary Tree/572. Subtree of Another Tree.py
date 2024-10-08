# method 1: Brute Force
# just check at each node for subtree by calling the 'isIdentical(root)'
# time : O(n*m)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root== None: return False    # simply return will also work
        # check if tree starting from root is same tree as subroot
        return self.isIdentical(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)  
    
    def isIdentical(self,root1, root2):
        # if any of them is None then both should be None for same tree
        if root1== None or root2== None:  # this will check that they are structurally same 
            return root1==root2    
        return (root1.val==root2.val) and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)
                # this will check all nodes are value wise same


# method 2: 
# i) Store values of tree in a list say root_values and values of subtree in a list say subtree_values.
# ii) Now apply string algorithm like Z-function check if any substring of subtree_values in present in root_values.
# if exists then subroot is present in root else not present.

# Note: We can't directly apply preorder and store values , it won't work.
# Because we have to take care of structure also i.e they should be structurally same.
# VVI: For this serialize both 'root' and 'subRoot' and apply Z-Algo in serialized one.

# Note: why we need to add extra line i.e ans.append(";")
"""
take example , where root = "12", subroot = "2" then 
i) without separator(;)
serialized_root = 12,N,N and serialized_subroot = 2,N,N 
So it will be match and it will give 'True' but it should be 'False' only.

ii) if we add separator(;) then 
serialized_root = ;,12,N,N and serialized_subroot =  ;,2,N,N
Then it won't be a match because including ';' subroot won't match.
"""

# Time: O(m+ n)

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def serialize(root):
            ans= []  # later will join this by any delimiter and return
            def Preorder(root):
                if root== None:   # for None node, using a speacial char 'N'
                    ans.append("N")  
                    return
                ans.append(";")   # Adding to distinguish for cases like: root = "12", subroot = "2" . Only difference from 'serialising Question".
                ans.append(str(root.val))    # since we have to return in string
                Preorder(root.left)
                Preorder(root.right)
            
            Preorder(root)
            return ",".join(ans)
        
        def Z_Algo(serialize_root, serialize_subRoot):
            m , n = len(serialize_root) , len(serialize_subRoot)
            # Make a new string combining both the string with one special character(to avoid comparison beyond that char)
            # jiska find karna h usko phle and jisme find karna h usko bad me.
            # Kyonki prefix == sufffix chahiye and jiska karna h wo prefix hona chahiye.
            s = serialize_subRoot + '$' + serialize_root   # any special symbol which is not allowed in string 
            # Now apply 'Z - Algo'.
            z = [0] * (m + n + 1)  # '1' for special symbol
            total = m + n + 1
            l , r = 0, 0
            for i in range(1, total):
                if i < r:
                    z[i] = min(r -i , z[i - l])
                while i + z[i] < total and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l , r = i, i + z[i]
            # Now find the 1st index in 'z' for which z[i] == len(subRoot) that will be our ans.
            # only we need to check in string 's' and that will start from 'n+1'.
            for i in range(n + 1, total):  
                if z[i] == n:  # len(serialize_subRoot)
                    # then actual index in 'subRoot' will be excluding the len(serialize_subRoot) + 1(special symbol)
                    return True   # Actual starting index: i - n - 1
            return False
        
        serialize_root = serialize(root)
        serialize_subRoot = serialize(subRoot)
        return Z_Algo(serialize_root, serialize_subRoot)



# JAva:
"""
// method 1: 
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null) {
            return false;
        }
        // Check if the tree starting from root is identical to subRoot
        if (isIdentical(root, subRoot)) {
            return true;
        }
        // If not identical, check the left and right subtrees
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean isIdentical(TreeNode root1, TreeNode root2) {
        // If either of the nodes is null, both must be null to be considered identical
        if (root1 == null || root2 == null) {
            return root1 == root2;
        }
        // Check if the current nodes' values are equal and recurse on left and right subtrees
        return (root1.val == root2.val) && isIdentical(root1.left, root2.left) && isIdentical(root1.right, root2.right);
    }
}

// method 2:
public class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        String serializeRoot = serialize(root);
        String serializeSubRoot = serialize(subRoot);
        return Z_Algo(serializeRoot, serializeSubRoot);
    }

    private String serialize(TreeNode root) {
        List<String> ans = new ArrayList<>();
        Preorder(root, ans);
        return String.join(",", ans);
    }

    private void Preorder(TreeNode root, List<String> ans) {
        if (root == null) {
            ans.add("N");  // using a special char 'N' for None node
            return;
        }
        ans.add(";");  // Adding to distinguish for cases like: root = "12", subroot = "2"
        ans.add(String.valueOf(root.val));
        Preorder(root.left, ans);
        Preorder(root.right, ans);
    }

    private boolean Z_Algo(String serializeRoot, String serializeSubRoot) {
        int m = serializeRoot.length();
        int n = serializeSubRoot.length();
        String s = serializeSubRoot + "$" + serializeRoot;  // any special symbol which is not allowed in string
        int total = m + n + 1;
        int[] z = new int[total];
        int l = 0, r = 0;

        for (int i = 1; i < total; i++) {
            if (i < r) {
                z[i] = Math.min(r - i, z[i - l]);
            }
            while (i + z[i] < total && s.charAt(z[i]) == s.charAt(i + z[i])) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }

        for (int i = n + 1; i < total; i++) {
            if (z[i] == n) {
                return true;  // found the match
            }
        }
        return false;  // no match found
    }
}
"""
