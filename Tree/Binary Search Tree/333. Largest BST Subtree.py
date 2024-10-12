
# method 1: Brute force
# go to every node and check whether subtree from that node is valid or not using "validate bst"
# if valid calculate the no of nodes in bst and keep updating the ans
# time: O(n^2)


# method 2:
# just traverse Bottom up. DP only
# since you need values of both left and right subtree to make decision for current node so go bottom up. 

# For each node we need three values :
# 1) Minimum node value starting from that node.
# 2) Maximum node value starting from that node.
# 3) Size of BST starting from that node.

# if none then return any valid NodeValue

# video: https://www.youtube.com/watch?v=X0oXMdtUDwo&t=10s
class NodeValue:
    def __init__(self,minValue, maxValue, maxSize):
        # For each node we need three values :
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
        # left side ka max valuse se root.data greater hona chahiye and
        # right side ke minimum value se root.val smaller hona chahiye
        if l.maxValue < root.data  and root.data < r.minValue:   # means BST
            # for minimum and maximum comparing with root.data to handle the returning values for root= None
            return NodeValue(min(l.minValue, root.data), max(root.data, r.maxValue), l.maxSize+ r.maxSize +1)
        # not BST. return any NodeValue which can't be included in ans but size should be maintained.
        # Always give incorrect while comparison i.e # min->minPossible, max->maxPossible
        return NodeValue(-999999, 999999, max(l.maxSize, r.maxSize)) 
    

# Easier one and very better one of above exact logic
# For each node we need three values , so returning those values from each node.
# 1) Minimum node value starting from that node.
# 2) Maximum node value starting from that node.
# 3) Size of BST starting from that node.

class Solution:
    def largestBst(self, root):
        
        self.ans = 0
        
        def maxSizeBst(root):
            if not root:
                return [999999, -999999, 0]
            min1, max1, size1 = maxSizeBst(root.left)
            min2, max2, size2 = maxSizeBst(root.right)
            # check including root is bst or not
            if max1 < root.data and root.data < min2:
                self.ans = max(self.ans, 1 + size1 + size2)
                return [min(min1, root.data), max(max2, root.data), 1 + size1 + size2]
            else:
                self.ans = max(self.ans, size1, size2)
                return [-999999, 999999, 0]
        
        maxSizeBst(root)
        
        return self.ans
