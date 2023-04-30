# same Q: Search a given node in binary tree
# or "Path sum 2"

# these all methods checked on leetcode giving correct output.
# here you have to stop once you find the node
# so for this if we get True we are simply just returning that.

# method 1: 
def Path(root,key):
    ans= []
    if helper(root,key,ans)== False:
        print("not present")
    else:
        return ans

def helper(self,root,key,ans):  
    if root== None:
        return False
    ans.append(root.val)  # simply add the node you visit
    if root.val== key:
        return True
    if helper(root.left,key,ans) or helper(root.right,key,ans):  # means key has path from the given root
        return True
    # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
    ans.pop()
    return False


# Q: for printing the depth of a node from a root

# just same logic as above
# if node is found then incr the ans by 1 instead of True and if root== None return 0 instead of False
# True->+1 then return , False->return 0.. append ->+1 in the depth, False->return 0
# and when any root will see non zero value then there is path from this root and then root will also incr the ans by 1 and will retrun the ans
# if both left and right== 0 then node has no path from root so it will retrun 0

# and at last return 'ans-1' since if node is found then root will also add 1 i.e one extra one get added 
# totally same logic as above method 1


# by method 2
# True->return ans , False->decr ans by 1 and then return ans , append ->+1 in the ans
def helper(self,root,key,depth):  
    if root== None:
        return 0
    depth+= 1  # simply add the node you visit
    if root.val== key:
        return depth
    if self.helper(root.left,key,depth) or self.helper(root.right,key,depth):  # means key has path from the given root(means we have found node with)
        return depth
    # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
    depth-= 1 
    return 0

# after function call ans= 'depth-1'
