# method 1: swapping the values(submitted on Leetcode)
# swapping type of q you can do by swapping the values but it's not a good method, good comapnies will not accept in interview
# not a good method.. Do by swapping nodes
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

# note: logic for changing node or swapping node- phla: ek dummy node lena h corner case ko dekhte huye
#  jis node ko attach karna h wahan pe pointer chahiye and jis node se attach akrna h wahan pe pointer chahiye
# ye tmko lana h and then uske bad pointer change kar dena h

# Note VVI: cycle se bachne ke liye ,node swap karte time ek direction wala sb link change karo then other direction se cycle na bane dekhte huye.

# 2nd method : found from submissions
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1054370/Python-3-or-Swapping-NODES-or-Swapping-Values-or-One-Pass-or-Fully-explained
# very good one
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

# Java Code 
"""
//Method 1
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode beg = head, end = head, curr = head;
        int count = 0;

        // Traverse and identify kth node from beginning and end
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

        // Swap values of kth nodes
        int temp = beg.val;
        beg.val = end.val;
        end.val = temp;

        return head;
    }
}
//Method 2
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        ListNode left = head, right = head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode preLeft = dummy, preRight = dummy;

        // Point left to kth node from start
        for (int i = 1; i < k; i++) {
            preLeft = left;
            left = left.next;
        }

        // Point right to kth node from end
        ListNode nullChecker = left;
        while (nullChecker.next != null) {
            nullChecker = nullChecker.next;
            preRight = right;
            right = right.next;
        }

        // Avoid swapping the same node
        if (left == right) return dummy.next;

        // Swap nodes by changing pointers
        preLeft.next = right;
        preRight.next = left;
        ListNode temp = left.next;
        left.next = right.next;
        right.next = temp;

        return dummy.next;
    }
}
"""

# C++ Code 
"""
//Method 1
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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* beg = head;
        ListNode* end = head;
        ListNode* curr = head;
        int count = 0;

        // Traverse and identify kth node from beginning and end
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

        // Swap values of kth nodes
        swap(beg->val, end->val);
        return head;
    }
};
//Method 2
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* left = head;
        ListNode* right = head;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre_left = dummy;
        ListNode* pre_right = dummy;

        // Point left to kth node from start
        for (int i = 1; i < k; i++) {
            pre_left = left;
            left = left->next;
        }

        // Point right to kth node from end
        ListNode* null_checker = left;
        while (null_checker->next) {
            null_checker = null_checker->next;
            pre_right = right;
            right = right->next;
        }

        // Avoid swapping the same node
        if (left == right) return dummy->next;

        // Swap nodes by changing pointers
        pre_left->next = right;
        pre_right->next = left;
        swap(left->next, right->next);

        return dummy->next;
    }
};
"""
