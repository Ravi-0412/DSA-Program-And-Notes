# method 2: find the path of each node from root
# time: O(n^2)

# method 2: 
# just start from root and store the maxValue seen till now.
# And if current node has value>= max_seen_till now then incr the count and update the max_seen

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count, ans= 0, []
        def dfs(root, maxSeen):
            if root== None:
                return
            if root.val>= maxSeen:
                ans.append(root.val)
                self.count+= 1
                maxSeen= root.val
            dfs(root.left, maxSeen)
            dfs(root.right, maxSeen)
        
        dfs(root,root.val)
        return self.count


# my mistake:
# first: i was only checking with the pre (parent value), should have thought little more
# and after knowing the logic, i implemented like this.
# stored the max in string thinking it will not change automatically but declaring like this behave as global, so will change automatically

# so we need something that need to be local for every functiin and for that just pass the that thing as variable or string inside the function.
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         self.maxSeen, self.count, ans= str(root.val), 0, []
#         def dfs(root):
#             if root== None:
#                 return
#             if root.val>= int(self.maxSeen):
#                 ans.append(root.val)
#                 self.count+= 1
#                 self.maxSeen= str(root.val)
#             dfs(root.left)
#             dfs(root.right)
        
#         dfs(root)
#         print(ans)
#         return self.count