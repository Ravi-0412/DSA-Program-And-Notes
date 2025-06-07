
# time: o(n), space: o(n)
# logic: palindrome means identical from both side
# so just traverse the list two times
# while traversing for first time go on pushing the val on stack
# and while traversing for second time compare the val on stack
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first, second= head,head
        stack= []
        # traverse the whole list and put the data ele on stack
        while first:
            stack.append(first.val)
            first= first.next
            
        # now traverse again and keep comparing the currrent node val
        # with val on stack and keep on poping the ele from stack 
        # if matches till end(after this stack will become empty) 
        # means palindrome else not
        while second and (stack.pop()==second.val):
            second= second.next
        # now  if stack is empty(or second is pointing to None) 
        # means palindrome
        return stack==[]    # will return true if matches to the right side
                    # i.e if stack is empty then return true else return false


# concise way of writing 1st method
# Can store value in string also and compare at last.
class Solution:
    def isPalindrome(self, head):
        first= head
        stack= []
        # traverse the whole list and put the data ele on stack
        while first:
            stack.append(first.data)
            first= first.next
        return stack== stack[::-1]


# method 2: Time- o(n), space- o(1)

# NO need to make 'next' of last node of 1st part as None as this will get
# automatically handled in during comparion because of 'and' in while loop.

class Solution:
    def isPalindrome(self, head):
        # first find the middle element
        # in case of even no of elements, midddle one will be 
        # the next middle
        middle = self.middleNode(head)
        ReverseHead= self.reverseList(middle)
        
        # now compare both the 1st half and 2nd half
        return self.Compare(head,ReverseHead)
    
    def middleNode(self, head1):
        slow, fast= head1, head1
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        # after this slow will point to middle ele in case of odd no
        # of ele and second middle in case no of ele is even.
        return slow
    
    def reverseList(self, middle1):
        pre,current,first= None,middle1,middle1 
        while current:
            first= current.next  
            current.next= pre    
            pre= current        
            current= first      
        return pre
    
    def Compare(self,pre_head, after_head):
        first1, first2= pre_head, after_head
        while first1 != None and first2 != None:
            if first1.val!= first2.val:
                return False
            first1= first1.next
            first2= first2.next
        return True

# Java Code 
"""
//Method 1
import java.util.Stack;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode first = head;
        ListNode second = head;
        Stack<Integer> stk = new Stack<>();

        // Traverse the list and push values onto stack
        while (first != null) {
            stk.push(first.val);
            first = first.next;
        }

        // Compare elements with stack pop values
        while (second != null && stk.pop().equals(second.val)) {
            second = second.next;
        }

        // If stack is empty, return true (palindrome)
        return stk.isEmpty();
    }
}
//Method 2
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode middle = findMiddle(head);
        ListNode reverseHead = reverseList(middle);

        // Compare first half with reversed second half
        return compareLists(head, reverseHead);
    }

    private ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow; // Middle node
    }

    private ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head;

        while (curr != null) {
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;
        }

        return prev;
    }

    private boolean compareLists(ListNode first, ListNode second) {
        while (first != null && second != null) {
            if (first.val != second.val) {
                return false;
            }
            first = first.next;
            second = second.next;
        }
        return true;
    }
}

"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <stack>

using namespace std;

class ListNode {
public:
    int val;
    ListNode* next;

    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* first = head;
        ListNode* second = head;
        stack<int> stk;

        // Traverse the list and push values onto stack
        while (first) {
            stk.push(first->val);
            first = first->next;
        }

        // Compare elements with stack pop values
        while (second && stk.top() == second->val) {
            stk.pop();
            second = second->next;
        }

        // If stack is empty, return true (palindrome)
        return stk.empty();
    }
};
//Method 2
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* middle = findMiddle(head);
        ListNode* reverseHead = reverseList(middle);

        // Compare first half with reversed second half
        return compareLists(head, reverseHead);
    }

private:
    ListNode* findMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return slow; // Middle node
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            ListNode* nextNode = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextNode;
        }

        return prev;
    }

    bool compareLists(ListNode* first, ListNode* second) {
        while (first && second) {
            if (first->val != second->val) {
                return false;
            }
            first = first->next;
            second = second->next;
        }
        return true;
    }
};

"""