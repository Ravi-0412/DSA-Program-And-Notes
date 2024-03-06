# logic: Visit each node and keeping track of parent and depth either using bfs or dfs.

# method 1: using bfs.
# We need to keep track of 'depth' , 'parent' for each node, so adding these values also with node in queue.
# ans will have two ele one for 'x' and one for 'y'. 

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        ans= []
        q= collections.deque()
        q.append((root, 0, None))   # [(node, depth, parent)]
        while q:
            node, depth, parent= q.popleft()
            if node.val== x or node.val== y:
                ans.append([depth, parent])
            if node.left:
                q.append((node.left, depth +1, node))
            if node.right:
                q.append((node.right, depth +1, node))
        # check for cousins
        return ans[0][0]== ans[1][0] and ans[0][1] != ans[1][1]
    

# method 2: Using Dfs
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.depth_x , self.depth_y = 0 , 0
        self.parent_x , self.parent_y = None, None

        def dfs(root, height, parent):
            if not root:
                return 
            if root.val == x:
                self.depth_x = height
                self.parent_x  = parent
            if root.val == y:
                self.depth_y = height
                self.parent_y  = parent
            dfs(root.left,  height + 1, root)
            dfs(root.right, height + 1, root)
            
        dfs(root, 0, None)
        return self.depth_x == self.depth_y  and self.parent_x != self.parent_y