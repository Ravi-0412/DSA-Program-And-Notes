# Method 1:
# just traverse the 1st linklist and store its address in hashmap with val =1(just any value)
# after that traverse the other linklist and check whether that node was in hashmap1
# it basically checking the address of the node, if equal then intesection point exist at that node
# other don't exist

"""
Method 1 analysis:
Time Complexity: O(m+n) where m and n are the lengths of the two linked lists.
Space Complexity: O(m) where m is the length of the first linked list (to store addresses in hashmap).
"""

def getIntersectionNode(self, headA, headB) ->:
        curr1,curr2,hashmap1= headA, headB,{}
        while curr1:
            hashmap1[curr1]= 1
            curr1= curr1.next
        while curr2:
            if curr2 in hashmap1: 
                return curr2
            curr2= curr2.next
        return None

# Method 2:
# find the diff in the length of linked list
# now move the linklist with greater length equal to the len_diff 
# now start moving the both linked list simultaneously and keep checking
# whether they point to the same Node
# if no common point exist then intersection point doesn't exist
# basically comapring the address of the nodes
# time: O(m+n), space: O(1)

class Solution:
    def getIntersectionNode(self, headA, headB):
        curr1,curr2, length1,length2= headA, headB, 0,0
        # find length of linklist1
        while curr1:
            length1,curr1= length1+ 1, curr1.next
        # find length of linklist2
        while curr2:
            length2,curr2= length2+ 1, curr2.next
        # find the diff and according call the function
        if length1>length2:
            d= length1-length2
            return self.IntersectionNode(d,headA,headB)  
        else:
            d= length2-length1
            return self.IntersectionNode(d,headB, headA)
    
    def IntersectionNode(self,d,head1,head2):
        curr1,curr2= head1,head2
        for i in range(d):
            curr1= curr1.next
        while curr1 and curr2:
            if curr1== curr2:  # if linklist from curr1 and curr2 is same
                               # in python all variable address will same if they point to the same data
                               # e.g:
                                    # a= 5
                                    # x=y=a
                                    # print(id(x),id(y))  # addres of both x and y will be same
                # print(id(curr1),id(curr2))  # here address of both will be same as they will be pointing to the same data like above
                return curr1
            curr1,curr2= curr1.next, curr2.next
        return None

"""
# Method 3:
# Using two pointers technique
# We can use two pointers to find the intersection point.
# We will traverse both linked lists simultaneously, and when we reach the end of one list, we will switch to the other list.
# This way, both pointers will traverse the same number of nodes, and they will meet at the intersection point if it exists.

"""
class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        curr1, curr2 = headA, headB
        
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
            
        return curr1

# Method 3 analysis:
# Time Complexity: O(m+n) where m and n are the lengths of the two linked lists.
# Space Complexity: O(1) as we are not using any extra space.
# Note: This method works because if there is an intersection, both pointers will eventually meet at the intersection point.


# Java
// Method 2: 
"""
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode curr1 = headA, curr2 = headB;
        int length1 = 0, length2 = 0;
        // find length of linklist1
        while (curr1 != null) {
            length1++;
            curr1 = curr1.next;
        }
        // find length of linklist2
        while (curr2 != null) {
            length2++;
            curr2 = curr2.next;
        }
        // find the diff and according call the function
        if (length1 > length2) {
            int d = length1 - length2;
            return IntersectionNode(d, headA, headB);
        } else {
            int d = length2 - length1;
            return IntersectionNode(d, headB, headA);
        }
    }

    public ListNode IntersectionNode(int d, ListNode head1, ListNode head2) {
        ListNode curr1 = head1, curr2 = head2;
        for (int i = 0; i < d; i++) {
            curr1 = curr1.next;
        }
        while (curr1 != null && curr2 != null) {
            if (curr1 == curr2) {  // if linklist from curr1 and curr2 is same
                                   // in java all variable address will same if they point to the same data
                                   // e.g:
                                        // Integer a = 5;
                                        // Integer x = a, y = a;
                                        // System.out.println(System.identityHashCode(x) + " " + System.identityHashCode(y));
                                        // address of both x and y will be same
                // System.out.println(System.identityHashCode(curr1) + " " + System.identityHashCode(curr2));
                // here address of both will be same as they will be pointing to the same data like above
                return curr1;
            }
            curr1 = curr1.next;
            curr2 = curr2.next;
        }
        return null;
    }
}

"""

# C++ 
"""
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curr1 = headA;
        ListNode* curr2 = headB;
        int length1 = 0, length2 = 0;
        // find length of linklist1
        while (curr1) {
            length1++;
            curr1 = curr1->next;
        }
        // find length of linklist2
        while (curr2) {
            length2++;
            curr2 = curr2->next;
        }
        // find the diff and according call the function
        if (length1 > length2) {
            int d = length1 - length2;
            return IntersectionNode(d, headA, headB);
        } else {
            int d = length2 - length1;
            return IntersectionNode(d, headB, headA);
        }
    }

    ListNode* IntersectionNode(int d, ListNode* head1, ListNode* head2) {
        ListNode* curr1 = head1;
        ListNode* curr2 = head2;
        for (int i = 0; i < d; i++) {
            curr1 = curr1->next;
        }
        while (curr1 && curr2) {
            if (curr1 == curr2) {  // if linklist from curr1 and curr2 is same
                                   // in C++ all variable address will same if they point to the same data
                                   // e.g:
                                        // int a = 5;
                                        // int* x = &a;
                                        // int* y = &a;
                                        // cout << x << " " << y;  // address of both x and y will be same
                // cout << curr1 << " " << curr2;
                // here address of both will be same as they will be pointing to the same data like above
                return curr1;
            }
            curr1 = curr1->next;
            curr2 = curr2->next;
        }
        return nullptr;
    }
};

"""