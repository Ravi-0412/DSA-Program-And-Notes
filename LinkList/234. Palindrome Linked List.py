
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

"""
# Java
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode first = head, second = head;
        Stack<Integer> stack = new Stack<>();

        // traverse the whole list and put the data ele on stack
        while (first != null) {
            stack.push(first.val);
            first = first.next;
        }

        // now traverse again and keep comparing the currrent node val
        // with val on stack and keep on poping the ele from stack 
        // if matches till end(after this stack will become empty) 
        // means palindrome else not
        while (second != null && stack.pop() == second.val) {
            second = second.next;
        }

        // now  if stack is empty(or second is pointing to null) 
        // means palindrome
        return stack.isEmpty();  // will return true if matches to the right side
                                 // i.e if stack is empty then return true else return false
    }
}


# C++
#include <stack>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* first = head;
        ListNode* second = head;
        std::stack<int> stack;

        // traverse the whole list and put the data ele on stack
        while (first != nullptr) {
            stack.push(first->val);
            first = first->next;
        }

        // now traverse again and keep comparing the currrent node val
        // with val on stack and keep on poping the ele from stack 
        // if matches till end(after this stack will become empty) 
        // means palindrome else not
        while (second != nullptr && stack.top() == second->val) {
            stack.pop();
            second = second->next;
        }

        // now  if stack is empty(or second is pointing to nullptr) 
        // means palindrome
        return stack.empty();  // will return true if matches to the right side
                               // i.e if stack is empty then return true else return false
    }
};


# Method 1 Analysis:
# Time: O(N) — two passes through the list
# Space: O(N) — stack holds all node values
"""

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


# method 2: 
# Time- o(n), space- o(1)
"""
To check if the list is a palindrome:
First, find the middle using slow and fast pointers
Then, reverse the second half of the list right there (in-place)
Next, compare the nodes from the start and from the reversed second half one by one
we only use a constant amount of extra space (O(1))
"""
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

"""
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public boolean isPalindrome(ListNode head) {
        // first find the middle element
        // in case of even no of elements, midddle one will be 
        // the next middle
        ListNode middle = middleNode(head);
        ListNode reverseHead = reverseList(middle);

        // now compare both the 1st half and 2nd half
        return compare(head, reverseHead);
    }

    public ListNode middleNode(ListNode head1) {
        ListNode slow = head1, fast = head1;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        // after this slow will point to middle ele in case of odd no
        // of ele and second middle in case no of ele is even.
        return slow;
    }

    public ListNode reverseList(ListNode middle1) {
        ListNode pre = null, current = middle1, first = middle1;
        while (current != null) {
            first = current.next;
            current.next = pre;
            pre = current;
            current = first;
        }
        return pre;
    }

    public boolean compare(ListNode preHead, ListNode afterHead) {
        ListNode first1 = preHead, first2 = afterHead;
        while (first1 != null && first2 != null) {
            if (first1.val != first2.val) return false;
            first1 = first1.next;
            first2 = first2.next;
        }
        return true;
    }
}


# C++
#include <iostream>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // first find the middle element
        // in case of even no of elements, midddle one will be 
        // the next middle
        ListNode* middle = middleNode(head);
        ListNode* reverseHead = reverseList(middle);

        // now compare both the 1st half and 2nd half
        return compare(head, reverseHead);
    }

    ListNode* middleNode(ListNode* head1) {
        ListNode* slow = head1;
        ListNode* fast = head1;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        // after this slow will point to middle ele in case of odd no
        // of ele and second middle in case no of ele is even.
        return slow;
    }

    ListNode* reverseList(ListNode* middle1) {
        ListNode* pre = nullptr;
        ListNode* current = middle1;
        ListNode* first = middle1;
        while (current) {
            first = current->next;
            current->next = pre;
            pre = current;
            current = first;
        }
        return pre;
    }

    bool compare(ListNode* preHead, ListNode* afterHead) {
        ListNode* first1 = preHead;
        ListNode* first2 = afterHead;
        while (first1 != nullptr && first2 != nullptr) {
            if (first1->val != first2->val) return false;
            first1 = first1->next;
            first2 = first2->next;
        }
        return true;
    }
};


"""
