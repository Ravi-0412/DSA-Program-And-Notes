# method 1 :
# just told what they told to do.
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans= []
        cur= head
        n= 0
        while cur:
            n+= 1
            cur= cur.next
        minPartSize= n // k   # minimum size of each part should be this only.
        extraNode= n % k      # after giving minPartSize to each list, we will left with this much extra node
        # "extraNode" this much list will contain one extra node i.e 'minPartSize +1' and all other will contain no of node= "minPartSize".

        # first diving the list including the extra node also i.e "extraNode" no of list will have "minPartSize +1" nodes.
        # since we have to keep list with more number of nodes at first
        cur= head  # Will point to next node from we have to include.
        for i in range(extraNode):
            ll= cur1= ListNode(0)  
            count= 0
            while cur and count < minPartSize +1:
                cur1.next= cur
                cur= cur.next
                cur1= cur1.next
                count+= 1
            cur1.next= None  # otherwise will take the list till end from the starting node of that part.
            ans.append(ll.next)

        # Now making the linklist with equal no of node having node 'count= minPartSize' 
        # and no of such list will be 'k-extra' 
        for i in range(k- extraNode):
            ll= cur1= ListNode(0)  
            count= 0
            while cur and count < minPartSize:
                cur1.next= cur
                cur= cur.next
                cur1= cur1.next
                count+= 1
            cur1.next= None
            ans.append(ll.next)
        
        return ans
    

# method 2: 
# same logic but very concise
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur= head
        n= 0
        while cur:
            n+= 1
            cur= cur.next
        minPartSize= n // k   # minimum size of each part should be this only.
        extraNode= n % k      # after giving minPartSize to each list, we will left with this much extra node
        # "extraNode" this much list will contain one extra node i.e 'minPartSize +1' and all other will contain no of node= "minPartSize".
        ans= [minPartSize + 1] * extraNode + [minPartSize ] * (k- extraNode)
        pre, cur= None, head
        for ind, num in enumerate(ans):
            if pre: # means we have found the ans. and pre will pointing to the last node of last part
                pre.next= None
            ans[ind]= cur   # cur will be pointing to the 1st node for cur part. 
            for i in range(num):
                pre, cur= cur, cur.next
        return ans
