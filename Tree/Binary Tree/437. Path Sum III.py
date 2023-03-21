# just similar logic as 'Two sum'.

# Brute force: just like we do in Two sum.
# from every node , count the ans possible.
# we can use any traversal to call the function to find the ans from each node.
# time: O(n^2)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root== None:
            return 0
        self.noPaths= 0

        self.dfs(root, targetSum)   # can do any traversal
        return self.noPaths
    
    def dfs(self, root, target):  # calling for each node one by one.
        if root== None:
            return 
        self.AllPath(root, target)   # checking if we ca get any path starting from this node.
        self.dfs(root.left, target)
        self.dfs(root.right, target)
    
    def AllPath(self, root, target):
        if root== None:
            return
        if root.val== target:
            self.noPaths+= 1
            # return    # as we can get the ans also after this from same root like we get both positive and negative nodes.
        self.AllPath(root.left, target- root.val)
        self.AllPath(root.right, target- root.val)

# optimisng to O(n): DP
# just like we do Two sum.
# Read the solutions in link and watch video for explanation.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root, preSum):
            if not root:
                return 
            curSum= preSum + root.val
            # (curSum- targetSum) : extra sum , just like remaining sum of 'Two Sum'.
            # agar hm us extra sum '(curSum- targetSum)' tak  ke nodes(may be more than one) ko hta de to hmko 'target' mil jaygea. (After that node to current node).
            # Hm curSum ho hashmap me dal rhe isliye 'extra sum' jisko remove karne pe continous sum= target ho jaye , check karna hoga.
            if (curSum- targetSum) in preSum_freq:   
                self.count+= preSum_freq[(curSum- targetSum)]
            if curSum in preSum_freq:
                preSum_freq[curSum]+= 1
            else:
                preSum_freq[curSum]= 1
            
            # now call the function for left and right part
            dfs(root.left, curSum)   # now curSum will become preSum
            dfs(root.right, curSum)
            preSum_freq[curSum]-= 1    # now current branch is not going to matter anymore. 

        self.count= 0
        preSum_freq= {0: 1}   # By default we can get sum== 0 by one way. Taking fre because there can be more than one path possible.
        dfs(root, 0)   # 0: preSum
        return self.count

        
