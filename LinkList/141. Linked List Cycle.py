# 1st method(i solved):
# if there will be any cycle then length of the linked will
# be more than the maximum no of elements according to the given constraint
# just find the length if >maximum length of the linked list then there 
# will be a loop otherwise not
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        length= 0
        while first:
            if(length>10001):
                return True
            else:
                first= first.next
                length+= 1
        return False


# 2nd method : storing the address into the hashmap or set
# why set came into mind: since we have to find cycle means same address can't repeat again while traversing and
# set only store the unique values
# time: o(n), space: o(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        add = {}
        temp = head
        # traverse the link list and when you see any node
        # for 1st time then store 'True' at the address of that node
        # and if that adress is alreay present then return true
        while temp:
            if temp in add: return True  # means we are visiting that address 
                                          # again means there is a loop
            else: add[temp]= True # at address of temp, making the value =True   , we are storing against the node 
            # so it will take the address of that node automatically as node conatains more than one object
            temp = temp.next
        return False


# my mistake in method 2 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        hashmap= {}
        while first:
            if id(first) not in hashmap: # error in this line 
                hashmap[first.val]= id(first) # error in this line
                # giving error because since we are storing address against the value and ele in the list can repeat with different add
                # so everytime it will change the address when repeating ele will come
                first= first.next
            else:
                return True
        if first== None:
            return False
        

# 3rd method
# time: o(n), space= o(1)
# mark the traversing node as 'visited'
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'visited':  # means we have seen this node before only
                return True
            head.val = 'visited'
            head = head.next
        return False


# 4th method: Floyd's cycle detection algorithm(submitted on GFG)
# time: o(n), space= o(1)
# logic: move the slow pointer one step ahead and 'fast' pointer 
# two steps ahead. And if there will be any cycle then at some time 
# slow== fast means there exist a cycle  since 'fast' was ahead of slow and again they meet means there must be moving in a cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow= head, head
        while fast and fast.next : # fast: for no node and fast.next for incr the fast two times
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                return True
        return False


# Java
"""
// method 4:
class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false; // If the list is empty or has only one element, there is no cycle
        }

        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) { // Ensure fast and fast.next are not null
            slow = slow.next; // Move slow by one step
            fast = fast.next.next; // Move fast by two steps
            if (slow == fast) { // If slow and fast meet, there is a cycle
                return true;
            }
        }
        return false; // If fast reaches the end, there is no cycle
    }
}
"""