# # just totally same as vertical order traversal(copied that code only)

# logic: you have to print the 1st node at each horizonatl level from bottom(maximum x_coordinate) that's it 
# since remaining node at same horizontal level won't be visible when seen from bottom.

# or you can say for each horizonatal level take the only ele with maximum_x coordinate

# time: O(n*logn)
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.min_h, self.max_h= 0, 0
        dic= collections.defaultdict(list)  
        
        def dfs(root, lvl_h, lvl_v):   
            if root== None:
                return
            self.min_h= min(self.min_h, lvl_h)
            self.max_h= max(self.max_h, lvl_h)
            dic[lvl_h].append((lvl_v, root.val))
            dfs(root.left, lvl_h-1, lvl_v+1)     # left node lies at (col-1,row+1), horizontal level->column and vertical level -> row
            dfs(root.right, lvl_h+1, lvl_v+1)
        
        dfs(root,0,0)   # just a traversla can say preorder

        for hori in range(self.min_h, self.max_h+ 1):
            for key, val in sorted(dic[hori],reverse= True):    # sorted the value in reverse order to bring nodes with maximum_x coordinate
                print(val,end=" ")
                break

