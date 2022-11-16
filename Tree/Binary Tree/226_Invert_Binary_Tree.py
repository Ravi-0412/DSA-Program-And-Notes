# just change the pointer for each node

def invertTree(self,root) :
        if not root:
            return 
        root.left, root.right= root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        
        
        # converting the above one into iterative using 'BFS'
        # if not root: return root
        # q= deque([root])
        # while q:
        #     curr= q.popleft()
        #     curr.left, curr.right= curr.right, curr.left
        #     if curr.left:
        #         q.append(curr.left)
        #     if curr.right:
        #         q.append(curr.right)
        # return root
        
    
        # converting the above one into iterative using 'DFS'
        # exactly same as BFS, only insert right node first
        
        # if not root: return root
        # stack= [root]
        # while stack:
        #     curr= stack.pop()
        #     curr.left, curr.right= curr.right, curr.left
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        # return root