# you will go and keep updating from root then it will not work since after updating at start
# any root may have more data values than sum of children(as children will get updated also to maintain the property) and decrement is not allowed

# so start updating from bottom to top
# this giving incorrect ans for some test cases but i am not able to cross check due to input syntax : coding ninja
# have to ask someone
def changeTree(root):
    if  root== None or (root.left== None and root.right== None):  # if root is None or root is a leaf 
        return 
    changeTree(root.left)
    changeTree(root.right)
    sum= 0
    if root.left or root.right:   # if root has any of child as not None
        if root.left:
            sum+= root.left.data
        if root.right:
            sum+= root.right.data
        diff= abs((sum- root.data))
        if root.data< sum:  # then make the root.data=  sum
            root.data= sum
        elif root.data> sum:  # then incr the any of the child data by the diff if exist 
            if root.left:
                root.left.data= root.left.data+ diff
            elif root.right:
                root.right.data= root.right.data+ diff


# methid 2: submitted on coding ninja
# if root data > child update the both child data= root.data
# it will make sure that root  data has values not more than the values of children later after children get updated
# later update the root value by sum of values of its children

def changeTree(root):
    if  root== None:  # if root is None or root is a leaf 
        return 
    child= 0  # store the ans of data sum of children
    if root.left:
        child+= root.left.data
    if root.right:
        child+= root.right.data
    if root.data> child:  # child < root.data then make both child data= root.data
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

# Doubt: for just above solution, if we update the children= root.data automatically withou checking anything then it should also work but it's not working
# have to ask someone
