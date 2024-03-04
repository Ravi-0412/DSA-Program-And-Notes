class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level= 0
        q= deque([root])
        while q:
            pre= None
            for i in range(len(q)):  
                curr= q.popleft()
                if level % 2== 0:
                    if curr.val % 2== 0 or (i>0 and pre >= curr.val):
                        return False
                else:
                    if curr.val % 2== 1 or ( i>0 and pre <= curr.val):
                        return False
                pre= curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level+= 1
        return True

