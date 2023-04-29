# just same logic as 'level order traversal'
# we have to calculate ans for each level in same way(exact same code).

# only thing we have to change the direction of output at alternate level
# i.e we have to print in revese at alternate level
# for this we have taken a variable count
# if count is even means we have to print from left to right(as usual)
# if count is odd means we have to print from right to left(so in this case first reverse the levelwise ans and then append in final ans)

# time: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root== None:
            return root
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
            if (count%2==0):  # left to right
                ans.append(level)
            else:
                ans.append(level[::-1])  # reverse in this case then add to ans
            count+= 1
        return ans

# very concise way of same method
# better one
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


