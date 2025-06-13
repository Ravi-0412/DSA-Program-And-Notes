# Method 1:
# just traverse the 1st linklist and store its address in hashmap or a set with val =1(just any value)
# after that traverse the other linklist and check whether that node was in hashmap1
# it basically checking the address of the node, if equal then intesection point exist at that node
# other don't exist

"""
Analysis:
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

Analysis:
# Time Complexity: O(m+n) where m and n are the lengths of the two linked lists.
# Space Complexity: O(1) as we are not using any extra space.
# Note: This method works because if there is an intersection, both pointers will eventually meet at the intersection point.

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


# Java
"""
// Method 1:
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        HashSet<ListNode> set = new HashSet<>();
        ListNode curr1 = headA, curr2 = headB;

        // Store all nodes from headA in a set
        while (curr1 != null) {
            set.add(curr1);
            curr1 = curr1.next;
        }

        // Traverse list B and check if any node is in the set
        while (curr2 != null) {
            if (set.contains(curr2)) {
                return curr2;
            }
            curr2 = curr2.next;
        }

        return null;
    }
}


// Method 2:
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode curr1 = headA, curr2 = headB;
        int length1 = 0, length2 = 0;

        // Find length of list1
        while (curr1 != null) {
            length1++;
            curr1 = curr1.next;
        }

        // Find length of list2
        while (curr2 != null) {
            length2++;
            curr2 = curr2.next;
        }

        // Find the difference and call the helper function
        if (length1 > length2) {
            return findIntersection(length1 - length2, headA, headB);
        } else {
            return findIntersection(length2 - length1, headB, headA);
        }
    }

    public ListNode findIntersection(int d, ListNode head1, ListNode head2) {
        ListNode curr1 = head1, curr2 = head2;

        // Move the pointer of the longer list by 'd' steps
        for (int i = 0; i < d; i++) {
            curr1 = curr1.next;
        }

        // Traverse both together and find the first common node
        while (curr1 != null && curr2 != null) {
            if (curr1 == curr2) return curr1;
            curr1 = curr1.next;
            curr2 = curr2.next;
        }

        return null;
    }
}


// Method 3:
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) return null;

        ListNode curr1 = headA, curr2 = headB;

        // When one reaches the end, redirect to the other list's head
        while (curr1 != curr2) {
            curr1 = (curr1 != null) ? curr1.next : headB;
            curr2 = (curr2 != null) ? curr2.next : headA;
        }

        return curr1;
    }
}


"""


# C++
"""
// Method 1:
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*> visited;
        ListNode* curr1 = headA;
        ListNode* curr2 = headB;

        // Store all nodes from headA in a set
        while (curr1) {
            visited.insert(curr1);
            curr1 = curr1->next;
        }

        // Traverse list B and check if any node is in the set
        while (curr2) {
            if (visited.count(curr2)) {
                return curr2;
            }
            curr2 = curr2->next;
        }

        return nullptr;
    }
};


// Method 2:
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curr1 = headA;
        ListNode* curr2 = headB;
        int length1 = 0, length2 = 0;

        // Find length of list1
        while (curr1) {
            length1++;
            curr1 = curr1->next;
        }

        // Find length of list2
        while (curr2) {
            length2++;
            curr2 = curr2->next;
        }

        // Find the difference and call the helper function
        if (length1 > length2) {
            return findIntersection(length1 - length2, headA, headB);
        } else {
            return findIntersection(length2 - length1, headB, headA);
        }
    }

    ListNode* findIntersection(int d, ListNode* head1, ListNode* head2) {
        ListNode* curr1 = head1;
        ListNode* curr2 = head2;

        // Move the pointer of the longer list by 'd' steps
        for (int i = 0; i < d; i++) {
            curr1 = curr1->next;
        }

        // Traverse both together and find the first common node
        while (curr1 && curr2) {
            if (curr1 == curr2) return curr1;
            curr1 = curr1->next;
            curr2 = curr2->next;
        }

        return nullptr;
    }
};
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode* curr1 = headA;
        ListNode* curr2 = headB;
        int length1 = 0, length2 = 0;

        // Find length of list1
        while (curr1) {
            length1++;
            curr1 = curr1->next;
        }

        // Find length of list2
        while (curr2) {
            length2++;
            curr2 = curr2->next;
        }

        // Find the difference and call the helper function
        if (length1 > length2) {
            return findIntersection(length1 - length2, headA, headB);
        } else {
            return findIntersection(length2 - length1, headB, headA);
        }
    }

    ListNode* findIntersection(int d, ListNode* head1, ListNode* head2) {
        ListNode* curr1 = head1;
        ListNode* curr2 = head2;

        // Move the pointer of the longer list by 'd' steps
        for (int i = 0; i < d; i++) {
            curr1 = curr1->next;
        }

        // Traverse both together and find the first common node
        while (curr1 && curr2) {
            if (curr1 == curr2) return curr1;
            curr1 = curr1->next;
            curr2 = curr2->next;
        }

        return nullptr;
    }
};


// Method 3:
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return nullptr;

        ListNode* curr1 = headA;
        ListNode* curr2 = headB;

        // When one reaches the end, redirect to the other list's head
        while (curr1 != curr2) {
            curr1 = (curr1 != nullptr) ? curr1->next : headB;
            curr2 = (curr2 != nullptr) ? curr2->next : headA;
        }

        return curr1;
    }
};

"""