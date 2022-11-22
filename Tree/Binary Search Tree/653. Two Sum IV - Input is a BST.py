# method 1: store the inorder 
# now problem reduces to "Two sum"
# then apply the two pointer approach for find th epair since inorder will be a sorted array 
# space= time= O(n)

# method 2:
# just store the remaining sum w.r.t each number you pop for inorder 
# After poping check whether that number is present in the hashmap for not
# if already presen then it means sum exist otherwise add the curr poped node into stack


# method 3: just use the 'BST iterator' i.e 'next' and 'prev'
# nect will give element from start i.e samllest one and 'prev' will give element from last i.e largest one
# Now problem reduces to "Two sum" with two pointer approach 'next' and 'prev'
# time: O(n)
# space: O(H)*2= O(H)
# this Q is based on this approach only since in this we are using a lot of proeperty of BST

class BSTIterator:
    def __init__(self, root, reverse):  # taking reverse also so that we don't have to make separate function 
                                        # for getting 'next' and 'prev'
        self.stack= []
        self.reverse= reverse
        self.PushAll(root)
        
    def next(self) -> int:
        temp= self.stack.pop()
        if self.reverse:
            self.PushAll(temp.left)  
        else:
            self.PushAll(temp.right)
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack!= []
    
    def PushAll(self, root):
        # push everything that comes on the left of root
        curr= root
        while curr:
            self.stack.append(curr)
            if self.reverse:  # means we have to get element from last so put all the right nodes into the stack
                curr= curr.right
            else:
                curr= curr.left
                
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        start= BSTIterator(root, False)    # go get element from start i.e smallest one first
        end=   BSTIterator(root, True)     # go get element from end i.e   largest one first so made reverse= "True"
        i= start.next()
        j= end.next()
        while i< j:
            if i + j== k:
                return True
            elif i + j <k:
                i= start.next()
            else: 
                j= end.next()
        return False
