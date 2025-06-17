# method 1:

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


# Extension
# later do using one stack and without linklist