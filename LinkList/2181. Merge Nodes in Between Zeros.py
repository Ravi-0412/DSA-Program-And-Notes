class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = head
        pre, cur = dummy, head.next   # pre: pointer to pre value in answer
        while cur and cur.next :
            cur_sum = 0
            while cur.val != 0:
                cur_sum += cur.val
                cur = cur.next
            node = ListNode(cur_sum)
            pre.next = node
            pre = pre.next
            cur = cur.next
        return dummy.next


# Java
"""
class Solution {
    public ListNode mergeNodes(ListNode head) {
        ListNode dummy = head;
        ListNode pre = dummy;
        ListNode cur = head.next;
        while(cur != null && cur.next != null) {
            int curSum = 0 ;
            while(cur.val != 0) {
                curSum += cur.val;
                cur = cur.next;
            }
            ListNode node = new ListNode(curSum);
            pre.next = node;
            pre = pre.next;
            cur = cur.next;
        }
        return dummy.next;
    }
}
"""