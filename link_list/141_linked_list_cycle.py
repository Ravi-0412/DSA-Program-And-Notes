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
                break
            else:
                first= first.next
                length+= 1
        if(length<10001):
            return False


# 2nd method: using dictionary to store the address of visiting node
# and if again we find the same address of any node means there is cycle otherwise not
# but not working 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        hashmap= {}
        while first:
            if id(first) not in hashmap: # error in this line 
                hashmap[first.val]= id(first) # error in this line
                first= first.next
            else:
                return True
                break
        if first== None:
            return False

# correct code of method 2
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mem = {}
        temp = head
        # traverse the link list and when you see any node
        # for 1st time then store 'True' at the address of that node
        # and if that adress is alreay present then return true
        while temp:
            if temp in mem: return True  # means we are visiting that address 
                                          # again means there is a loop
            else: mem[temp]= True # at address of temp, making the value =True
            temp = temp.next
        return False



# 3rd method : storing the address into the set
# time: o(n^2), space: o(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first= head
        # storing the address of visited node in the set
        # and if address is already present then loop otherwise not 
        s= set()
        while first:
            if first in s:
                return True 
                break
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
# slow== fast means there exist a cycle
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        fast, slow= head, head
        # while slow: # will generate error as in this case slow might not be None 
                    # but fast.next or fast.next.next may be null
        while fast.next and fast.next.next and slow:
            slow= slow.next
            fast= fast.next.next
            if slow== fast:
                return True
                break
        return False



