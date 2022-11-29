# submitted on gfg
# time: O(n)

def levelOrder(self,root ):
        Q= [root]   #  use deque to reduce time complexity 
        ans= []
        while Q:
            curr= Q.pop(0)
            ans.append(curr.data)
            if curr.left!= None:
                Q.append(curr.left)
            if curr.right!= None:
                Q.append(curr.right)
        return ans


# for leetcode
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


# just shorter version of above logic only
class Solution:
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:  # 1st condition is checking for null and 2nd is checking for while q
            ans.append([node.val for node in level])  # just the same as : curr= q.popleft()
            LRpair= [(node.left,node.right) for node in level]  
            level= [leaf for LR in LRpair for leaf in LR if leaf]  # will take LR pair and then first left then right from lR pair and add them into level
                                                                    # same as appending in Q
        return ans

