# logic: just copy the next node val into the node that we have to delete 
# and after that delete the next node

class Solution:
    def deleteNode(self, node):
        node.val= node.next.val
        node.next= node.next.next

# my mistake: Didn't read the Q properly, i was thinking to delete the node itself and got stuck
# but Q is something else, doesn't mean that node should be deleted from the memory

# Note: Read all the Q proeprly then only try to solve according to the meaning of Q, don't go on the way you were solving the Q always