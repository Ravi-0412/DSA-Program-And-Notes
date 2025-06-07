# using two stack 
# one stack(stack s) will do push,pop, top operations in O(1)
# other stack (min_stack) will give the min_ele in O(1)

# Note: Methods pop, top and getMin operations will always be called on non-empty stacks.

# time: O(1), space: O(n)
class MinStack:
    def __init__(self):
        self.s=[]
        self.min_stack= []
        
    def push(self, val: int) -> None: 
        self.s.append(val)  # we have to always push in 's' because pop, and top will get from this only.
        # push in 'mim_stack' if val <= top of min_stack.
        # we are also pusing in case of equal ele because in case of repeating ele it will create problem(either wrong and or out of index)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        temp= self.s.pop()  # have always to return from normal stack only
        # check if poped ele is min_ele. if minimum then pop from min_stack
        if temp== self.min_stack[-1]:
            self.min_stack.pop()
        return temp
        
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]  # min_stack will give the min_ele

# Method 2: without any extra space i.e without using other stack.
# Logic: Implement stack using linklist where each node wil have three things:
# i) node val  ii) Minimum value till now iii) next node
# VVI: 1) Add the new element at start to get pop, top in O(1).
# 2)Store the minimum element at front only to get in O(1)

class Node:
    def __init__(self, val= None, minimum = None, next = None):
        self.value = val
        self.minimum = minimum
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        # add at front so we get get pop and top from head only
        if self.head == None:
            self.head = Node(val, val)
        else:
            # make new node as head and current head to its next.
            # first should store the minimum value till now
            self.head = Node(val, min(val, self.head.minimum), self.head)   

    def pop(self) -> None:
        temp = self.head.value
        self.head = self.head.next
        return temp

    def top(self) -> int:
        return self.head.value
    
    def getMin(self) -> int:
        return self.head.minimum

# later do using one stack and without linklist


# Java Code 
"""
//Method 1
import java.util.Stack;

class MinStack {
    private Stack<Integer> s;
    private Stack<Integer> minStack;

    public MinStack() {
        s = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        s.push(val);
        // Push in minStack if val <= top of minStack (to handle duplicate minimums)
        if (minStack.isEmpty() || val <= minStack.peek()) {
            minStack.push(val);
        }
    }

    public void pop() {
        int temp = s.pop();
        // If popped element is the minimum, remove it from minStack as well
        if (temp == minStack.peek()) {
            minStack.pop();
        }
    }

    public int top() {
        return s.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
//Method 2
class Node {
    int value;
    int minimum;
    Node next;

    public Node(int val, int min_val, Node nextNode) {
        this.value = val;
        this.minimum = min_val;
        this.next = nextNode;
    }
}

class MinStack {
    private Node head;

    public MinStack() {
        head = null;
    }

    public void push(int val) {
        // Add at the front to get pop and top operations in O(1)
        if (head == null) {
            head = new Node(val, val, null);
        } else {
            head = new Node(val, Math.min(val, head.minimum), head);
        }
    }

    public void pop() {
        if (head != null) {
            head = head.next;
        }
    }

    public int top() {
        return head != null ? head.value : -1; // Handle edge case
    }

    public int getMin() {
        return head != null ? head.minimum : -1; // Handle edge case
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <stack>

using namespace std;

class MinStack {
private:
    stack<int> s;
    stack<int> min_stack;

public:
    MinStack() {}

    void push(int val) {
        s.push(val);
        // Push in min_stack if val <= top of min_stack (to handle duplicate minimums)
        if (min_stack.empty() || val <= min_stack.top()) {
            min_stack.push(val);
        }
    }

    void pop() {
        int temp = s.top();
        s.pop();
        // If popped element is the minimum, remove it from min_stack as well
        if (temp == min_stack.top()) {
            min_stack.pop();
        }
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return min_stack.top();
    }
};
//Method 2
#include <iostream>

using namespace std;

class Node {
public:
    int value;
    int minimum;
    Node* next;

    Node(int val, int min_val, Node* nextNode) {
        value = val;
        minimum = min_val;
        next = nextNode;
    }
};

class MinStack {
private:
    Node* head;

public:
    MinStack() {
        head = nullptr;
    }

    void push(int val) {
        // Add at the front to get pop and top operations in O(1)
        if (!head) {
            head = new Node(val, val, nullptr);
        } else {
            head = new Node(val, min(val, head->minimum), head);
        }
    }

    void pop() {
        if (head) {
            head = head->next;
        }
    }

    int top() {
        return head ? head->value : -1; // Handle edge case
    }

    int getMin() {
        return head ? head->minimum : -1; // Handle edge case
    }
};
"""