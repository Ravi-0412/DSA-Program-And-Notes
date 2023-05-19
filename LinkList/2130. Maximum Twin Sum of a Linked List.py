# method 1: 
# logic: If we treat as array then we have to find the max of :
# 1st ele from start + 1st ele from last, 2nd ele from start + 2nd ele from last and so on.

# so 1st put all the nodes in an array and then find the max.
# time= sapce= O(n)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr= []
        curr= head
        while curr:
            arr.append(curr.val)
            curr= curr.next
        n= len(arr)
        ans= 0
        left, right= 0, n-1
        while left < right:
            ans= max(ans, arr[left] +  arr[right])
            left+= 1
            right-= 1
        return ans


# method 2:
# logic: just reverse the 2nd half of linklist and then find the max sum of any position of linklist like we add the linklist.

# time: O(n)
# space: O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # finding the middle(1st one)
        cur= head
        slow= fast= cur
        # if we want to find the 2nd: while fast and fast.next
        while fast and fast.next and fast.next.next:  
            slow, fast= slow.next, fast.next.next
        temp= slow.next  # node from where we have to reverse
        slow.next= None  # to make both equal in size otherwise middle node will be in both
                        # without this also will give correct ans only.
        # Reverse the other half of linklist i.e from slow.next to last.
        slow= temp  
        pre= None
        while slow:
            temp= slow.next
            slow.next= pre
            pre= slow
            slow= temp
        # now we have two linklist:
        #  1) head to just slow 2) from pre to last
        # first linklist will contain one extra node i.e 2nd middle will be in both the linklist
        ans= 0
        while pre:
            ans= max(ans, head.val + pre.val)
            pre, head= pre.next, head.next
        return ans
    

# same method as above
# finding the 2nd middle 
# here middle will be in both the linklist.

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # finding the middle(2nd one)
        cur= head
        slow= fast= cur
        while fast and fast.next:
            slow, fast= slow.next, fast.next.next
        # Reverse the other half of linklist i.e from slow to last.
        pre= None
        while slow:
            temp= slow.next
            slow.next= pre
            pre= slow
            slow= temp
        # now we have two linklist:
        #  1) head to just before slow 2) from pre to last
        ans= 0
        while pre:
            ans= max(ans, head.val + pre.val)
            pre, head= pre.next, head.next
        return ans
