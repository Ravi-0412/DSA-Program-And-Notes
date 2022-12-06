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

# 2nd method
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





# 3rd method : storing the address into the set
# why set came into mind: since we have to find cycle means same address can't repeat again while traversing and
# set only store the unique values
# time: o(n), space: o(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        # storing the address of visited node in the set
        # and if address is already present then loop otherwise not 
        s= set()
        while first:
            if first in s:
                return True 
            s.add(first)  # adding the add of fisrt into the set
            first= first.next
        return False
        

# 4th method(other student from leetcode)
# time: o(n), space= o(1)
# mark the traversing node as 'visited'
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'visited':
                return True
            head.val = 'visited'
            head = head.next
        return False


# 5th method: Floyd's cycle detection algorithm(submitted on GFG)
# time: o(n), space= o(1)
# logic: move the slow pointer one step ahead and 'fast' pointer 
# two steps ahead. And if there will be any cycle then at some time 
# slow== fast means there exist a cycle  since 'fast' was ahead of slow and again they meet means there must be moving in a cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow= head, head
        # while slow: # will generate error as in this case slow might not be None 
                    # but fast.next or fast.next.next may be null
        while fast and fast.next : # fast for no node and fast.next for incr the fast two times
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                return True
        return False



