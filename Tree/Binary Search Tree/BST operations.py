class Node:
    def __init__(self,data= None):
        self.data= data
        self.left= None
        self.right= None
    
class BST:

    def BuildBSTRecursive(self,root,ele):
        if root== None:
            return Node(ele)
        elif ele <root.data:
            root.left= self.BuildBSTRecursive(root.left, ele)
        else:
            root.right= self.BuildBSTRecursive(root.right, ele)
        return root  # return the root always as we have to start checking from root  
    
    def SearchMin(self,root):
        if root== None:
            return
        if root.left== None:
            return root.data
        return self.SearchMin(root.left)

    def SearchMax(self,root):
        if root== None:
            return
        if root.right== None:
            return root.data
        return self.SearchMax(root.right)
    
    def SearchKey(self,root, key):
        if root== None:   # if reached None
            print("{} is not present or tree is empty".format(key))
            return None
        if root.data== key:
            # print("{} is present at node address {}".format(key,root))
            return root
        elif key< root.data:
            return self.SearchKey(root.left, key)
        else:
            return self.SearchKey(root.right, key)

    def deleteNode(self, root, key):
        if root== None:
            return root
        if key< root.data:
            root.left= self.deleteNode(root.left, key)
        elif key >root.data:
            root.right= self.deleteNode(root.right, key)
        else:
            if root.left== None and root.right== None:
                root= None
            elif root.left!= None and root.right== None:
                root= root.left
            elif root.right!= None and root.left== None:
                root= root.right
            else:
                temp= self.SearchMin1(root.right)
                root.data= temp.data
                root.right= self.deleteNode(root.right, root.data)
        return root
                
    def SearchMin1(self,root):
        if root.left== None:
            return root
        return self.SearchMin(root.left)
    
        # Or 
        """
        while root.left:
            root = root.left
        return root
        """
    
    def TotalNodes(self, root):
        # concise way of writing
        if root== None:
            return 0
        return 1+ self.TotalNodes(root.left) + self.TotalNodes(root.right)
    # Later try by iterative way


    def LeafNode(self, root):
        # concise way
        if root== None:
            return 0
        if root.left== None and root.right== None:
            return 1
        return self.LeafNode(root.left) + self.LeafNode(root.right)
        # Later try by iterative way

    def Depth(self,root):
        if root== None:
            return 0
        return 1 + max(self.Depth(root.left), self.Depth(root.right))
    # try later by iterative way

root= None
b= BST()
arr= [50,15,62,5,20,58,91,3,8,37,60,24]
for ele in arr:
    root= b.BuildBSTRecursive(root,ele)

# now insert into already made BST
# root= b.BuildBSTRecursive(root,23)

# print("minimum ele in BST is: ", b.SearchMin(root))
# print("maximum ele in BST is: ", b.SearchMax(root))

# b.SearchKey(root,20)
# b.SearchKey(root,13)

# b.deleteNode(root,24)
print("inorder traversal Iterative is: ")
b.InorderIterative(root)
print()
# print("total no of nodes: ", b.TotalNodes(root))
# print("no of leaf nodes: ", b.LeafNode(root))
print("depth of the tree is: ",b.Depth(root))


# Keep this inorder traversal code in mind
# Most of the q of BST , we can solve modifying this a little.
def InorderIterative(self,root):
    if root== None:
        return 
    stack, ans= [], []
    while stack or root:
        while root:  # keep going left 
            stack.append(root)
            root= root.left
        # if None, it means no left child then print the stack top (just pop).
        # it means we have reached the leftmost node.
        curr= stack.pop()
        ans.append(curr.val)
        root= curr.right  # move the pointer to check the right child.
    return ans

# Java
"""
import java.util.*;

class Node {
    int data;
    Node left, right;
    Node(int data) {
        this.data = data;
        left = right = null;
    }
}

class BST {

    Node BuildBSTRecursive(Node root, int ele) {
        if (root == null) return new Node(ele);
        else if (ele < root.data) root.left = BuildBSTRecursive(root.left, ele);
        else root.right = BuildBSTRecursive(root.right, ele);
        return root;  // return the root always as we have to start checking from root
    }

    int SearchMin(Node root) {
        if (root == null) return -1;
        if (root.left == null) return root.data;
        return SearchMin(root.left);
    }

    int SearchMax(Node root) {
        if (root == null) return -1;
        if (root.right == null) return root.data;
        return SearchMax(root.right);
    }

    Node SearchKey(Node root, int key) {
        if (root == null) {
            System.out.println(key + " is not present or tree is empty");
            return null;
        }
        if (root.data == key) return root;
        else if (key < root.data) return SearchKey(root.left, key);
        else return SearchKey(root.right, key);
    }

    Node deleteNode(Node root, int key) {
        if (root == null) return root;
        if (key < root.data) root.left = deleteNode(root.left, key);
        else if (key > root.data) root.right = deleteNode(root.right, key);
        else {
            if (root.left == null && root.right == null) return null;
            else if (root.left != null && root.right == null) return root.left;
            else if (root.right != null && root.left == null) return root.right;
            else {
                Node temp = SearchMin1(root.right);
                root.data = temp.data;
                root.right = deleteNode(root.right, root.data);
            }
        }
        return root;
    }

    Node SearchMin1(Node root) {
        if (root.left == null) return root;
        return SearchMin1(root.left);
    }

    int TotalNodes(Node root) {
        if (root == null) return 0;
        return 1 + TotalNodes(root.left) + TotalNodes(root.right);
    }

    int LeafNode(Node root) {
        if (root == null) return 0;
        if (root.left == null && root.right == null) return 1;
        return LeafNode(root.left) + LeafNode(root.right);
    }

    int Depth(Node root) {
        if (root == null) return 0;
        return 1 + Math.max(Depth(root.left), Depth(root.right));
    }

    void InorderIterative(Node root) {
        if (root == null) return;
        Stack<Node> stack = new Stack<>();
        ArrayList<Integer> ans = new ArrayList<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {  // keep going left
                stack.push(root);
                root = root.left;
            }
            // if None, it means no left child then print the stack top (just pop).
            // it means we have reached the leftmost node.
            Node curr = stack.pop();
            ans.add(curr.data);
            root = curr.right;  // move the pointer to check the right child.
        }
        for (int val : ans) System.out.print(val + " ");
    }
}

public class Main {
    public static void main(String[] args) {
        Node root = null;
        BST b = new BST();
        int[] arr = {50,15,62,5,20,58,91,3,8,37,60,24};
        for (int ele : arr) {
            root = b.BuildBSTRecursive(root, ele);
        }

        System.out.println("inorder traversal Iterative is: ");
        b.InorderIterative(root);
        System.out.println();

        System.out.println("depth of the tree is: " + b.Depth(root));
    }
}

"""

#C++ Code 
"""
class Node:
    def __init__(self,data= None):
        self.data= data
        self.left= None
        self.right= None
    
class BST:

    def BuildBSTRecursive(self,root,ele):
        if root== None:
            return Node(ele)
        elif ele <root.data:
            root.left= self.BuildBSTRecursive(root.left, ele)
        else:
            root.right= self.BuildBSTRecursive(root.right, ele)
        return root  # return the root always as we have to start checking from root  
    
    def SearchMin(self,root):
        if root== None:
            return
        if root.left== None:
            return root.data
        return self.SearchMin(root.left)

    def SearchMax(self,root):
        if root== None:
            return
        if root.right== None:
            return root.data
        return self.SearchMax(root.right)
    
    def SearchKey(self,root, key):
        if root== None:   # if reached None
            print("{} is not present or tree is empty".format(key))
            return None
        if root.data== key:
            # print("{} is present at node address {}".format(key,root))
            return root
        elif key< root.data:
            return self.SearchKey(root.left, key)
        else:
            return self.SearchKey(root.right, key)

    def deleteNode(self, root, key):
        if root== None:
            return root
        if key< root.data:
            root.left= self.deleteNode(root.left, key)
        elif key >root.data:
            root.right= self.deleteNode(root.right, key)
        else:
            if root.left== None and root.right== None:
                root= None
            elif root.left!= None and root.right== None:
                root= root.left
            elif root.right!= None and root.left== None:
                root= root.right
            else:
                temp= self.SearchMin1(root.right)
                root.data= temp.data
                root.right= self.deleteNode(root.right, root.data)
        return root
                
    def SearchMin1(self,root):
        if root.left== None:
            return root
        return self.SearchMin(root.left)
    
        # Or 
        """
        while root.left:
            root = root.left
        return root
        """
    
    def TotalNodes(self, root):
        # concise way of writing
        if root== None:
            return 0
        return 1+ self.TotalNodes(root.left) + self.TotalNodes(root.right)
    # Later try by iterative way


    def LeafNode(self, root):
        # concise way
        if root== None:
            return 0
        if root.left== None and root.right== None:
            return 1
        return self.LeafNode(root.left) + self.LeafNode(root.right)
        # Later try by iterative way

    def Depth(self,root):
        if root== None:
            return 0
        return 1 + max(self.Depth(root.left), self.Depth(root.right))
    # try later by iterative way

root= None
b= BST()
arr= [50,15,62,5,20,58,91,3,8,37,60,24]
for ele in arr:
    root= b.BuildBSTRecursive(root,ele)

# now insert into already made BST
# root= b.BuildBSTRecursive(root,23)

# print("minimum ele in BST is: ", b.SearchMin(root))
# print("maximum ele in BST is: ", b.SearchMax(root))

# b.SearchKey(root,20)
# b.SearchKey(root,13)

# b.deleteNode(root,24)
print("inorder traversal Iterative is: ")
b.InorderIterative(root)
print()
# print("total no of nodes: ", b.TotalNodes(root))
# print("no of leaf nodes: ", b.LeafNode(root))
print("depth of the tree is: ",b.Depth(root))


# Keep this inorder traversal code in mind
# Most of the q of BST , we can solve modifying this a little.
def InorderIterative(self,root):
    if root== None:
        return 
    stack, ans= [], []
    while stack or root:
        while root:  # keep going left 
            stack.append(root)
            root= root.left
        # if None, it means no left child then print the stack top (just pop).
        # it means we have reached the leftmost node.
        curr= stack.pop()
        ans.append(curr.val)
        root= curr.right  # move the pointer to check the right child.
    return ans


Convert to c++ and java , dont change variable name and please dont chnage commments 

"""