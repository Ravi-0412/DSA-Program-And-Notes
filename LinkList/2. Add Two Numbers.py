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

# Java Code 
"""
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ans = new ListNode(0); // Creating a dummy node
        ListNode cur = ans;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int curSum = carry;
            if (l1 != null) {
                curSum += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                curSum += l2.val;
                l2 = l2.next;
            }
            carry = curSum / 10;
            cur.next = new ListNode(curSum % 10);
            cur = cur.next;
        }

        return ans.next;
    }
}
"""

# C++ Code 
"""
#include <iostream>

using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;
    
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode(0); // Creating a dummy node
        ListNode* cur = ans;
        int carry = 0;

        while (l1 || l2 || carry) {
            int curSum = carry;
            if (l1) {
                curSum += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                curSum += l2->val;
                l2 = l2->next;
            }
            carry = curSum / 10;
            cur->next = new ListNode(curSum % 10);
            cur = cur->next;
        }

        return ans->next;
    }
};
"""


