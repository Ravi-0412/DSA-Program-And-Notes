# They are telling to connect all nodes at sam elevel by right pointer.
# and whenenver we have to do something levelwise, first thing should come into mind is 'Level Order Traversal'(MultiSource Bfs)
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root== None:
            return root
        q= deque([root])
        while q:
            pre= None
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if pre:  # not None
                    pre.next= curr
                    pre= pre.next
                else: # if poped one is the first node at the current level
                    pre= curr
        return root