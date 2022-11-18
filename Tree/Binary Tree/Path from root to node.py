# same Q: Search a given node in binary tree

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
    if root.val== key:  # key has been found so traverse back and add the nodes that come in the path
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


# for printing the depth of a node from a root
# just same logic as above
# if node is found then incr the ansa by 1 instead of True and if root== None return 0 instead of False
# True->+1 then return , False->return 0.. append ->+1 in the ans, False->return 0
# and when any root will see non zero value then there is path from this root and then root will also incr the ans by 1 and will retrun the ans
# if both left and right== 0 then node has no path from root so it will retrun 0

# and at last return 'ans-1' since if node is found then root will also add 1 i.e one extra one get added 
# totally same logic as above method 1
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans= [0]
        self.helper(root,6,ans)
        if ans[0]== 0:
            print("node is not present")
            return 
        return ans[0]-1
    # this will add the path in reverse order
    def helper(self,root,key,ans):  
        if root== None:
            return 0
        if root.val== key:  # key has been found so traverse back and add the nodes that come in the path
            ans[0]+= 1
            return ans[0]
        l= self.helper(root.left,key,ans)
        r= self.helper(root.right,key,ans)
        if l!=0 or r!=0:  # if any of its child return True then it means 'key' has path from curr root so add in ans
            ans[0]+= 1
            return ans[0]
        else:
            return 0


# by method 2
# True->return ans , False->decr ans by 1 and then return ans , append ->+1 in the ans
def helper(self,root,key,ans):  
    if root== None:
        return 0
    ans[0]+= 1  # simply add the node you visit
    if root.val== key:
        return ans[0]
    if self.helper(root.left,key,ans) or self.helper(root.right,key,ans):  # means key has path from the given root
        return ans[0]
    # if key has not path from the curr root(neither left nor right return True) then pop root from the ans and return False
    ans[0]-= 1
    return 0

