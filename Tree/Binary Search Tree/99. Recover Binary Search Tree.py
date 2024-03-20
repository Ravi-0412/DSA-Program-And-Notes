# method 1: just find the inorder traversal  say : inorder
# and keep and extra array for sorted inorder traveresal say: sorted_inorder
# now compare the values in both the array , whenever you will find any mismatch that will be our ans
# i.e we have to swap those two nodes where they will mismatch for first time

# now swapping for nodes just search both the nodes and swap

# time: O(n*logn), space: O(n)*2 


# we can little modify the above approach
# first find the sorted array of all the nodes present in tree. for this we can use any traversal and sort that
# now start finding the inorder traversal of tree and when you get any ele just compare that ele with value in the sorted array
# if differ then make that node value equal to the value in sorted array and incr the index in sorted array
# time: O(n*logn), space: O(n)
# Note vvi: this will be valid for any number of mismatch nodes


# method 2: No need to store the ans/sorted order in array
# also use can avoid this stack extra space by recursion or morris Traversal
# logic: just compare the current ele with the pre one
# if violating then mark the violation
# first_violation_By: will tell the node which violated the BST property first i.e = pre
# first_violation_At: will tell the node at which violation occur
# second_violation_At: will tell curr last node where violation occcured

# now there can be two possibility 
# case1:both the nodes are adjacent, then you will not get the second violation i.e second_violation_At= None
# in this case simply swap the values of 'first_violation_By' and 'first_violation_At'

# 2nd case: both the violating nodes are not adjacent i.e second_violation_At!= None
# in this case simply swap the values of 'first_violation_By' and 'second_violation_At'

# logic: phla violation ka pre lena h(phla wala node) since it's first time and dusra vilation ka dusra node lena h since 2nd violation

# Note: This is only valid if only two nodes are swapped not more than two.

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        if root== None:
            return 
        stack, pre, first_violation_By, first_violation_At, second_violation_At= [], None,None, None,None
        while stack or root:
            while root:
                stack.append(root)
                root= root.left
            # if None, it means no left child then print the stack top and append the 'poped.right'
            # it means we have reached the leftmost node i.e next node in inorder traversal.
            curr= stack.pop()
            if pre and curr.val<= pre.val:  # means violation so update the variables
                if first_violation_By== None:  # first violation only
                    first_violation_By= pre
                    first_violation_At= curr
                else:   # second violation only
                    second_violation_At= curr
            pre= curr
            root= curr.right
                    
        if first_violation_By and second_violation_At:
            # means there is only one violation and both the nodes are adjacent. See the 1st example of LC  
            first_violation_By.val, second_violation_At.val= second_violation_At.val, first_violation_By.val
        elif first_violation_By and first_violation_At: 
            # means there is two violation and both the nodes are not adjacent. See the 2nd example of LC  
            first_violation_By.val, first_violation_At.val= first_violation_At.val, first_violation_By.val


# Note: VVVI for BST problem.. 
# In most of the BST Q,every manipulation and changes is done while we print the node for the inorder traversal.. 
# keep this in mind and try to think what changes you can make there to get the ans.
# this approach is valid in above 80-90 % of BST Q
# Video link: https://www.youtube.com/watch?v=ZWGW7FminDM&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=53

# for avoiding extra space in above Q, just use recursive way and make all these variables global