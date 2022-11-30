
# method 1: Brute force
# go to every node and check whether subtree from that node is valid or not using "validate bst"
# if valid calculate the no of nodes in bst and keep updating the ans
# time: O(n^2)


# method 2:
# correct one only
# just traverse Bottom up. DP only
# since you need values of both left and right subtree to make decision like we used in DP Q of string so call them first and then make a decision 
# and according to decison return value.
# if none then return any valid NodeValue

# video: https://www.youtube.com/watch?v=X0oXMdtUDwo&t=10s
class NodeValue:
    def __init__(self,minValue, maxValue, maxSize):
        self.minValue= minValue
        self.maxValue= maxValue
        self.maxSize=  maxSize

class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        return self.helper(root).maxSize
    
    def helper(self,root):
        if root== None:
            # return a node with any nodevalue which can be always valid when compared
            return NodeValue(999999, -999999, 0)  # minvalue-> max possible,maxvalue->min possible, size= 0
        l= self.helper(root.left)
        r= self.helper(root.right)
        
        # now comapre the values and check if bst or not. just like bottom up DP
        if l.maxValue< root.val  and root.val< r.minValue:   # means BST
            return NodeValue(min(l.minValue, root.val), max(root.val, r.maxValue), l.maxSize+ r.maxSize +1)
        else: # not BST. return any NodeValue which can be included in ans but size should be maintained
            return NodeValue(-999999, 999999, max(l.maxSize, r.maxSize)) # min->minPossible, max->maxPossible