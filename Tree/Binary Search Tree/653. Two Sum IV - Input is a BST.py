# method 1: 
"""
store the inorder 
now problem reduces to "Two sum"
then apply the two pointer approach for find the pair since inorder will be a sorted array 
space= time= O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Step 1: Get the in-order traversal (sorted array)
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        nums = inorder(root)
        
        # Step 2: Apply two-pointer approach
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False
    
# method 2:
"""
just store the remaining sum w.r.t each number you pop for inorder 
After poping check whether that number is present in the hashmap for not
if already presen then it means sum exist otherwise add the curr poped node into stack.
space= time= O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return False

# method 3:
"""
just use the 'BST iterator' i.e 'next' and 'prev'
next will give element from start i.e smallest one and 'prev' will give element from last i.e largest one.
Now problem reduces to "Two sum" with two pointer approach 'next' and 'prev'.

for getting the 'prev' just push all the right ele first and for any node you pop 
push their 'left'. 
just the opposite of 'next'.

time: O(n)
space: O(H)*2= O(H)
this Q is based on this approach only since in this we are using a lot of property of BST
"""

class BSTIterator:
    def __init__(self, root, reverse):  # taking reverse also so that we don't have to make separate function 
                                        # for getting 'next' and 'prev', for smallest and greatest one.
        self.stack= []
        self.reverse= reverse
        self.PushAll(root)
        
    def next(self) -> int:
        temp= self.stack.pop()
        if self.reverse:
            self.PushAll(temp.left)  
        else:
            self.PushAll(temp.right)
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack != []
    
    def PushAll(self, root):
        # push everything that comes on the left/right of root based on 'reverse' value.
        curr= root
        while curr:
            self.stack.append(curr)
            if self.reverse:  # means we have to get element from last so put all the right nodes into the stack
                curr= curr.right
            else:
                curr= curr.left
                
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        start= BSTIterator(root, False)    # get element from start i.e smallest one first
        end=   BSTIterator(root, True)     # get element from end i.e   largest one first so made reverse= "True"
        i= start.next()
        j= end.next()
        while i< j:
            if i + j== k:
                return True
            elif i + j < k:
                i= start.next()
            else: 
                j= end.next()
        return False
