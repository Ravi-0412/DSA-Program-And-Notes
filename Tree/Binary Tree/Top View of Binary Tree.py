# # just totally same as vertical order traversal(copied that code only)

# logic: root pe baith jao and h jo node tmko dikhe usko print karna h..tm sirf har horizonaty sirf ek hi node top wala hi dekh paoge.
# you have to print the 1st node at each horizonatl level that's from top(minimum y_coor from root) that's it. 
# since remaining node at same horizontal level won't be visible when seen from top

# or you can say for each horizonatal level take the only ele with minimum y coordinate

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
        min_h, max_h= [0], [0]  # minimum horizonatl level and maximum horizontal level
        dic= collections.defaultdict(list)  # will store the (vertical_level,node) as value with horizontal_level as key
        # since we have to print horizontally(from min x_axis to max x_axis) so made horizonatl_level as key 
        # and since case of same x and y coordinate we have to take the node with minimum value first so we are also storing the vertical_level with node node in the dic
        # so before adding any value to the ans sort the each key pair by vertical_level then add in case of same vertical_level , node with smaller values will come first
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
            for key, val in sorted(dic[hori]):    # this will sort all the node at each hori level acc to the y_coordinate 
                print(val,end=" ")  # only you have to print the 1st node at each hori level(i,e with minimum y coordinate) 
                break
    