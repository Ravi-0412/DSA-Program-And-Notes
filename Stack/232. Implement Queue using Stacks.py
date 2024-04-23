# 'pop' and 'peek' will tell 

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
        


# optimising the above solution
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


# Try this also.

# optimize for pop operation in O(1) time, didn't care about push's time complexity.
# This way , i have done in Q: "225.Implement stack using Queues"