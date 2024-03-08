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

# No need to take 'ans' in function call, can take as global variable.

# Q: for printing the depth of a node from a root

# just keep 'depth' also as parameter and once you find the node return the depth.
