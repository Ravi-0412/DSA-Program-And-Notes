# time: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q= deque([root])
        ans, level= [], []
        while q:
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(level)
            level= []   # to store the ans of next level
        return ans


# Related q:
# 1) 515. Find Largest Value in Each Tree Row

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        q= deque([root])
        ans = []
        while q:
            maxi = float('-inf')
            for i in range(len(q)):  # we have to print level by level in a list
                cur= q.popleft()
                maxi = max(maxi, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(maxi)
        return ans


# 2) 513. Find Bottom Left Tree Value
# simplied: Find the 1st node of last level

# a) When you find node at greater level , update the ans.
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((0, root))
        maxLevel = -1
        ans = None
        while q:
            l , node = q.popleft()
            if l > maxLevel :
                maxLevel = l
                ans = node.val
            if node.left:
                q.append((l + 1, node.left))
            if node.right:
                q.append((l + 1, node.right))
        return ans


# b) Append right to left then last poped node will be our ans
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        while q:
            root = q.popleft()   # change root then only we will be able to return correct ans at last.
            if root.right:
                q.append(root.right)
            if root.left:
                q.append(root.left)
            
        return root.val  # value of last poped node

# 3) 103. Binary Tree Zigzag Level Order Traversal
# 4) 1609. Even Odd Tree
# 5) 1161. Maximum Level Sum of a Binary Tree
# 6) 116. Populating Next Right Pointers in Each Node
# 7) 199. Binary Tree Right Side View
# 8) Left View of a Binary Tree
    