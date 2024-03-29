
# method 1:
# as you can see clearly that we have to print the last node at each level i.e we have to print only the rightmost node at each level
# so applied the exactly same logic of "level order traversal" and for each level put only the last ele at that level that's it

# why ? Because all other nodes at same level won't be visible.

# unusual way python work(shocked)
# i was thinking when we will print the value of 'i' outside the function then it will be '4'(value passed inside range)
# but it stops at max possible value only
for i in range(4):
    print(i,"in")
print(i)   # will print '3' only


# optimising the space complexity in above method
# we are unnecessarily adding all the node in level array at each level but we only need the last node value at each level
# and last node val, we will get after each 'for' loop
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return root
        ans= []
        q= deque([root])
        while q:
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans+= [curr.val]  # last poped node will be the rightmost node
        return ans


# or you can append in ans before for loop also
# better one.
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return root
        ans= []
        q= deque([root])
        while q:
            ans+= [q[-1].val]   # appending the last node value at each level
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans


# Recursive way
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        # just preorder traversal only. just we are traversing first right before left because we have to add right node first if exist
        def dfs(root, level): 
            if root== None:
                return
            if level== len(ans):  # means at that level no node has been added.  
                # this is the first node from the right at that level so add in the ans
                ans.append(root.val)
            dfs(root.right, level+1)
            dfs(root.left,  level+1)
    
        dfs(root, 0)
        return ans


# Method 2:
# this can also be done by the vertical order approaches 
# here key= vertical_level and value will be a pair of (hori_level, node.val)
# and we have to traverse from min depth i.e= 0 to max depth(range of vertical level)
# after that print the value with max horizonatl level that's it 
# but time complexity of this will go O(n*logn)

