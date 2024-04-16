# Logic: At depth 'depth-1' create two nodes with different name for each not null node and 
# change the pointer.
# And we only need to go till 'depth-1' . so better use bfs.

# Note: If you will create newNode with same name then you will duplication as 
# both left and right subtree will get added to each of the formed node if same name.
# But we want only to add left and right subtree to newly created node respectively.

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            cur = TreeNode(val)
            cur.left = root
            return cur
        q = collections.deque([root])
        d = 1
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if d == depth - 1:
                    newNode1, newNode2 =  TreeNode(val), TreeNode(val)
                    # temp_left , temp_right = cur.left, cur.right
                    # cur.left , cur.right = newNode1, newNode2
                    # newNode1.left, newNode2.right = temp_left, temp_right
                    cur.left , newNode1.left, cur.right, newNode2.right = newNode1, cur.left, newNode2, cur.right  
                    # shortcut of above three line. Here changes will happen simultaneoulsy i.e with structure till now         
                if d <  depth - 1:
                    # we only need to go till nodes of 'depth -1' 
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            d += 1
        return root