
# method 1:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        # we are joining distinct node with the help of temp
        temp= head  # temp will always point to the pre distinct ele
        current= head.next  # will point from the 2nd ele 
        while current != None:
            if current.val == temp.val:  # if duplicates 
                temp.next = current.next  # skipping the duplicates, thinking next node might be distinct
            else:
                # here temp.next already be pointing to the distinct node than 'temp' so simply make temp = temp.next
                temp = temp.next
            current = current.next 
        return head


# method 2 : concise way of method 1
# Better one
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head   # cur will point to last distinct ele.
        while curr: 
            while curr.next and curr.next.val== curr.val:
                curr.next= curr.next.next
            curr= curr.next
        return head
    
# my mistake: i was missing 1st while loop



# method 3: By recursion 

# better one to understand:
# agar aage wala node ka value same h to hm apne aap ko usme include nhi kar sakte isliye 'head.next' return kar denge
# agar aage wala node ka value different h to hm apne aap ko usme include kar sakte isliye apna value include karke return kar denge, 
# isliye 'head' return kar rhe.

# Note: Har distinct element ka last node store hoga internally answer me.
# Only last distinct element will get added for each node.

def deleteDuplicates(self, head):
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head   # will act as base case also


