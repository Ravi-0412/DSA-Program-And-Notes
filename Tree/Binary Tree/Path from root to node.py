# this i checked on leetcode giving correct output
# here you have to stop once you find the node
# so for this if we get True we are simply just returning that 
def Path(root,key):
    ans= []
    if helper(root,key,ans)== False:
        print("not present")
    else:
        return [ans[::-1]]
# this will add the path in reverse order
def helper(root,key,ans):  
    if root== None:
        return False
    if root.val== key:
        ans.append(root.val)
        return True
    l= helper(root.left,key,ans)
    r= helper(root.right,key,ans)
    if l or r:  # if any of its child return True then it means 'key' has path from curr root so add in ans
        ans.append(root.val)
        return True
    else:
        return False


# other way backtracking 
# better one, just the same logic only 
# only diff here we are appending when we are seeing the node
def Path(root,key):
    ans= []
    if helper(root,key,ans)== False:
        print("not present")
    else:
        return [ans]

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



