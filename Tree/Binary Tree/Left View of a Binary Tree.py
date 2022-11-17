# just same as "Right view"
# here instead of printing the last node at each level , print the 1st node at each level that's it i.e first node from left at each level
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return root
        q= deque([root])
        while q:
            level= []
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if i== 0:
                    print(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

# do by recursive approach also later


