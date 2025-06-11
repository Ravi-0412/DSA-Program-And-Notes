# just same method as merging in arrays
# made the dummy node to point to 1st ele of the result
# after that only we have to link the nodes based on condition

"""
We have a dummy node which gives a fixed starting point so we don't have to worry about edge cases for the head of the merged list.
Then we simply iterate through both lists, taking the smaller node each time and linking it to our result.
A temp pointer keeps track of the last node in our merged list, so we can keep building it smoothly as we go.
Once one of the lists completed, we just take whatever's left from the other list — since it's already sorted, we're good to go.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0)
        temp= dummy
        curr1= list1
        curr2= list2
        while curr1!=None and curr2!= None:
            if curr1.val>= curr2.val:
                temp.next= curr2
                temp= curr2
                curr2= curr2.next
            else:
                temp.next= curr1
                temp= curr1
                curr1= curr1.next
            temp = temp.next
        # Connect the node which is still remaining
        # if curr1!= None:
        #     temp.next= curr1
        # if curr2!= None:
        #     temp.next= curr2
        temp.next = curr1 or curr2  # shortcut
        return dummy.next
"""
# Java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode temp = dummy;
        ListNode curr1 = list1;
        ListNode curr2 = list2;

        while (curr1 != null && curr2 != null) {
            if (curr1.val >= curr2.val) {
                temp.next = curr2;
                temp = curr2;
                curr2 = curr2.next;
            } else {
                temp.next = curr1;
                temp = curr1;
                curr1 = curr1.next;
            }
            temp = temp.next;
        }

        temp.next = (curr1 != null) ? curr1 : curr2;
        return dummy.next;
    }
}

# C++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode(0);
        ListNode* temp = dummy;
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;

        while (curr1 != nullptr && curr2 != nullptr) {
            if (curr1->val >= curr2->val) {
                temp->next = curr2;
                temp = curr2;
                curr2 = curr2->next;
            } else {
                temp->next = curr1;
                temp = curr1;
                curr1 = curr1->next;
            }
            temp = temp->next;
        }

        temp->next = (curr1 != nullptr) ? curr1 : curr2;
        return dummy->next;
    }
};

Method 1 Analysis:
# Time Complexity: O(n + m) — each node from both lists is visited once.
# Space Complexity: O(1) — merging is done in-place using pointers only.
"""

# method 2: recursive way
"""
If either of the lists is empty, we return the other — because an empty list doesn't affect the result.
Then compare the head values of both lists.
If l1 has the smaller value, we link l1.next to the result of merging the rest of l1 and all of l2, and return l1 as the current node.
If l2 is smaller or equal, we do the same but with l2, and return l2 as the current node.
Now, the recursion will do it's work, merging the rest of the lists until we reach the base case where one of them is empty.
"""
# just conversion of above iterative method
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # base condition.. Both list can't be None at the same time
        # if l1 if None then return 'l2' and if 'l2' is None then return 'l1'. (This condition is short form of this meaning)
        if not l1 or not l2:   
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            # in this case starting node will be from 'l1' so return 'l1'
            return l1  
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            # in this case starting node will be from 'l1' so return 'l1'
            return l2
"""
class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // base condition.. Both list can't be null at the same time
        // if l1 is null then return 'l2' and if 'l2' is null then return 'l1'. (This condition is short form of this meaning)
        if (l1 == null || l2 == null) {
            return (l1 != null) ? l1 : l2;
        }

        if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            // in this case starting node will be from 'l1' so return 'l1'
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            // in this case starting node will be from 'l1' so return 'l1'
            return l2;
        }
    }
}

# C++
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        // base condition.. Both list can't be nullptr at the same time
        // if l1 is nullptr then return 'l2' and if 'l2' is nullptr then return 'l1'. (This condition is short form of this meaning)
        if (!l1 || !l2) {
            return l1 ? l1 : l2;
        }

        if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            // in this case starting node will be from 'l1' so return 'l1'
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            // in this case starting node will be from 'l1' so return 'l1'
            return l2;
        }
    }
};


Method 2 Analysis:
# Time Complexity: O(n + m) — each node from both lists is visited once.
# Space Complexity: O(n + m) — recursion stack, where n and m are the lengths of the two lists.
"""

# method 3: Recursive way but very much concise
# just the above logic only 

"""
Time and Space Complexity
Time Complexity: O(n + m)
Where n is the length of list1 and m is the length of list2. Each node is visited once.

Space Complexity:

Recursive call stack: O(n + m) in the worst case (due to recursion depth).

No extra data structures are used, so auxiliary space is O(1) apart from recursion stack.
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            # make sure whether list1 has minimum ele or not
            # i.e we can start from list1 or not
            # if not minimum then exchange the pointers
            # we were only exchanging the pointers(point to min) in all the above cases

            if list1.val> list2.val:
                # in iterative(exchanging temp) and in recursion above one exchanging the list pointer 
                # based on condition and exactly same here                       
                list1, list2= list2, list1                                                                                  
            list1.next= self.mergeTwoLists(list1.next,list2)  # now whichever list will have min ele will become 1st ele
        
        # if any of the list is None then return the list which is not 'None' at last 
        return list1 or list2                              


"""
# Java

class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 != null && list2 != null) {
            // make sure whether list1 has minimum ele or not
            // i.e we can start from list1 or not
            // if not minimum then exchange the pointers
            // we were only exchanging the pointers(point to min) in all the above cases

            if (list1.val > list2.val) {
                // in iterative(exchanging temp) and in recursion above one exchanging the list pointer 
                // based on condition and exactly same here
                ListNode temp = list1;
                list1 = list2;
                list2 = temp;
            }

            list1.next = mergeTwoLists(list1.next, list2); // now whichever list will have min ele will become 1st ele
        }

        // if any of the list is null then return the list which is not 'null' at last
        return (list1 != null) ? list1 : list2;
    }
}


# C++

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 && list2) {
            // make sure whether list1 has minimum ele or not
            // i.e we can start from list1 or not
            // if not minimum then exchange the pointers
            // we were only exchanging the pointers(point to min) in all the above cases

            if (list1->val > list2->val) {
                // in iterative(exchanging temp) and in recursion above one exchanging the list pointer 
                // based on condition and exactly same here
                std::swap(list1, list2);
            }

            list1->next = mergeTwoLists(list1->next, list2); // now whichever list will have min ele will become 1st ele
        }

        // if any of the list is nullptr then return the list which is not 'nullptr' at last
        return list1 ? list1 : list2;
    }
};

"""