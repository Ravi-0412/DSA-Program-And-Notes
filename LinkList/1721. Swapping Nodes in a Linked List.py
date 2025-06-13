# method 1: swapping the values(submitted on Leetcode)
# swapping type of q you can do by swapping the values but it's not a good method, good comapnies will not accept in interview
# not a good method.. Do by swapping nodes
"""
In this approach, we traverse the linked list to find the kth node from the beginning and the kth node from the end.
After the traversal, we swap the values of these two nodes.
"""
"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once to find the kth nodes.
Space Complexity: O(1), as we are not using any extra space for data structures.
"""

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        beg,end, curr=head,head,head
        # beg point to kth element from beg 
        # end point to kth element from end
        count= 0
        while curr.next:
            curr= curr.next
            count+= 1
            if count< k:
                beg= beg.next
            if count>= k:
                end= end.next
        beg.val, end.val= end.val, beg.val
        return head


# Method 2: 
# note: logic for changing node or swapping node- phla: ek dummy node lena h corner case ko dekhte huye
#  jis node ko attach karna h wahan pe pointer chahiye and jis node se attach akrna h wahan pe pointer chahiye
# ye tmko lana h and then uske bad pointer change kar dena h

# Note VVI: cycle se bachne ke liye ,node swap karte time ek direction wala sb link change karo then other direction se cycle na bane dekhte huye.

"""
Analysis:
Time Complexity: O(n), where n is the number of nodes in the linked list. We traverse the list once to find the kth nodes.
Space Complexity: O(1), as we are not using any extra space for data structures.
"""

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left= right= head  # i am sure that both left and right will go at least till head(1st ele). so initialise with that only
        # in case of pre_left and pre_right , these might not even go to 1st ele so initialise these with dummy
        dummy= ListNode(0)
        dummy.next= head
        pre_left= pre_right= dummy  # initialisng with dummy as if we initailse with None, it won't work for k=1
        # point left to kth ele from beg first
        for i in range(1,k):  # should run k-1 times to point 'left' to kth node from start
            pre_left= left
            left= left.next
        # now make right point to kth node from end
        null_checker= left
        while null_checker.next:
            null_checker= null_checker.next
            pre_right= right
            right= right.next
        if left== right:   # means if we have to swap the middle node in case of odd no of elements.. specially checking to avoid cycle. it will auto check for 
            return dummy.next
        pre_left.next, pre_right.next= right, left
        left.next, right.next= right.next, left.next
        return dummy.next


# if you want to write in sequence then you have to do like this as above directly swap simultaneously

# pre_left.next= right
# pre_right.next= left
# temp= left.next    # extra line 
# left.next= right.next
# right.next= temp
# return dummy.next


# Java
"""
// Method 1:
public class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode beg = head, end = head, curr = head;
        // beg points to kth element from beg 
        // end points to kth element from end
        int count = 0;

        while (curr.next != null) {
            curr = curr.next;
            count++;
            if (count < k) {
                beg = beg.next;
            }
            if (count >= k) {
                end = end.next;
            }
        }
        // swap values of beg and end
        int temp = beg.val;
        beg.val = end.val;
        end.val = temp;

        return head;
    }
}

// Method 2:
public class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode left = head, right = head;  // i am sure that both left and right will go at least till head(1st ele). so initialise with that only
        // in case of pre_left and pre_right , these might not even go to 1st ele so initialise these with dummy
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre_left = dummy, pre_right = dummy; // initialising with dummy as if we initialise with null, it won't work for k=1

        // point left to kth ele from beg first
        for (int i = 1; i < k; i++) { // should run k-1 times to point 'left' to kth node from start
            pre_left = left;
            left = left.next;
        }

        // now make right point to kth node from end
        ListNode null_checker = left;
        while (null_checker.next != null) {
            null_checker = null_checker.next;
            pre_right = right;
            right = right.next;
        }

        if (left == right) {  // means if we have to swap the middle node in case of odd no of elements.. specially checking to avoid cycle.
            return dummy.next;
        }

        // swapping nodes
        pre_left.next = right;
        pre_right.next = left;

        ListNode temp = left.next;
        left.next = right.next;
        right.next = temp;

        return dummy.next;
    }
}



"""

# C++
"""
// Method 1:
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* beg = head;
        ListNode* end = head;
        ListNode* curr = head;
        // beg points to kth element from beg 
        // end points to kth element from end
        int count = 0;

        while (curr->next) {
            curr = curr->next;
            count++;
            if (count < k) {
                beg = beg->next;
            }
            if (count >= k) {
                end = end->next;
            }
        }

        // swap values of beg and end
        int temp = beg->val;
        beg->val = end->val;
        end->val = temp;

        return head;
    }
};


// Method 2:
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* left = head;
        ListNode* right = head;  // i am sure that both left and right will go at least till head(1st ele). so initialise with that only

        ListNode dummy(0);
        dummy.next = head;
        ListNode* pre_left = &dummy;
        ListNode* pre_right = &dummy;  // initialising with dummy as if we initialise with nullptr, it won't work for k=1

        // point left to kth ele from beg first
        for (int i = 1; i < k; i++) {  // should run k-1 times to point 'left' to kth node from start
            pre_left = left;
            left = left->next;
        }

        // now make right point to kth node from end
        ListNode* null_checker = left;
        while (null_checker->next) {
            null_checker = null_checker->next;
            pre_right = right;
            right = right->next;
        }

        if (left == right) {  // means if we have to swap the middle node in case of odd no of elements.. specially checking to avoid cycle.
            return dummy.next;
        }

        // swapping nodes
        pre_left->next = right;
        pre_right->next = left;

        ListNode* temp = left->next;
        left->next = right->next;
        right->next = temp;

        return dummy.next;
    }
};



"""