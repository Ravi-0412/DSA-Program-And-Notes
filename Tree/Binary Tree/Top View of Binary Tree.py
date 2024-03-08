# # just totally same as vertical order traversal(copied that code only)

# logic: root pe baith jao and h jo node tmko dikhe usko print karna h..tm sirf har horizonatal pe sirf ek hi node top wala hi dekh paoge.
# so, you have to print the 1st node at each horizontal level from top(minimum x_coodinate) that's it. 
# since remaining node at same horizontal level won't be visible when we will from see from top.

# just calculate the minimum and maximum horizontal level 
# now for each each horizonatl level in the range (mi_hori to max_hori), print the 1st node 
# time: O(n^2)


# method 2:
# just store the (coor_y, node.val) as value wrt coor_x in a dictionary
# after that print the 1st node value for each value
# Time: O(n*logn)

# checked the output in leetcode giving correct one but at GFg giving error don't know why
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
        
        dfs(root,0,0)
        
        for hori in range(self.min_h, self.max_h+ 1):
            for key, val in sorted(dic[hori]):    
                print(val,end=" ")  # only you have to print the 1st node at each hori level(i,e with minimum y coordinate) 
                break
    