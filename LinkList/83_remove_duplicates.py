# submitted on leetcode
# method 1:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        # we are joining distinct node with the help of temp
        temp= head  # temp will always point to the pre distinct ele
        current= head.next  # will point from the 2nd ele 
        while current!=None:
            if current.val== temp.val:  # if duplicates 
                temp.next= current.next  # skipping the duplicates, thinking next node might be distinct
            else:
                # here temp.next already be pointing to the distinct node than 'temp' so simply make temp = temp.next
                temp= temp.next
            current= current.next 
        return head


# my mistake for above solution:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None:
            return head
        temp= head
        current= head
        while current.next:
            if current.next.val== temp.val:
                temp.next= current.next.next
                current= current.next  # here you are incr one step and this can make current point to 'None' so
                                    # after this in while condition it will give 'error' like: "None type object has no attribute 'next' "
            else:
                temp= temp.next
                currrent= current.next  # i wrote wrong here left side 'currrent' : 3 'r'
        return head


# method 2 : concise way of method 1
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr= head
        while curr: 
            while curr.next and curr.next.val== curr.val:
                curr.next= curr.next.next
            curr= curr.next
        return head
    
# my mistake: i was missing 1st while loop



# method 3: By recursion (have to look once properly and understand)
# logic: just keep on calling the function and after each call check for duplicates
# if duplicates then connect with next duplicate and skip the 1st one(if duplicates then it will get connected to last node of duplicate not 1st one) else return head

# better one to understand:
# agar aage wala node ka value same h to hm apne aap ko usme include nhi kar sakte isliye 'head.next' return kar denge
# agar aage wala node ka value different h to hm apne aap ko usme include kar sakte isliye apna value include karke return kar denge, isliye 'head' return kar rhe

def deleteDuplicates(self, head):
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head



# getting error and don't able to do when trying to skip later ele in case of duplicates
# try later or ask someone this approach
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            if head.val== head.next.val:
                head.next= self.deleteDuplicates(head.next.next)
            else:
                head.next= self.deleteDuplicates(head.next)
        return head

