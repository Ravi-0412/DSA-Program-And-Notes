# Similar logic as: "1008. Construct Binary Search Tree from Preorder Traversal"

# logic: Since here last node will be the parent so we will traverse from right side(root side).
# if any ele will be greater that will be right child and we can add them directly to the right of tree.
# And if smaller then we we have to search for the node for which 'num' will be the left child.
# Reason for above logic: for post (left, right, root). so if greater then will go to right side directly.

# vvi: Difference from 'given preoder and construct BST'?
# Ans: 1) in preorder we were traversing from left to right(from root) and here from right to left (from root only).
# 2) in preoder if 'num' was smaller then we were directly adding and in this we are directly adding if num is greater.

# time= space= O(n)

class Solution:
    def constructTree(self,post,n):
        n= len(post)
        root=  Node(post[-1])  # last ele will be the root only.
        stack= [root]
        for i in range(n-2, -1, -1):
            num= post[i]
            node= Node(num)
            if num > stack[-1].val:  # means num will be the right child. so directly add.
                stack[-1].right= node
            else: # Finding the last greater ele than 'num' in stack for which 'num' can be the left child.
                #  so pop until you find any smaller ele than 'num'.
                while stack and num < stack[-1].val:
                    last= stack.pop()
                # last will be the just greater than 'num' and num will be the left of 'last' only.
                last.left= node
            stack.append(node)
        return root
