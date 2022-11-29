# # just totally same as vertical order traversal(copied that code only)

# logic: you have to print the 1st node at each horizonatl level from bottom(maximum y_coor from root) that's it 
# since remaining node at same horizontal level won't be visible when seen from bottom

# or you can say for each horizonatal level take the only ele with maximum y coordinate

# just calculate the minimum and maximum horizontal level 
# now for each each horizonatl level in the range (mi_hori to max_hori), print the 1st node
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_h, max_h= [0], [0]  # minimum horizonatl level and maximum horizontal level
        dic= collections.defaultdict(list)  # will store the (vertical_level,node) as value with horizontal_level as key.
        # since we have to print horizontally(from x_axis to max x_axis) so made horizonatl_level as key 
        # and since case of same x and y coordinate we have to take the node with minimum value first 
        # so we are also storing the vertical_level with node node in the dic.
        # so before adding any value to the ans sort the each key pair by vertical_level 
        # then add in case of same vertical_level , node with smaller values will come first.
        def dfs(root, lvl_h, lvl_v):  # level horizontal, level vertical
            if root== None:
                return
            min_h[0]= min(min_h[0],lvl_h)
            max_h[0]= max(max_h[0],lvl_h)
            dic[lvl_h].append((lvl_v, root.val))
            dfs(root.left, lvl_h-1, lvl_v+1)
            dfs(root.right, lvl_h+1, lvl_v+1)
        
        dfs(root,0,0)   # just a traversla can say preorder

        for hori in range(min_h[0], max_h[0]+ 1):
            for key, val in sorted(dic[hori],reverse= True):    # sorted the value in reverse order to bring nodes with maximum y coor first
                print(val,end=" ")
                break

