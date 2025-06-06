# just similar as "2. Add Two numbers"

# Difference ?
# Ans: Here MSB on left side and LSB on right side.
# We always start to add number from LSB, so we have to start from right side only.
# Just like normal sum because in this , our carry will automatically get adjusted to MSB.

# Approach 1:
# Just reverse both the linklist then this Q get reduced to "2. Add Two numbers".

# Time: O(n + m)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(head):
            if not head:
                return None
            pre, cur= None, head
            while cur:
                temp= cur.next
                cur.next= pre
                pre, cur= cur, temp
            return pre
        # Reverse the linklists to bring 'LSB' left side 
        Reversedl1 , Reversedl2 = reverseList(l1) , reverseList(l2)
        # Now apply same logic as "2. Add Two Numbers"
        ans=cur= ListNode(0)
        carry= 0
        cur1, cur2 = Reversedl1, Reversedl2
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
        # Now reverse the ans and return 
        return reverseList(ans.next)

# Approach 2: Without reversing the input
# Since we have start from right side so one data structure which can help is stack.

# so put all ele value of l1 and l2 in two different stack.
# Then we can apply the same logic as "2. Add Two numbers".

# But here we will reverse the direction of newNode since we have bring the 'LSB' first.

# time= space= O(n + m)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stackL1= []   # will store the node val of l1
        stackL2= []   # will store the node val of l2
        while l1:
            stackL1.append(l1.val)
            l1= l1.next
        while l2:
            stackL2.append(l2.val)
            l2= l2.next
        
        ans= None  # head of ans. first time newNode will be point to None only
        carry= 0
        while stackL1 or stackL2 or carry:
            curSum= carry
            if stackL1:
                curSum+= stackL1.pop()
            if stackL2:
                curSum+= stackL2.pop()
            # here changing the direction. LSB should go at last and MSB should come at first.
            # Just adding the new formed node to front to reverse the direction. same as we reverse the linklist.
            newNode= ListNode(curSum % 10)
            newNode.next= ans
            ans= newNode
            carry= curSum //10
        return ans

# optimising space complexity to O(1)
# time: O(n+m) = space

# very good approach. 
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def size(cur):
            n= 0
            while cur:
                n+= 1
                cur= cur.next
            return n
        
        def addToFront(value, node):
            new= ListNode(value)
            new.next= node
            return new

        cur1, cur2= l1, l2
        s1, s2= size(cur1), size(cur2)

        # make a linklist combine values(actual value, without carry) of both from left to right.
        res= None
        cur1, cur2= l1, l2
        while s1 and s2:    # or while cur1 and cur2:
            curSum= 0   # making the linklist from actual value 
            if s1 >= s2:
                curSum+= cur1.val
                cur1= cur1.next
                s1-= 1
            if s2 > s1:  
                # We will only add value at the same position and for this s2 > s1 .
                #This will handle both cases : 1) in case if we have decremented 's1' above
                # After that if s2 > s1 then s1 and s2 were equal so we will include element from both i.e
                # We adding element at same position.
                # 2) Else s2 > s1 so we will include value at s2 only not s1.
                curSum+= cur2.val
                cur2= cur2.next
                s2-= 1
            res= addToFront(curSum, res)   # to reverse the direction just like above one

        # now propagate the carry from LSB to MSB if value of node in above formed linklist is >= 10 and update the node value.
        # And we have to reverse the direction also since we have to return ans MSB-->LSB.
        cur= res
        res, carry = None, 0
        while cur or carry:
            sumValue = carry
            if cur:
                sumValue += cur.val
                cur = cur.next
            carry, nodeValue= divmod(sumValue, 10)
            res = addToFront(nodeValue, res)
        return res

# Java Code 
"""
//Approach 1: Reverse Both Linked Lists
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode temp = cur.next;
            cur.next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode reversedL1 = reverseList(l1);
        ListNode reversedL2 = reverseList(l2);
        ListNode ans = new ListNode(0);
        ListNode cur = ans;
        int carry = 0;

        while (reversedL1 != null || reversedL2 != null || carry != 0) {
            int curSum = carry;
            if (reversedL1 != null) {
                curSum += reversedL1.val;
                reversedL1 = reversedL1.next;
            }
            if (reversedL2 != null) {
                curSum += reversedL2.val;
                reversedL2 = reversedL2.next;
            }
            carry = curSum / 10;
            cur.next = new ListNode(curSum % 10);
            cur = cur.next;
        }

        return reverseList(ans.next);
    }
}
//Approach 2: Using Stacks
import java.util.Stack;

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> stackL1 = new Stack<>();
        Stack<Integer> stackL2 = new Stack<>();

        while (l1 != null) {
            stackL1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            stackL2.push(l2.val);
            l2 = l2.next;
        }

        ListNode ans = null;
        int carry = 0;

        while (!stackL1.isEmpty() || !stackL2.isEmpty() || carry != 0) {
            int curSum = carry;
            if (!stackL1.isEmpty()) {
                curSum += stackL1.pop();
            }
            if (!stackL2.isEmpty()) {
                curSum += stackL2.pop();
            }
            ListNode newNode = new ListNode(curSum % 10);
            newNode.next = ans;
            ans = newNode;
            carry = curSum / 10;
        }

        return ans;
    }
}
"""

# C++ Code 
"""
//Approach 1: Reverse Both Linked Lists
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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* cur = head;
        while (cur) {
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        return prev;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* reversedL1 = reverseList(l1);
        ListNode* reversedL2 = reverseList(l2);
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        int carry = 0;

        while (reversedL1 || reversedL2 || carry) {
            int curSum = carry;
            if (reversedL1) {
                curSum += reversedL1->val;
                reversedL1 = reversedL1->next;
            }
            if (reversedL2) {
                curSum += reversedL2->val;
                reversedL2 = reversedL2->next;
            }
            carry = curSum / 10;
            cur->next = new ListNode(curSum % 10);
            cur = cur->next;
        }

        return reverseList(ans->next);
    }
};
//Approach 2: Using Stacks
#include <iostream>
#include <stack>

using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stackL1, stackL2;

        while (l1) {
            stackL1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            stackL2.push(l2->val);
            l2 = l2->next;
        }

        ListNode* ans = nullptr;
        int carry = 0;

        while (!stackL1.empty() || !stackL2.empty() || carry) {
            int curSum = carry;
            if (!stackL1.empty()) {
                curSum += stackL1.top();
                stackL1.pop();
            }
            if (!stackL2.empty()) {
                curSum += stackL2.top();
                stackL2.pop();
            }
            ListNode* newNode = new ListNode(curSum % 10);
            newNode->next = ans;
            ans = newNode;
            carry = curSum / 10;
        }

        return ans;
    }
};
"""

# Similar Q in array:
# 1) "66. Plus One".
# 2) 2816. Double a Number Represented as a Linked List
