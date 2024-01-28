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

# Time = O(n)
# Space = O(1)

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow= fast= head
        while fast and fast.next:
            slow, fast= slow.next, fast.next.next
        # Reverse the other half of linklist i.e from slow to last.
        pre = None # will store the head after reversing 2nd half
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
        
