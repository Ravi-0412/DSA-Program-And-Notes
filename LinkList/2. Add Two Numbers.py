# logic: Just we do the sum of two number given on paper.
# we keep on doing the sum either 1) first no has some ele remaining 2) second no has some ele remaining  3) carry is non zero
# here doing the same thing we are calculating the cursum of each position of l1 and l2, and adding with carry.

# Note: Here given LSB on left side, so we are calculating from left side only because in simple addition also we start from LSB only.
# We are exactly doing what we do in simple addition. we always start from LSB and go to MSB


# time: O(m+n)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur= ListNode(0)  # creating a dummy node to handle inserting at first
        carry= 0
        cur1, cur2 = l1, l2
        while cur1 or cur2 or carry:
            curSum = carry
            if cur1:
               curSum += cur1.val
               cur1= cur1.next
            if cur2:
                curSum += cur2.val
                cur2= cur2.next
            carry, sum= divmod(curSum,10)   # carry will equal to 'quotient' and 'sum' = 'remainder'
            cur.next= ListNode(sum)
            cur= cur.next
        return ans.next
    
# To read about divmod
# https://www.tutorialsteacher.com/python/divmod-method

# java
"""
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0); // creating a dummy node to handle inserting at first
        ListNode cur = ans;
        int carry = 0;
        ListNode cur1 = l1, cur2 = l2;
        while (cur1 != null || cur2 != null || carry != 0) {
            int curSum = carry;
            if (cur1 != null) {
                curSum += cur1.val;
                cur1 = cur1.next;
            }
            if (cur2 != null) {
                curSum += cur2.val;
                cur2 = cur2.next;
            }
            carry = curSum / 10;
            int sum = curSum % 10;
            cur.next = new ListNode(sum);
            cur = cur.next;
        }
        return ans.next;
    }
}
"""


