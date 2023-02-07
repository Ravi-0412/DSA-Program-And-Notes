# done the same thing in ' Q no: 287.Find Duplictes'
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
                if slow== fast:
                    slow= head
                    while slow!= fast:
                        slow, fast= slow.next, fast.next
                    return slow
            print("no cycle")

# https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701055/JavaC%2B%2BPython-best-explanation-ever-happen's-for-this-problem   
# https://leetcode.com/problems/find-the-duplicate-number/solutions/650942/proof-of-floyds-cycle-detection-algorithm-find-the-duplicate-number/
    
    
    