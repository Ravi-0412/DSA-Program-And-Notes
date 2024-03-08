# method 1:

# logic: if we perform level order traversal then 'null' node should not come before any of the 'Not_null' node,
#  in case of complete binary tree OR when we encount any 'null' node then after no 'not_null' souldn't come, all node should be 'null only'.
# in this insert the 'null' node also.

# vvi: To make sure the above condition, we will check if we have found the 'none' in level before or in current level before.

# why level order traversal?
# Ans: since we have to check from left to right in same level so.
# time: O(n)
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q= collections.deque([root])
        nullFound= False
        while q:
            cur= q.popleft()
            if not cur:  # mark and keep skipping
                nullFound= True
                continue  # we will check if 'nullfound= True' from next time. 
                          # checking this time will give wrong ans because all nodes can ne 'none' after this node.
            if nullFound:  # means we have found 'null' node before a 'not_null', node or we have found 'not_null' after null node in same level or level before
                return False
            q.append(cur.left)
            q.append(cur.right)
        return True

# other way : my mistake
# Here we are checking current 'None' found with next level .
# here we are checking the child not the node value direct as 'None'.
# so we will get wrong ans. (we will get False in case of True also).
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q= collections.deque([root])
        nullFound= False
        while q:
            if nullFound: return False
            cur= q.popleft()
            if cur.left:    
                q.append(cur.left)
            else:
                nullFound= True   # leading to next level since we are checking the child.
            if cur.right:
                q.append(cur.right)
            else:
                nullFound= True

        return True

# method 2:
# logic: if we write the position of each node in array form starting from index '1',
# ie. for left child= 2*index, right child= 2*index +1, where index= index of parent then
# maxIndex to which all these nodes go in the array and no of nodes both should be same only(both strting from 1).
# so just checking that by keeping track of 'maxIndex' and 'nodecount'.

# just same code as we find the no of nodes, only using one more para 'index'
#  to put that node at index 'index' in array when we will start index from '1'.

# This method will also help in checking whether tree follow heap property or not.
# heap: complete BST + min/max heap

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        self.maxIndex= 0
        self.nodeCount= 0

        def checkCompleteTree(root, index):
            if root == None:
                return
            self.nodeCount+= 1 
            self.maxIndex= max(self.maxIndex, index)
            checkCompleteTree(root.left, 2*index)
            checkCompleteTree(root.right, 2*index +1)

        checkCompleteTree(root, 1)  
        print(self.maxIndex, self.nodeCount) 
        return self.maxIndex== self.nodeCount

