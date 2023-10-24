# time: O(n)

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root== None:
            return root
        ans, level= [], []
        return self.helper(root,level,ans)
    
    def helper(self,root, level, ans):
        q= deque([root])
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
            level= []   # to store the ans of next level
        return ans



