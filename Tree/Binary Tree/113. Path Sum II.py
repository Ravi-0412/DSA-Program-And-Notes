# time: O(n^2).
# we are visiting every node only once but we are copying the path into 'ans'.
# Each time it can cost O(n), since no of leaf is O(n/2) ..
# so time: O(n^2)

# logic: keep adding the node value into ans and keep decr the target.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans, path= [], []
        self.AllPath(root, targetSum, path, ans)
        return ans
    
    def AllPath(self, root, target, path, ans):
        if root== None:  # this should be the 1st base case.
            return
        if target== root.val and root.left== None and root.right== None: # value is equal to remaining target and root is a leaf.
            ans.append(path + [root.val]) 
            return
        self.AllPath(root.left, target- root.val, path + [root.val], ans)
        self.AllPath(root.right, target- root.val, path + [root.val], ans)


# my mistake : This will print the every path two times
# Because when target will become zero at any node then that will call its child to print the ans.
# so we will get same ans two times for left and right child as well.
# Also this can give ans when it will not reach the leaf node also since we are only checking with target.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans, path= [], []
        self.AllPath(root, targetSum, path, ans)
        return ans
    
    def AllPath(self, root, target, path, ans):
        if target== 0:
            ans.append(path)
            return
        if root== None:
            return 
        self.AllPath(root.left, target- root.val, path + [root.val], ans)
        self.AllPath(root.right, target- root.val, path + [root.val], ans)



# Try to do iteratively using bfs and using stack also.(link in sheet)
# Think yourself and do.


# Related Q:
# 1) 129. Sum Root to Leaf Numbers