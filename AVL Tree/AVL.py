"""
Youtube Link: https://www.youtube.com/watch?v=CVA85JuJEn0 
Note VVI: AVL ,  Red-Black Tree & B-Trees / B+ Trees are such data structure that stores elements in sorted order and supports:

Insertion in O(log n)
Deletion in O(log n)
Search in O(log n)

=> For printing data in sorted order in case of AVL & Red-Black tree , just use inorder traversal,
because Binary search tree is base for both.

Note:
1) Insert: Insert in same way as we do in BST
But before returing the actual node update the height of current node and 
check if tree is balanced by calling the 'rotate(node)'.

2) Searching a node:  search in avl tree is exactly same as we do in BST.

3) Deletion: Involves four steps : 
a) Finding the node to be deleted. => just search the node
b) Removing the node, handling the three standard BST deletion cases (leaf, one child, two children).
c) Updating the heights of affected nodes.
d) Rebalancing the tree if necessary.

Time for all operation i.e insertion , searching and deletion is : O(logn)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1  # height from node to leaf
        self.left = None 
        self.right = None

class AVL:

    def height(self, node):  # height from node to leaf
        if node is None:
            return 0
        return node.height

    def insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        node.height = max(self.height(node.left), self.height(node.right)) + 1  # update the height of node before balancing
        return self.rotate(node)  # then rotate the node if balanced and return new updated node

    def rotate(self, node):
        if self.height(node.left) - self.height(node.right) > 1:
            if self.height(node.left.left) >= self.height(node.left.right):
                # left-left case so simply rotate one time right
                return self.rightRotate(node)
            else:
                # left - right case from top. So rotate first Left and then Right(we do from bottom up and in opposite fashon to balance)
                node.left = self.leftRotate(node.left)  # extra node will come as Left child of 'node' after LeftRotation.
                return self.rightRotate(node)
        if self.height(node.right) - self.height(node.left) > 1:
            if self.height(node.right.right) >= self.height(node.right.left):
                # right - right case so simply rotate one time left
                return self.leftRotate(node)
            else:
                # right - left case from top. So rotate first right and then Left(we do from bottom up and in opposite fashon to balance)
                node.right = self.rightRotate(node.right)  # extra node will come as right child of 'node' after rightRotation.
                return self.leftRotate(node)
        return node  # if already balanced then return the (unchanged) node pointer

    def rightRotate(self, parent):
        left_child = parent.left
        left_right_child = left_child.right
        left_child.right = parent
        parent.left = left_right_child
        parent.height = max(self.height(parent.left), self.height(parent.right)) + 1
        left_child.height = max(self.height(left_child.left), self.height(left_child.right)) + 1
        return left_child  # this will become parent after rotation so return this node

    def leftRotate(self, parent):
        right_child = parent.right
        right_left_child = right_child.left
        right_child.left = parent
        parent.right = right_left_child
        parent.height = max(self.height(parent.left), self.height(parent.right)) + 1
        right_child.height = max(self.height(right_child.left), self.height(right_child.right)) + 1
        return right_child  # this will become parent after rotation so return this node

    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.right)
            node.value = temp.value
            node.right = self.delete(node.right, temp.value)

        node.height = max(self.height(node.left), self.height(node.right)) + 1
        return self.rotate(node)

    def search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)

    def inorder(self, node):  # New method to print tree values in sorted order
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

# Main program
root = None
avl = AVL()

# Insert values
for i in range(1000):
    root = avl.insert(root, i)

print("Height of AVL tree after insertion:", avl.height(root))

# Print all values in tree
print("Values in AVL tree (in-order):")
avl.inorder(root)

# Search for a value
search_value = 500
found_node = avl.search(root, search_value)
if found_node:
    print(f"Value {search_value} found in AVL tree.")
else:
    print(f"Value {search_value} not found in AVL tree.")

# Delete values
for i in range(600):
    root = avl.delete(root, i)

print("Height of AVL tree after deletion:", avl.height(root))


# java
"""
class Node {
    int value;
    int height;  // height from node to leaf
    Node left;
    Node right;

    Node(int value) {
        this.value = value;
        this.height = 1;
    }
}

class AVL {

    int height(Node node) {  // height from node to leaf
        if (node == null) return 0;
        return node.height;
    }

    Node insert(Node node, int value) {
        if (node == null) return new Node(value);
        if (value < node.value)
            node.left = insert(node.left, value);
        else
            node.right = insert(node.right, value);

        node.height = Math.max(height(node.left), height(node.right)) + 1;  // update the height of node before balancing
        return rotate(node);  // then rotate the node if balanced and return new updated node
    }

    Node rotate(Node node) {
        if (height(node.left) - height(node.right) > 1) {
            if (height(node.left.left) >= height(node.left.right)) {
                // left-left case so simply rotate one time right
                return rightRotate(node);
            } else {
                // left - right case from top. So rotate first Left and then Right(we do from bottom up and in opposite fashon to balance)
                node.left = leftRotate(node.left);  // extra node will come as Left child of 'node' after LeftRotation.
                return rightRotate(node);
            }
        }
        if (height(node.right) - height(node.left) > 1) {
            if (height(node.right.right) >= height(node.right.left)) {
                // right - right case so simply rotate one time left
                return leftRotate(node);
            } else {
                // right - left case from top. So rotate first right and then Left(we do from bottom up and in opposite fashon to balance)
                node.right = rightRotate(node.right);  // extra node will come as right child of 'node' after rightRotation.
                return leftRotate(node);
            }
        }
        return node;  // if already balanced then return the (unchanged) node pointer
    }

    Node rightRotate(Node parent) {
        Node left_child = parent.left;
        Node left_right_child = left_child.right;
        left_child.right = parent;
        parent.left = left_right_child;
        parent.height = Math.max(height(parent.left), height(parent.right)) + 1;
        left_child.height = Math.max(height(left_child.left), height(left_child.right)) + 1;
        return left_child;  // this will become parent after rotation so return this node
    }

    Node leftRotate(Node parent) {
        Node right_child = parent.right;
        Node right_left_child = right_child.left;
        right_child.left = parent;
        parent.right = right_left_child;
        parent.height = Math.max(height(parent.left), height(parent.right)) + 1;
        right_child.height = Math.max(height(right_child.left), height(right_child.right)) + 1;
        return right_child;  // this will become parent after rotation so return this node
    }

    Node minValueNode(Node node) {
        Node current = node;
        while (current.left != null)
            current = current.left;
        return current;
    }

    Node delete(Node node, int value) {
        if (node == null) return node;

        if (value < node.value)
            node.left = delete(node.left, value);
        else if (value > node.value)
            node.right = delete(node.right, value);
        else {
            if (node.left == null) {
                Node temp = node.right;
                node = null;
                return temp;
            } else if (node.right == null) {
                Node temp = node.left;
                node = null;
                return temp;
            }
            Node temp = minValueNode(node.right);
            node.value = temp.value;
            node.right = delete(node.right, temp.value);
        }

        node.height = Math.max(height(node.left), height(node.right)) + 1;
        return rotate(node);
    }

    Node search(Node node, int value) {
        if (node == null || node.value == value) return node;
        if (value < node.value)
            return search(node.left, value);
        return search(node.right, value);
    }

    void inorder(Node node) {  // New method to print tree values in sorted order
        if (node != null) {
            inorder(node.left);
            System.out.print(node.value + " ");
            inorder(node.right);
        }
    }

    public static void main(String[] args) {
        Node root = null;
        AVL avl = new AVL();

        // Insert values
        for (int i = 0; i < 1000; i++) {
            root = avl.insert(root, i);
        }

        System.out.println("Height of AVL tree after insertion: " + avl.height(root));

        // Print all values in tree
        System.out.println("Values in AVL tree (in-order):");
        avl.inorder(root);

        // Search for a value
        int search_value = 500;
        Node found_node = avl.search(root, search_value);
        if (found_node != null)
            System.out.println("\nValue " + search_value + " found in AVL tree.");
        else
            System.out.println("\nValue " + search_value + " not found in AVL tree.");

        // Delete values
        for (int i = 0; i < 600; i++) {
            root = avl.delete(root, i);
        }

        System.out.println("Height of AVL tree after deletion: " + avl.height(root));
    }
}
"""
# C++ code
"""
#include <iostream>
#include <algorithm>
using namespace std;

class Node {
public:
    int value;
    int height;  // height from node to leaf
    Node* left;
    Node* right;

    Node(int value) {
        this->value = value;
        height = 1;
        left = right = nullptr;
    }
};

class AVL {
public:
    int height(Node* node) {  // height from node to leaf
        if (node == nullptr)
            return 0;
        return node->height;
    }

    Node* insert(Node* node, int value) {
        if (node == nullptr)
            return new Node(value);
        if (value < node->value)
            node->left = insert(node->left, value);
        else
            node->right = insert(node->right, value);

        node->height = max(height(node->left), height(node->right)) + 1;  // update the height of node before balancing
        return rotate(node);  // then rotate the node if balanced and return new updated node
    }

    Node* rotate(Node* node) {
        if (height(node->left) - height(node->right) > 1) {
            if (height(node->left->left) >= height(node->left->right)) {
                // left-left case so simply rotate one time right
                return rightRotate(node);
            } else {
                // left - right case from top. So rotate first Left and then Right(we do from bottom up and in opposite fashon to balance)
                node->left = leftRotate(node->left);  // extra node will come as Left child of 'node' after LeftRotation.
                return rightRotate(node);
            }
        }
        if (height(node->right) - height(node->left) > 1) {
            if (height(node->right->right) >= height(node->right->left)) {
                // right - right case so simply rotate one time left
                return leftRotate(node);
            } else {
                // right - left case from top. So rotate first right and then Left(we do from bottom up and in opposite fashon to balance)
                node->right = rightRotate(node->right);  // extra node will come as right child of 'node' after rightRotation.
                return leftRotate(node);
            }
        }
        return node;  // if already balanced then return the (unchanged) node pointer
    }

    Node* rightRotate(Node* parent) {
        Node* left_child = parent->left;
        Node* left_right_child = left_child->right;
        left_child->right = parent;
        parent->left = left_right_child;
        parent->height = max(height(parent->left), height(parent->right)) + 1;
        left_child->height = max(height(left_child->left), height(left_child->right)) + 1;
        return left_child;  // this will become parent after rotation so return this node
    }

    Node* leftRotate(Node* parent) {
        Node* right_child = parent->right;
        Node* right_left_child = right_child->left;
        right_child->left = parent;
        parent->right = right_left_child;
        parent->height = max(height(parent->left), height(parent->right)) + 1;
        right_child->height = max(height(right_child->left), height(right_child->right)) + 1;
        return right_child;  // this will become parent after rotation so return this node
    }

    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current->left != nullptr)
            current = current->left;
        return current;
    }

    Node* deleteNode(Node* node, int value) {
        if (node == nullptr) return node;

        if (value < node->value)
            node->left = deleteNode(node->left, value);
        else if (value > node->value)
            node->right = deleteNode(node->right, value);
        else {
            if (node->left == nullptr) {
                Node* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr) {
                Node* temp = node->left;
                delete node;
                return temp;
            }

            Node* temp = minValueNode(node->right);
            node->value = temp->value;
            node->right = deleteNode(node->right, temp->value);
        }

        node->height = max(height(node->left), height(node->right)) + 1;
        return rotate(node);
    }

    Node* search(Node* node, int value) {
        if (node == nullptr || node->value == value)
            return node;
        if (value < node->value)
            return search(node->left, value);
        return search(node->right, value);
    }

    void inorder(Node* node) {  // New method to print tree values in sorted order
        if (node != nullptr) {
            inorder(node->left);
            cout << node->value << " ";
            inorder(node->right);
        }
    }
};

int main() {
    Node* root = nullptr;
    AVL avl;

    // Insert values
    for (int i = 0; i < 1000; i++) {
        root = avl.insert(root, i);
    }

    cout << "Height of AVL tree after insertion: " << avl.height(root) << endl;

    // Print all values in tree
    cout << "Values in AVL tree (in-order):" << endl;
    avl.inorder(root);
    cout << endl;

    // Search for a value
    int search_value = 500;
    Node* found_node = avl.search(root, search_value);
    if (found_node)
        cout << "Value " << search_value << " found in AVL tree." << endl;
    else
        cout << "Value " << search_value << " not found in AVL tree." << endl;

    // Delete values
    for (int i = 0; i < 600; i++) {
        root = avl.deleteNode(root, i);
    }

    cout << "Height of AVL tree after deletion: " << avl.height(root) << endl;
}
"""
