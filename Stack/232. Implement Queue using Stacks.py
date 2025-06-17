# Method 1: 

class MyQueue:
    
    def __init__(self):
        self.stack1= []
        self.stack2= []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:   # stack1 ka pop hmko queue ka phla(q me pop matlab phla ele) ele de.
        while len(self.stack1) > 1:  # moving ell ele except first one to stack2.
            temp= self.stack1.pop()
            self.stack2.append(temp)
        ans= self.stack1.pop()
        while self.stack2:  # again moving all ele from stack2 to stcak1
            temp= self.stack2.pop()
            self.stack1.append(temp)
        return ans
        

    def peek(self) -> int:  # stack ka top hmko queue ka phla ele de.
        while len(self.stack1) > 1:  # moving ell ele except first one to stack2.
            temp= self.stack1.pop()
            self.stack2.append(temp)
        ans= self.stack1[0]
        while self.stack2:   # again moving all ele from stack2 to stcak1
            temp= self.stack2.pop()
            self.stack1.append(temp)
        return ans

        

    def empty(self) -> bool:
        return (self.stack1== [] and self.stack2== [])
        

# Method 2: 
# optimising method 1
# Here no need to move el from stack2 to stack1.
# only need to move ele from stack1 to stack2 for ans when stack2 is empty.

# logic: once we have moved ele from stack1 to stack2 then already we can get ans for queue operation from stack2 directly as long as stcak2 is empty.
# for before every operation we are checking if ele is there in stack2 or not. if yes then we will get the ans directly otherwise we will need to move ele from stack1 to stack2.
# push: always in stack1

# note: no need to keep track of ele in stack2, we can directly check using len(stack2).

# time: average time for operation will be O(1).

class MyQueue:
    
    def __init__(self):
        self.stack1= []
        self.stack2= []
        self.eleInStack2= 0

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.eleInStack2 > 0:
            self.eleInStack2-= 1
            return self.stack2.pop()

        while len(self.stack1) > 1:
            temp= self.stack1.pop()
            self.stack2.append(temp)
            self.eleInStack2+= 1
        return self.stack1.pop()
        

    def peek(self):
        if self.eleInStack2 > 0:
            return self.stack2[-1]
            
        while len(self.stack1) :
            temp= self.stack1.pop()
            self.stack2.append(temp)
            self.eleInStack2+= 1
        return self.stack2[-1]

    def empty(self):
        return (self.stack1== [] and self.stack2== [])

# Java Code 
"""
//Method 1

import java.util.Stack;

class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void push(int x) {
        stack1.push(x);
    }

    public int pop() {
        while (stack1.size() > 1) { // Move all elements except the first one to stack2
            stack2.push(stack1.pop());
        }

        int ans = stack1.pop(); // Get the first element

        while (!stack2.isEmpty()) { // Move elements back to stack1
            stack1.push(stack2.pop());
        }

        return ans;
    }

    public int peek() {
        while (stack1.size() > 1) { // Move all elements except the first one to stack2
            stack2.push(stack1.pop());
        }

        int ans = stack1.peek(); // Peek the first element

        while (!stack2.isEmpty()) { // Move elements back to stack1
            stack1.push(stack2.pop());
        }

        return ans;
    }

    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}


//Method 2
import java.util.Stack;

class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    public void push(int x) {
        stack1.push(x);
    }

    public int pop() {
        if (!stack2.isEmpty()) {
            return stack2.pop();
        }

        while (!stack1.isEmpty()) { // Move elements from stack1 to stack2
            stack2.push(stack1.pop());
        }

        return stack2.pop();
    }

    public int peek() {
        if (!stack2.isEmpty()) {
            return stack2.peek();
        }

        while (!stack1.isEmpty()) { // Move elements from stack1 to stack2
            stack2.push(stack1.pop());
        }

        return stack2.peek();
    }

    public boolean empty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <stack>

using namespace std;

class MyQueue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    MyQueue() {}

    void push(int x) {
        stack1.push(x);
    }

    int pop() {
        while (stack1.size() > 1) { // Move all elements except the first one to stack2
            stack2.push(stack1.top());
            stack1.pop();
        }

        int ans = stack1.top(); // Get the first element
        stack1.pop();

        while (!stack2.empty()) { // Move elements back to stack1
            stack1.push(stack2.top());
            stack2.pop();
        }

        return ans;
    }

    int peek() {
        while (stack1.size() > 1) { // Move all elements except the first one to stack2
            stack2.push(stack1.top());
            stack1.pop();
        }

        int ans = stack1.top(); // Peek the first element

        while (!stack2.empty()) { // Move elements back to stack1
            stack1.push(stack2.top());
            stack2.pop();
        }

        return ans;
    }

    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};


//Method 2
#include <iostream>
#include <stack>

using namespace std;

class MyQueue {
private:
    stack<int> stack1;
    stack<int> stack2;

public:
    MyQueue() {}

    void push(int x) {
        stack1.push(x);
    }

    int pop() {
        if (!stack2.empty()) {
            int ans = stack2.top();
            stack2.pop();
            return ans;
        }

        while (!stack1.empty()) { // Move elements from stack1 to stack2
            stack2.push(stack1.top());
            stack1.pop();
        }

        int ans = stack2.top();
        stack2.pop();
        return ans;
    }

    int peek() {
        if (!stack2.empty()) {
            return stack2.top();
        }

        while (!stack1.empty()) { // Move elements from stack1 to stack2
            stack2.push(stack1.top());
            stack1.pop();
        }

        return stack2.top();
    }

    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};
"""


# Extension: 
# optimize for pop operation in O(1) time, didn't care about push's time complexity.
# This way , i have done in Q: "225.Implement stack using Queues"