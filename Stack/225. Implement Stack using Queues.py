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

