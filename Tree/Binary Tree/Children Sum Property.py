# if you will go and keep updating from root then it will not work since after updating at start
# any root may have more/less data values than sum of children(as children will get updated also to maintain the property).

# vvi: Decrement is not allowed.

# my Method and mistake: 
# vvi: keep in mind decrement operation is not allowed.

# we are blindly updating the node values with sum of its children values going Bottom up.
# But while updating the current node value we might be decreasing node value also ,say 
# node val= 50 and after updating its left_child_val= 10 and right_child_val= 15
#  then, when we will update cur node val to sum of its children then  
# node_val= 25 but it is less than its current value(50) which is not allowed(since decrement operation is not allowed).

# note: It will work fine when both increment and decrement operation is allowed.

# logic: just go Bottom up and make node values= sum of its children.
def changeTree(root): 
    
    def dfs(node):
        if not node:
            return 0
        # if leaf simply return its node value
        if node.left== None and node.right== None: 
            return node.data
        l= dfs(node.left)
        r= dfs(node.right)
        # make node value = sum of its children
        node.data= l  + r  
        return node.data
        
    dfs(root)
    return root

# Correct one

# to solve the mistake in above Q,
# we have to make sure that while updating the values going Bottom up, we only incr the node value.
# for this we have to make sure that root  data has values not more than the values of children later after children get updated

# For this make both left and right child data = root.data when you see any node (root) for first time, 
# if root.data > sum_children.

# therefore when you will update the cur node value while becoming back then node_val <= sum of its children value.
# so we will simply update the cur node value = sum of its children.(only incr operation we will have to do).

# if while going top to bottom, if node_val<= children_value then do nothing.

# Note: in short => 1st top-down then bottom-up

def changeTree(root):
    if  root== None:  # if root is None 
        return
    # find the sum of its child values
    child= 0  # store the ans of data sum of children
    if root.left:
        child+= root.left.data
    if root.right:
        child+= root.right.data
    # if child < root.data then make both child data= root.data
    if root.data > child:  
        if root.left:
            root.left.data= root.data
        elif root.right:
            root.right.data= root.data
    changeTree(root.left)
    changeTree(root.right)
    # now update the root value with sum of values of children
    update_root= 0
    if root.left:
        update_root+= root.left.data
    if root.right:
        update_root+= root.right.data
    if root.left or root.right:
        root.data= update_root




