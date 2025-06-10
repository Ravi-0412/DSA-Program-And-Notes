# Note: kiske help se implement kar rhe h , uske operation se 'jisko' implement kar rhe uska operation ka ans
# milna chahiye.

# Yahan 'queue' ke help se 'stack' ko implement kar rhe isliye
# 'queue' ke operation se hmko stack ka ans milna chahiye for same operation.

# e.g: queue me agar pop kre tb 'stack' ka pop mile,
# queue me agar top element find kre tb 'stack' ka top mile.

# In similar way when we will implement 'queue' using stack.


# Method 1: Using Two queues
# Note: Here 'taking' variable like Q: "232. Implement Queue using Stacks" won't work
# because last added element should come first.

# time: all operation O(1) except push : O(n) but push on average will be O(1) only.

class MyStack:
    def __init__(self):
        self.q1= collections.deque([])   # we want to give ans for peek and pop from this queue.
        self.q2= collections.deque([])    

    def push(self, x: int) -> None:
        # remove all the elements from 'q1' and put into 'q2'.
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Now add current ele 'x' into 'q1' at front
        self.q1.append(x)
        # Now add remaining ele from 'q2' to 'q1' to maintain the order of 'top' and 'pop'
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0] 

    def empty(self) -> bool:
        return len(self.q1) == len(self.q2) == 0
    

# Method 2: Using One queue

# time: all operation O(1) except push : O(n).

class MyStack:
    def __init__(self):
        self.q= collections.deque([])  

    def push(self, x: int) -> None:
        self.q.append(x)
        # move all elements before the curr pushed to last, to bring the last pushed element at first
        # to get 'top' , 'pop' in O(1).
        for _ in range(len(self.q) -1):
            self.q.append(self.q.popleft()) 

    def pop(self) -> int:
        return self.q.popleft() if self.q else -1
        
    def top(self) -> int:
        return self.q[0] if self.q else -1
        
    def empty(self) -> bool:
        return len(self.q)== 0

# Java Code 
"""
//Method 1
import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    private Queue<Integer> q1; // This queue will be used for peek and pop operations
    private Queue<Integer> q2; // Temporary queue

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }

    public void push(int x) {
        while (!q1.isEmpty()) {
            q2.offer(q1.poll());
        }

        q1.offer(x);

        while (!q2.isEmpty()) {
            q1.offer(q2.poll());
        }
    }

    public int pop() {
        return q1.poll();
    }

    public int top() {
        return q1.peek();
    }

    public boolean empty() {
        return q1.isEmpty() && q2.isEmpty();
    }
}
//Method 2
import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    private Queue<Integer> q;

    public MyStack() {
        q = new LinkedList<>();
    }

    public void push(int x) {
        q.offer(x);
        // Move all elements before the current pushed element to last
        // This ensures the last pushed element is at the front
        for (int i = 0; i < q.size() - 1; i++) {
            q.offer(q.poll());
        }
    }

    public int pop() {
        return q.isEmpty() ? -1 : q.poll();
    }

    public int top() {
        return q.isEmpty() ? -1 : q.peek();
    }

    public boolean empty() {
        return q.isEmpty();
    }
}
"""

# C++ Code 
"""
//Method 1
#include <iostream>
#include <queue>

using namespace std;

class MyStack {
private:
    queue<int> q1; // This queue will be used for peek and pop operations
    queue<int> q2; // Temporary queue

public:
    MyStack() {}

    void push(int x) {
        // Move all elements from q1 to q2
        while (!q1.empty()) {
            q2.push(q1.front());
            q1.pop();
        }

        // Insert the current element at front
        q1.push(x);

        // Move all elements from q2 back to q1 to maintain order
        while (!q2.empty()) {
            q1.push(q2.front());
            q2.pop();
        }
    }

    int pop() {
        int temp = q1.front();
        q1.pop();
        return temp;
    }

    int top() {
        return q1.front();
    }

    bool empty() {
        return q1.empty() && q2.empty();
    }
};
//Method 2
#include <iostream>
#include <queue>

using namespace std;

class MyStack {
private:
    queue<int> q;

public:
    MyStack() {}

    void push(int x) {
        q.push(x);
        // Move all elements before the current pushed element to last
        // This ensures the last pushed element is at the front
        for (int i = 0; i < q.size() - 1; i++) {
            q.push(q.front());
            q.pop();
        }
    }

    int pop() {
        if (q.empty()) return -1;
        int temp = q.front();
        q.pop();
        return temp;
    }

    int top() {
        return q.empty() ? -1 : q.front();
    }

    bool empty() {
        return q.empty();
    }
};
"""
