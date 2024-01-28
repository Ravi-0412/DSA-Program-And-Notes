# Note: "You should preserve the original relative order of the nodes in each of the two partitions."
# this statement doesn't mean that we have to sort the list to get the ans.
# I.e if you sort then order of elements can change.

# Vvvi: meaning of above statement is that : 1) ele < 'x' should come before 'x' should be in 1st partition. 
# 2) ele >= x should be in 2nd partition  &&
# 3) order of ele should be preserved in both the partitions means both partition need not to be sorted but order should be maintained.


# Logic: Just store the ele < 'x' in one list and ele >= 'x' in other list.
# After that point last ele of list to 1st ele of 2nd list.

# Note vvi(my mistake): Make last pointer of both the list to "None" before updating the pointer otherwise there will be cycle
#Do this on paper to visualise.

# Time = space = O(n)

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 , dummy2= ListNode(0) , ListNode(0)
        cur1, cur2 = dummy1, dummy2
        cur = head
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur= cur.next
        # cur1.next, cur2.next = None, None   # make both None otherwise there will be cycle
        cur2.next = None    # only this will also work as 'cur1.next' is getting changed below.
        cur1.next = dummy2.next
        return dummy1.next
