# Brute force :
# find the minimum horizontal distance and maximum horizontal distance, by taking distance of left child as '-1- and for right child as '+1' always
# minimum will be for leftmost leaf node and max will be rightmost leaf node

# for coordinates: just stand at root(assume root as origin as given also) (0,0) and left side of root will be negative x coordinate
# and right side of root will be positive x coordinate , and  y coordinate will be always positive .. x axis on left and right side and y axis on top to bottom
# so just think we are printing horizonatlly from min_horizontal to max_horizontal

# now for each horizonatl distance in range find all the nodes matching to gievn horizontal distance and add into the ans
# time: O(n^2) , for each horizontal level we are find the nodes that matches with given horizonatl level
# but this will not print the node in sorted value when they belong to same vertical and horizonatl level (work on GFG but on leetcode)
# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        minHD, maxHD= [0],[0]
        # find the minimum and maximum horizontal distance in the tree
        # min will be at leftmost root and maximum will be at rightmost root
        self.FindHD(root, minHD, maxHD,0)  # also a traversal only  preorder
        print(minHD, maxHD)
        
        # now print the node from minHD to maxHD which matches with the given horizontal distance
        ans, level= [], []
        for line in range(minHD[0], maxHD[0]+1):
            self.PrintNode(root, level, line, 0)      # it just a traversal totally preorder
            ans.append(level)
            level= []
        return ans
    
    # hd: taking horizontal distance of left child to be -1 and for right child +1
    def FindHD(self, root, minHD, maxHD, hd):
        if root== None:
            return 
        if hd < minHD[0]:
            minHD[0]= hd
        elif hd> maxHD[0]:
            maxHD[0]= hd
        self.FindHD(root.left, minHD, maxHD, hd-1)
        self.FindHD(root.right, minHD, maxHD, hd+1)
    
    # if node level hd matches with level just add that into the ans
    def PrintNode(self, root, level, line , hd):
        if root== None:
            return 
        if hd== line:
            level.append(root.val)
        self.PrintNode(root.left, level, line , hd-1)
        self.PrintNode(root.right, level, line , hd+1)


# method 2:
# time; O(n*logn). for hashmapo buliding its O(n) only but for adding into ans we haev to sort the node at each level so n*logn
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/777584/Python-Simple-dfs-explained
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        min_h, max_h= [0], [0]  # minimum horizonatl level and maximum horizontal level
        dic= collections.defaultdict(list)  # will store the (vertical_level,node) as value with horizontal_level as key
        # since we have to print horizontally(from x_axis to max x_axis) so made horizonatl_level as key 
        # and since case of same x and y coordinate we have to take the node with minimum value first so we are also storing the vertical_level with node node in the dic
        # so before adding any value to the ans sort the each key pair by vertical_level then add in case of same vertical_level , node with smaller values will come first
        def dfs(root, lvl_h, lvl_v):  # level horizontal, level vertical
            if root== None:
                return
            min_h[0]= min(min_h[0],lvl_h)
            max_h[0]= max(max_h[0],lvl_h)
            dic[lvl_h].append((lvl_v, root.val))
            dfs(root.left, lvl_h-1, lvl_v+1)     # left node lies at (col-1,row+1), horizontal level->column and vertical level -> row
            dfs(root.right, lvl_h+1, lvl_v+1)    # right node lies at (col-1,row+1)
        
        dfs(root,0,0)   # just a traversla can say preorder
        # now print the all nodes horizonatl level wise, and sort the value by 1st val (acc to vertical_level)  adding into ans 

# do by iterative way later all the view based q