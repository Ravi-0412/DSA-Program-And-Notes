# first add the left boundary node then the leaf nodes and then right boundary nodes

class Solution:
    def printBoundaryView(self, root):
        ans= []
        if root.left!= None or root.right!= None: # if not a leaf node
            ans.append(root.data)
        # self.LeftBoundary(root, ans)      # calling like this will give wrong ans according the logic we have applied
                                            # so better call from root.left and append root before calling if not None
        self.LeftBoundary(root.left, ans)   # add the left boundaruy ele excluding root
        self.AddLeaves(root, ans)        
        self.RightBoundary(root.right, ans) # add the right boundaruy ele excluding root
        return ans
    
    def LeftBoundary(self,root,ans):
        curr= root
        #  hmko yahan wapas kisi node pe nhi aana h kisi bhi subtree me, ek hi direction me chalte rhna h
        # isliye stack ki koi jaroorat nhi
        while curr:  
            # check for non leaf before adding
            if curr.left!= None or curr.right!= None:
                ans.append(curr.data)
            if curr.left:
                curr= curr.left
            elif curr.left== None:
                curr= curr.right   # if even curr.right will be None then it means that curr node was leaf and now curr will point to None 
                                   # and will come out of loop means we have completed the traversal for left boundary
    def AddLeaves(self,root, ans):
        if root== None:
            return 
        if root.left==None and root.right== None: # if leaf add into the ans
            ans.append(root.data)
            return
        self.AddLeaves(root.left, ans)
        self.AddLeaves(root.right, ans)
        
    
    def RightBoundary(self,root,ans):
        curr= root
        temp= []
        while curr:
            # take a temp array , as we have to add in reverse order 

            # check for non leaf before adding
            if curr.left!= None or curr.right!= None:
                temp.append(curr.data)
            if curr.right:
                curr= curr.right 
            elif curr.right== None:
                curr= curr.left   # if even curr.left will be None then it means that curr node was leaf and now curr will point to None 
                                   # and will come out of loop means we have completed the traversal for right boundary
        ans+= temp[::-1]


