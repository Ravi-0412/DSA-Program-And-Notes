# method 1: Since we have to reverse, so stack should come into mind
# just push the node into the stack and then start poping
#  and keep  updating the pointer

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None: return head
        stack= []
        curr= head
        while curr:
            stack.append(curr)
            curr= curr.next
        head= temp= stack.pop()
        while stack:
            temp.next= stack.pop()
            temp= temp.next
        # now temp will be pointing to the last node from reverse
        # so make temp.next= None
        temp.next= None
        return head
"""
# Java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return head;
        Stack<ListNode> stack = new Stack<>();
        ListNode curr = head;
        while (curr != null) {
            stack.push(curr);
            curr = curr.next;
        }
        head = stack.pop();
        ListNode temp = head;
        while (!stack.isEmpty()) {
            temp.next = stack.pop();
            temp = temp.next;
        }
        temp.next = null;
        return head;
    }
}

# C++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return head;
        stack<ListNode*> stk;
        ListNode* curr = head;
        while (curr != nullptr) {
            stk.push(curr);
            curr = curr->next;
        }
        head = stk.top();
        stk.pop();
        ListNode* temp = head;
        while (!stk.empty()) {
            temp->next = stk.top();
            stk.pop();
            temp = temp->next;
        }
        temp->next = nullptr;
        return head;
    }
};

Method 1 Analysis:
# Time Complexity: O(N) — traverse the list once
# Space Complexity: O(N) — stack holds all nodes
"""

# method 2: Iterative(submitted on leetcode)
"""
method 2: We'll reverse the list by changing the links directly
Start with two pointers: one for the previous node (pre = None) and one for the current node (curr = head)
As we move traverse the list, we keep flipping the pointers so that each node points to the one before it
Keep doing this till we reach the end of the list
In the end, pre will be pointing to the new head
"""
# time: o(n), space: o(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head 
        # current will point one step ahead of pre,
        # what ever node we will pass in function, it will reverse all node from that node till end
        pre,current= None,head 
        while current:  # if you will write 'while curr.next' it will not reverse the last node
            temp= current.next  # you need to store current.next somewhere so that after reversing current ele , current point to his next to reverse that also
            current.next= pre    # change the direction of current ele i.e point to the ele before it
            pre= current        # we have to store current somewhere so that next time reversed ele point to this or "pre must point to one position before curr"
            current= temp     # move current one step forward 
        return pre              # at last pre will point to the 1st node in reverse list
                                # and current and first will point to None
"""
# Java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null, current = head;
        while (current != null) {
            ListNode temp = current.next;
            current.next = pre;
            pre = current;
            current = temp;
        }
        return pre;
    }
}

# C++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre = nullptr, *current = head;
        while (current != nullptr) {
            ListNode* temp = current->next;
            current->next = pre;
            pre = current;
            current = temp;
        }
        return pre;
    }
};
Method 2 Analysis:
# Time Complexity: O(N) — traverse the list once
# Space Complexity: O(1) — only a few pointers used
"""

# Method 3: Iterative
"""
Create a dummy node before the head to make handling edge cases easier
We'll use three pointers:
  pre - the node right before the part we're reversing
  start - the first node in the part we're currently reversing
  then - the next node that needs to be moved to the front of the reversed section
Keep doing this until we've moved all nodes to the front
At the end, dummy.next will point to the new head of the reversed list
"""
# Do on pen and paper and understand.
# Understand this later properly.
    
# This method we can use in "92. Reverse Linked List II"  for concise code.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head== None: return head
        dummy= ListNode(0)  # will help to handle the case when we will reverse from head also
        dummy.next= head
        pre = dummy
        start = head   # starting node from which we have to reverse
        # Note: We won't change 'pre' and 'start' pointer. Will only change its 'next'.
        then = start.next  # node from which we will change the direction

        # 1 - 2 -3 - 4 - 5 ; ---> pre = dummy, start = 1, then = 2
        # dummy-> 1 -> 2 -> 3 -> 4 -> 5

        # 'pre.next'     will always point to the 1st node that we got after reversing till now.
        # 'start.next' : will point the node from which we have to reverse in next iteration

        cur = head
        # We are changing direction one step ahead of 'cur' so need to check 'cur.next' only not 'while cur:'
        while cur.next:   
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next  # will point the node from which we have to reverse in next iteration
        # first reversing : dummy->2 - 1 - 3 - 4 - 5;   pre = dummy, start = 1, then = 3  , 1st two node got reversed
        # second reversing: dummy->3 - 2 - 1 - 4 - 5;   pre = dummy, start = 1, then = 4    , 1st three node got reversed
        # third reversing:  dummy->4- 3 - 2 - 1 - 5;    pre = dummy, start = 1, then = 5   , 1st four node got reversed
        # fourth reversing: dummy->5- 4- 3 - 2 - 1;    pre = dummy, start = 1, then = None (finish)  , all nodes got reversed
        return dummy.next
"""
# Java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        ListNode start = head;
        ListNode then = start.next;
        
        while (then != null) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }
        
        return dummy.next;
    }
}

# C++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return head;
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* start = head;
        ListNode* then = start->next;
        
        while (then != nullptr) {
            start->next = then->next;
            then->next = pre->next;
            pre->next = then;
            then = start->next;
        }
        
        ListNode* newHead = dummy->next;
        delete dummy;
        return newHead;
    }
};

Method 3 Analysis:
# Time Complexity: O(N) — traverse the list once
# Space Complexity: O(1) — only a few pointers used
"""

# Method 3: By recursion
# just the conversion of above iterative into recursive.
"""
Use recursion to reverse the list starting from the head
Keep track of two pointers:
  pre - the part we've already reversed
  current - the part we still need to process
Recursively call the function, moving forward until current reaches the end
Then, as the calls return, flip the pointers so current.next points back to pre
In the end, return the new head once everything's reversed
"""
# Bottom up(like we do in Tree till we reach the leaf node or 'None' ).

# time: O(n), space: O(n)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        pre,curr= None, head
        return self.ReverseByRecursion(pre,curr)  # whatever you will pass as current, from current  it will reverse till last
    #  at last current will point to None and
    # pre will point to last node
    # so make head point to pre
    # now it will start reversing the pointer like: current.next= pre
    # will execute in backward direction till first call
    def ReverseByRecursion(self,pre, current):  
            if current== None:  # now we have to change the direction so make head point to pre as pre will be pointing to the last ele           
                self.head= pre   # using head of above function so using 'self'.                  
            else:
                self.ReverseByRecursion(current, current.next)  # this is breaking into small subproblem
                current.next= pre  
                # pre.next= None # no need of this as while traversing back link will get broken automatically 
            return self.head

"""
# Java
class Solution {
    private ListNode newHead;
    public ListNode reverseList(ListNode head) {
        newHead = null;
        return ReverseByRecursion(null, head);
    }
    private ListNode ReverseByRecursion(ListNode pre, ListNode current) {
        if (current == null) {
            newHead = pre;
        } else {
            ReverseByRecursion(current, current.next);
            current.next = pre;
        }
        return newHead;
    }
}

# C++
class Solution {
public:
    ListNode* newHead = nullptr;
    ListNode* reverseList(ListNode* head) {
        return ReverseByRecursion(nullptr, head);
    }
    ListNode* ReverseByRecursion(ListNode* pre, ListNode* current) {
        if (current == nullptr) {
            newHead = pre;
        } else {
            ReverseByRecursion(current, current->next);
            current->next = pre;
        }
        return newHead;
    }
};
Analysis:
# Time Complexity: O(N) — each node visited once
# Space Complexity: O(N) — recursive call stack
"""

# another way of writing the above code
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        pre,curr= None, head
        return self.ReverseByRecursion(pre, curr)
    def ReverseByRecursion(self,pre, curr):
        headreverse= None
        if curr== None:
            headreverse= pre
        else:
            # self.ReverseByRecursion(current,current.next)  # this will return none at last since we are 
                                                                    # not storing the updated value of 'headreverse' 
            headreverse = self.ReverseByRecursion(curr,curr.next)  # keep storing the result into headreverse
            curr.next= pre  
        return headreverse  # at last return head reverse


# method 4: using only one parameter
# Logic: After reaching base case 'that last node' should be head for reverse order.
# That reverse node should not change.
# Only change the pointer to reverse the direction and return the same 'reverseNode' always like above recursive methods.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:  # if there is no node or only one node. start reversing after you reach the last node
            return head
        reverseHead= self.reverseList(head.next)
        head.next.next= head  # reversing the link between next node and head.
        head.next= None  # this we have to write for the 1st node. other next will automatically become None
        return reverseHead
"""
# Java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        ListNode reverseHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return reverseHead;
    }
}

# C++
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return head;
        ListNode* reverseHead = reverseList(head->next);
        head->next->next = head;
        head->next = nullptr;
        return reverseHead;
    }
};
Method 4 Analysis:
# Time Complexity: O(N) — each node visited once
# Space Complexity: O(N) — recursion stack depth
"""

# Note vvi: Whenever you have comapare 1st and last ele , 
# do sum of 1st and last ele, append 1st to last ele , or any operation related to 1st and last ele.
# Must think of 'reversing linklist' and how we can get ans from reversing.

# Questions based on this:
# 234. Palindrome Linked List
# 61. Rotate List
# 2130. Maximum Twin Sum of a Linked List
# 143. Reorder List

# mistakes
# i got my mistake: for using a variable defined in other function, just put both the function inside a class and 
# make that variable a member variable using 'self.variable_name'
# for using a variable that is passed as parameter in other function inside a class. just call that variable using self
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre,curr= None, head
        return self.helper(pre,curr)
    def helper(self,pre,curr):
        if curr==None:
            head= pre   # if we write self.head then it's giving correct ans
        else:
            self.helper(curr,curr.next)  
            curr.next= pre
        return head    # if we write self.head then it's giving correct ans


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre,curr= None, head
        return self.helper(pre,curr)
    def helper(self,pre,curr):  
        if curr.next:    # for avoiding cycle, go till one step ahead like. while curr:           
            return self.helper(curr,curr.next)  # when you will write like this it will simply return,
            #  it will not process the below next statement so direction won't get changed
        curr.next= pre  # this will lead to cycle as pre is pointing to just one before curr 
        return curr

# tried changing the just above method
# this will only give the 1st ele as you are not storing the returned value anywhere, and returning the curr each time
# and at last curr will point to head only so it will only return the 1st element
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre,curr= None, head
        return self.helper(pre,curr)
    def helper(self,pre,curr):
        if curr.next:             
            self.helper(curr,curr.next)  # when you will write like this it will simply return,
            #  it will not process the below next statement so direction won't get changed
            if pre!=None:
                pre.next= None
            curr.next= pre
        return curr   



# Template for using in other questions:
def reverseList(self, head) :
        if not head: return head 
        pre,current= None,head 
        while current:  
            temp= current.next  
            current.next= pre    
            pre= current        
            current= temp     
        return pre              


# java
"""
// method 2:
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return head;
        ListNode pre = null, current = head;
        while (current != null) {
            ListNode temp = current.next;
            current.next = pre;
            pre = current;
            current = temp;
        }
        return pre;
    }
}

// method 3:
class Solution {
    private ListNode head;
    public ListNode reverseList(ListNode head) {
        this.head = head;
        ListNode pre = null, curr = head;
        return reverseByRecursion(pre, curr);
    }

    private ListNode reverseByRecursion(ListNode pre, ListNode curr) {
        if (curr == null) {
            this.head = pre;
        } else {
            reverseByRecursion(curr, curr.next);
            curr.next = pre;
        }
        return this.head;
    }
    }

// method 4:
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode reverseHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return reverseHead;
    }
}

"""