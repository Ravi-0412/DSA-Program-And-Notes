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



