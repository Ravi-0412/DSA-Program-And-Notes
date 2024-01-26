# using two stack 
# one stack(stack s) will do push,pop, top operations in O(1)
# other stack (min_stack) will give the min_ele in O(1)
# time: O(1), space: O(n)
class MinStack:
    def __init__(self):
        self.s=[]
        self.minEle=None
        self.min_stack= []
        
    def push(self, val: int) -> None: 
        self.s.append(val)  # we have to always push in stack 's' since it is doing normal operations only
        if not self.min_stack or val<=self.min_stack[-1]:   # ony push in min_stack when min_stack is empty or
                                                            # curr_ele is less than or equal to min_satck[-1]
                                                            # we are also pusing in case of equal ele because
                                                            # in case of repeating ele it will create problem(either wrong and or out of index)
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if not self.s:  
            return -1
        temp= self.s.pop()  # have always to return from normal stack only
        if temp== self.min_stack[-1]: # check if poped ele is min_ele 
                                      # if minimum then pop from min_stack
            self.min_stack.pop()
        return temp
        
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]  # min_stack will give the min_ele


# VVVI: without any extra space i.e other stack
# detailed solution in notes
class MinStack:
    def __init__(self):
        self.s=[]
        self.minEle=None
        
    def push(self, val: int) -> None:
        if not self.s: # if stack is empty
            self.s.append(val)
            self.min_ele= val
        elif val>= self.min_ele:
            self.s.append(val)
        else:  # val< self.min_ele
            modified_val= 2*val- self.min_ele
            self.s.append(modified_val)
            self.min_ele= val
    def pop(self) -> None:
        if not self.s:
            return -1
        elif self.s[-1]< self.min_ele:  # stack top is less than min_ele(unsual condition)
            temp= self.min_ele
            pre_min= 2*self.min_ele - self.s[-1]
            self.s.pop()
            self.min_ele= pre_min
            return temp
        # else:  self.s[-1]>= self.min_ele
        return self.s.pop()
        
    def top(self) -> int:
        if self.s[-1]>= self.min_ele:
            return self.s[-1]
        return self.min_ele   # if s[top] <min_ele (unusual condition)

    def getMin(self) -> int:
        if not self.s:
            return -1
        return self.min_ele 