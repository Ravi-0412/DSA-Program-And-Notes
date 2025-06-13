# Method 1:
# just similar as "2. Add Two numbers"

# Difference from  "2. Add Two numbers" ?
# Ans: Here MSB on left side and LSB on right side.
# We always start to add number from LSB, so we have to start from right side only.
# Just like normal sum because in this , our carry will automatically get adjusted to MSB.

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

# Method 2: 
# Without reversing the input
# Since we have start from right side so one data structure which can help is stack.
# so put all ele value of l1 and l2 in two different stack.
# Then we can apply the same logic as "2. Add Two numbers".
# But here we will reverse the direction of newNode since we have bring the 'LSB' first.
# time = space= O(n + m)

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


# Method 3: 
# very good approach. 
# optimising space complexity to O(1)
# time: O(n+m) , space: O(1)


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
// Java implementation for all three methods of Add Two Numbers

class Solution {

    // Reverse both lists, add them, then reverse the result
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Reverse the linklists to bring 'LSB' left side 
        ListNode Reversedl1 = reverseList(l1);
        ListNode Reversedl2 = reverseList(l2);

        // Now apply same logic as "2. Add Two Numbers"
        ListNode ans = new ListNode(0);
        ListNode cur = ans;
        int carry = 0;
        ListNode cur1 = Reversedl1, cur2 = Reversedl2;
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
        // Now reverse the ans and return 
        return reverseList(ans.next);
    }

    private ListNode reverseList(ListNode head) {
        if (head == null) return null;
        ListNode pre = null, cur = head;
        while (cur != null) {
            ListNode temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    // Method 2: 

    public ListNode addTwoNumbersWithStacks(ListNode l1, ListNode l2) {
        Stack<Integer> stackL1 = new Stack<>(); // will store the node val of l1
        Stack<Integer> stackL2 = new Stack<>(); // will store the node val of l2

        while (l1 != null) {
            stackL1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            stackL2.push(l2.val);
            l2 = l2.next;
        }

        ListNode ans = null; // head of ans. first time newNode will be point to null only
        int carry = 0;
        while (!stackL1.isEmpty() || !stackL2.isEmpty() || carry != 0) {
            int curSum = carry;
            if (!stackL1.isEmpty()) {
                curSum += stackL1.pop();
            }
            if (!stackL2.isEmpty()) {
                curSum += stackL2.pop();
            }
            // here changing the direction. LSB should go at last and MSB should come at first.
            // Just adding the new formed node to front to reverse the direction. same as we reverse the linklist.
            ListNode newNode = new ListNode(curSum % 10);
            newNode.next = ans;
            ans = newNode;
            carry = curSum / 10;
        }
        return ans;
    }

    // Method 3: 

    public ListNode addTwoNumbersWithLengthAlign(ListNode l1, ListNode l2) {
        int s1 = size(l1), s2 = size(l2);
        ListNode cur1 = l1, cur2 = l2;

        // make a linklist combine values(actual value, without carry) of both from left to right.
        ListNode res = null;
        while (s1 > 0 || s2 > 0) {
            int curSum = 0; // making the linklist from actual value 
            if (s1 >= s2) {
                curSum += cur1.val;
                cur1 = cur1.next;
                s1--;
            }
            if (s2 > s1) {
                // We will only add value at the same position and for this s2 > s1 .
                // This will handle both cases :
                // 1) in case if we have decremented 's1' above
                //    After that if s2 > s1 then s1 and s2 were equal so we will include element from both i.e
                //    We adding element at same position.
                // 2) Else s2 > s1 so we will include value at s2 only not s1.
                curSum += cur2.val;
                cur2 = cur2.next;
                s2--;
            }
            res = addToFront(curSum, res); // to reverse the direction just like above one
        }

        // now propagate the carry from LSB to MSB if value of node in above formed linklist is >= 10 and update the node value.
        // And we have to reverse the direction also since we have to return ans MSB-->LSB.
        ListNode cur = res;
        res = null;
        int carry = 0;
        while (cur != null || carry != 0) {
            int sumValue = carry;
            if (cur != null) {
                sumValue += cur.val;
                cur = cur.next;
            }
            int nodeValue = sumValue % 10;
            carry = sumValue / 10;
            res = addToFront(nodeValue, res);
        }
        return res;
    }

    private int size(ListNode node) {
        int n = 0;
        while (node != null) {
            n++;
            node = node.next;
        }
        return n;
    }

    private ListNode addToFront(int value, ListNode node) {
        ListNode newNode = new ListNode(value);
        newNode.next = node;
        return newNode;
    }
}

// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

"""

# C++ Code 
"""
// Method 1:
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        ListNode* pre = nullptr;
        ListNode* cur = head;
        while (cur) {
            ListNode* temp = cur->next;
            cur->next = pre;
            pre = cur;
            cur = temp;
        }
        return pre;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Reverse the linklists to bring 'LSB' left side
        ListNode* Reversedl1 = reverseList(l1);
        ListNode* Reversedl2 = reverseList(l2);

        // Now apply same logic as "2. Add Two Numbers"
        ListNode* ans = new ListNode(0);
        ListNode* cur = ans;
        int carry = 0;
        ListNode* cur1 = Reversedl1;
        ListNode* cur2 = Reversedl2;

        while (cur1 || cur2 || carry) {
            int curSum = carry;
            if (cur1) {
                curSum += cur1->val;
                cur1 = cur1->next;
            }
            if (cur2) {
                curSum += cur2->val;
                cur2 = cur2->next;
            }
            carry = curSum / 10;
            int sum = curSum % 10;
            cur->next = new ListNode(sum);
            cur = cur->next;
        }
        return reverseList(ans->next);
    }
};

// Method 2:
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stackL1, stackL2;

        // will store the node val of l1
        while (l1) {
            stackL1.push(l1->val);
            l1 = l1->next;
        }
        // will store the node val of l2
        while (l2) {
            stackL2.push(l2->val);
            l2 = l2->next;
        }

        ListNode* ans = nullptr;  // head of ans. first time newNode will point to None only
        int carry = 0;
        while (!stackL1.empty() || !stackL2.empty() || carry) {
            int curSum = carry;
            if (!stackL1.empty()) {
                curSum += stackL1.top(); stackL1.pop();
            }
            if (!stackL2.empty()) {
                curSum += stackL2.top(); stackL2.pop();
            }
            // here changing the direction. LSB should go at last and MSB should come at first.
            // Just adding the new formed node to front to reverse the direction. same as we reverse the linklist.
            ListNode* newNode = new ListNode(curSum % 10);
            newNode->next = ans;
            ans = newNode;
            carry = curSum / 10;
        }
        return ans;
    }
};

// Method 3:
class Solution {
public:
    int size(ListNode* cur) {
        int n = 0;
        while (cur) {
            n++;
            cur = cur->next;
        }
        return n;
    }

    ListNode* addToFront(int value, ListNode* node) {
        ListNode* newNode = new ListNode(value);
        newNode->next = node;
        return newNode;
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* cur1 = l1;
        ListNode* cur2 = l2;
        int s1 = size(cur1), s2 = size(cur2);

        // make a linklist combine values(actual value, without carry) of both from left to right.
        ListNode* res = nullptr;
        cur1 = l1;
        cur2 = l2;

        while (s1 || s2) {
            int curSum = 0;  // making the linklist from actual value
            if (s1 >= s2) {
                curSum += cur1->val;
                cur1 = cur1->next;
                s1--;
            }
            if (s2 > s1) {
                // We will only add value at the same position and for this s2 > s1 .
                // This will handle both cases : 
                // 1) in case if we have decremented 's1' above
                //    After that if s2 > s1 then s1 and s2 were equal so we will include element from both i.e
                //    We are adding element at same position.
                // 2) Else s2 > s1 so we will include value at s2 only not s1.
                curSum += cur2->val;
                cur2 = cur2->next;
                s2--;
            }
            res = addToFront(curSum, res);  // to reverse the direction just like above one
        }

        // now propagate the carry from LSB to MSB if value of node in above formed linklist is >= 10 and update the node value.
        // And we have to reverse the direction also since we have to return ans MSB-->LSB.
        ListNode* cur = res;
        res = nullptr;
        int carry = 0;

        while (cur || carry) {
            int sumValue = carry;
            if (cur) {
                sumValue += cur->val;
                cur = cur->next;
            }
            int nodeValue = sumValue % 10;
            carry = sumValue / 10;
            res = addToFront(nodeValue, res);
        }
        return res;
    }
};
"""

# Similar Q in array:
# 1) "66. Plus One".
# 2) 2816. Double a Number Represented as a Linked List
