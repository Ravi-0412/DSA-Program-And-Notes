# just same logic as 'level order traversal'
# only thing we have to change the direction of output at alternate level
# i.e we have to print in revese at alternate level
# for this we have taken a variable count
# if count is even means we have to print from left to right(as usual)
# if count is odd means we have to print from right to left(so in this case first reverse the levelwise ans and then append in final ans)

# time: O(n)
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root== None:
            return root
        import collections
        q= collections.deque()
        q.append(root)
        ans,count= [],0
        while q:
            qLen= len(q)
            level= []
            for i in range(qLen): # will iterate for each level
                curr= q.popleft()     # popleft() takes O(1)
                level.append(curr.val)
                if curr.left:   
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level and (count%2==0):
                ans.append(level)
            else:
                ans.append(level[::-1])  # reverse in this case then add to ans
            count+= 1
        return ans

# very concise way of same method
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        q, ans, direction= deque([root]), [], 1
        while q:
            level= []
            for i in range(len(q)):
                curr= q.popleft()
                level.append(curr.val)
                if curr.left:  q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(level[::direction])  # adding in final ans like this
            direction*= -1  # for adding in reverse order in next iteration
        return ans


# method 2: using 2 stack
# odd stack will hold the odd level ele and even stack will hold the even level ele
# but push in stack according to the order in which you have to print
# in odd level you have to print right to left, so append in odd stack
# right first then left as you are using stack and 
# for even level just opposite
# and other things are totally same
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack_odd, stack_even, ans, level= [], [], [], 1
        if not root:
            return root
        stack_odd.append(root)
        level+= 1
        while stack_odd or stack_even:
            level_wise= []
            if level%2!= 0:
                while stack_even:
                    curr= stack_even.pop()
                    level_wise.append(curr.val)
                    if curr.right:
                        stack_odd.append(curr.right)
                    if curr.left:
                        stack_odd.append(curr.left)
            else:
                while stack_odd:
                    curr= stack_odd.pop()
                    level_wise.append(curr.val)
                    if curr.left:
                        stack_even.append(curr.left)
                    if curr.right:
                        stack_even.append(curr.right)
            level+= 1
            ans.append(level_wise)
        return ans
