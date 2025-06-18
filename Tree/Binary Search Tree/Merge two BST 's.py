# method 1: 

# steps to do:
# 1) find the inorder traversal of both the tree and store in separate arrays.
# 2) Now merge two arrays(sorted form) and store them into a list.
# 3) Now Q reduces to "Given a sorted array convert into a balanced BST"

# Time : O(m+ n) = space
class Solution:
    
    def merge(self, root1, root2):
        inorder1= self.InorderIterative(root1)
        inorder2= self.InorderIterative(root2)
        # print(inorder1, inorder2)
        merged_array= self.mergeSortedArray(inorder1, len(inorder1), inorder2, len(inorder2))
        # return merged_array   # not a good way to return. form bst then return.
        root= self.sortedArrayToBST(merged_array)  # this will be give the root of the merged BST.
        return self.InorderIterative(root)
    
    def InorderIterative(self,root):
        if root== None:
            return 
        stack, ans= [], []
        while stack or root:
            while root:  # keep going left 
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node 
            curr= stack.pop()
            ans.append(curr.data)
            root= curr.right
        return ans
    
    def mergeSortedArray(self, nums1, m, nums2, n):
        i,j= 0,0
        ans= []
        while(i<m and j <n):
            if nums1[i] >= nums2[j]:
                ans.append(nums2[j])
                j += 1
            else: 
                ans.append(nums1[i])
                i += 1
        while(i < m):
            ans.append(nums1[i])
            i += 1
        while(j<n):
            ans.append(nums2[j])
            j += 1
        return ans
    
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid= len(nums)//2
        node= Node(nums[mid])
        node.left=  self.sortedArrayToBST(nums[:mid])
        node.right= self.sortedArrayToBST(nums[mid+1:])
        return node

# Java
"""
class Solution {

    public List<Integer> merge(Node root1, Node root2) {
        List<Integer> inorder1 = InorderIterative(root1);
        List<Integer> inorder2 = InorderIterative(root2);
        // print(inorder1, inorder2)
        List<Integer> merged_array = mergeSortedArray(inorder1, inorder1.size(), inorder2, inorder2.size());
        // return merged_array   // not a good way to return. form bst then return.
        Node root = sortedArrayToBST(merged_array);  // this will be give the root of the merged BST.
        return InorderIterative(root);
    }

    public List<Integer> InorderIterative(Node root) {
        if (root == null) {
            return new ArrayList<>();
        }
        Stack<Node> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {  // keep going left 
                stack.push(root);
                root = root.left;
            }
            // if None, it means no left child then print the stack top and append the 'poped.right'
            // it means we have reached the leftmost node 
            Node curr = stack.pop();
            ans.add(curr.data);
            root = curr.right;
        }
        return ans;
    }

    public List<Integer> mergeSortedArray(List<Integer> nums1, int m, List<Integer> nums2, int n) {
        int i = 0, j = 0;
        List<Integer> ans = new ArrayList<>();
        while (i < m && j < n) {
            if (nums1.get(i) >= nums2.get(j)) {
                ans.add(nums2.get(j));
                j += 1;
            } else {
                ans.add(nums1.get(i));
                i += 1;
            }
        }
        while (i < m) {
            ans.add(nums1.get(i));
            i += 1;
        }
        while (j < n) {
            ans.add(nums2.get(j));
            j += 1;
        }
        return ans;
    }

    public Node sortedArrayToBST(List<Integer> nums) {
        if (nums.isEmpty()) {
            return null;
        }
        int mid = nums.size() / 2;
        Node node = new Node(nums.get(mid));
        node.left = sortedArrayToBST(nums.subList(0, mid));
        node.right = sortedArrayToBST(nums.subList(mid + 1, nums.size()));
        return node;
    }
}

"""
# C++ Code
"""
class Solution {
public:
    vector<int> merge(Node* root1, Node* root2) {
        vector<int> inorder1 = InorderIterative(root1);
        vector<int> inorder2 = InorderIterative(root2);
        // print(inorder1, inorder2)
        vector<int> merged_array = mergeSortedArray(inorder1, inorder1.size(), inorder2, inorder2.size());
        // return merged_array   // not a good way to return. form bst then return.
        Node* root = sortedArrayToBST(merged_array);  // this will be give the root of the merged BST.
        return InorderIterative(root);
    }

    vector<int> InorderIterative(Node* root) {
        if (root == nullptr) {
            return {};
        }
        stack<Node*> stack;
        vector<int> ans;
        while (!stack.empty() || root != nullptr) {
            while (root) {  // keep going left 
                stack.push(root);
                root = root->left;
            }
            // if None, it means no left child then print the stack top and append the 'poped.right'
            // it means we have reached the leftmost node 
            Node* curr = stack.top();
            stack.pop();
            ans.push_back(curr->data);
            root = curr->right;
        }
        return ans;
    }

    vector<int> mergeSortedArray(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = 0, j = 0;
        vector<int> ans;
        while (i < m && j < n) {
            if (nums1[i] >= nums2[j]) {
                ans.push_back(nums2[j]);
                j += 1;
            } else {
                ans.push_back(nums1[i]);
                i += 1;
            }
        }
        while (i < m) {
            ans.push_back(nums1[i]);
            i += 1;
        }
        while (j < n) {
            ans.push_back(nums2[j]);
            j += 1;
        }
        return ans;
    }

    Node* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) {
            return nullptr;
        }
        int mid = nums.size() / 2;
        Node* node = new Node(nums[mid]);
        vector<int> left(nums.begin(), nums.begin() + mid);
        vector<int> right(nums.begin() + mid + 1, nums.end());
        node->left = sortedArrayToBST(left);
        node->right = sortedArrayToBST(right);
        return node;
    }
};

"""