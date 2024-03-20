# method 1: do any traversal and then sort the ans and then return the kth ele from start
# time: O(n*logn), space: O(n)

# method 2: just find the inorder traversal of the tree and return the kth element from the start
# inorder always give the ans in sorted form for BST
# time: O(n), space: O(n) for ans + recursion depth

# method 3: rather than storing the ans in any array just keep a count for method 2
# and increment the count when you add any ele to the ans 
# and when count reaches 'k' just print the value of that node
# time: O(n), space: O(n) recursion depth

# to avoid the space complexity in method 3
# use the morris inorder traversal



