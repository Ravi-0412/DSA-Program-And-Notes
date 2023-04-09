# done the same thing in ' Q no: 287.Find Duplicates'
# time: 0(n), space: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow,fast= head, head
            cycle= False  # this will check whether there exist cycle or not 
            # first check whether cycle exist or not 
            while fast and fast.next:
                slow, fast= slow.next, fast.next.next
                if slow== fast:
                    cycle= True
                    break
            if cycle== False:
                print("no cycle")
                return
            # if cycle exist now find the starting point
            slow1= head
            while slow1!= slow:
                slow1, slow= slow1.next, slow.next
            return slow


# concise way and doing in only one loop above logic
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow,fast= head, head 
            while fast and fast.next:
                slow, fast= slow.next, fast.next.next
                if slow== fast: # we have found the cycle , now check the node.
                    slow= head
                    while slow!= fast:
                        slow, fast= slow.next, fast.next
                    return slow
            print("no cycle")


    
    
    