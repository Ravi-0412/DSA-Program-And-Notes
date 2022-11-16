# when you will append any new node then it always will get added with num= 1
# and for any just the one next child that comes in meaning of that traversal after printing the root like:
# for preorder next will be 'left', for inorder next will be 'right' and for postorder next will be nothing

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre, inorder,post,stack= [],[],[],[(root,1)]
        while stack:
            curr, num= stack.pop()
            # preorder
            if num== 1:  # add in preorder and make num= 2and then again append curr in stack with updated num
                pre.append(curr.val)
                num= 2
                stack.append((curr,num))
                # if left child exixt then append that with num= 1
                if curr.left:
                    num= 1
                    stack.append((curr.left,num))
            # Inorder case 
            elif num== 2:  # add in inorder and make num= 3 and then again append curr in stack with updated num
                inorder.append(curr.val)
                num= 3
                stack.append((curr,num))
                # if right child exixt then append that with num= 1
                if curr.right:
                    num= 1
                    stack.append((curr.right,num))
            # postorder
            elif num==3:
                post.append(curr.val)
        
        print(pre,inorder,post)

