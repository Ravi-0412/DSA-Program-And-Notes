# submitted on gfg
# time: O(n)

def levelOrder(self,root ):
        Q= [root]
        ans= []
        while Q:
            curr= Q.pop(0)
            ans.append(curr.data)
            if curr.left!= None:
                Q.append(curr.left)
            if curr.right!= None:
                Q.append(curr.right)
        return ans


# for leetcode
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root== None:
        #     return root
        # Q= []
        # Q.append(root)
        # ans= []
        # while Q:   
        #     i = len(Q)
        #     smallAns= []
        #     while i>0:
        #         curr= Q.pop(0)  # pop(0) takes O(n) due to shifting of elements
        #         smallAns.append(curr.val)
        #         if curr.left!= None:
        #             Q.append(curr.left)
        #         if curr.right!= None:
        #             Q.append(curr.right)
        #         i-= 1
        #     if smallAns:
        #         ans.append(smallAns)
        # return ans
    
    
        # if root== None:
        #     return root
        # q= collections.deque()
        # q.append(root)
        # ans= []
        # while q:
        #     qLen= len(q)
        #     level= []
        #     for i in range(qLen): #will put in list the node level by level
        #         curr= q.popleft()     # popleft() takes O(1)
        #         level.append(curr.val)
        #         if curr.left:   
        #             q.append(curr.left)
        #         if curr.right:
        #             q.append(curr.right)
        #     if level:
        #         ans.append(level)
        # return ans

