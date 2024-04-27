# for each people check if he is celebrity or not.
# by comparing with other people.
# time: O(n^2)

def findCelebrity(n, knows):
    for i in range(n):
        isCelebrity= True    # initially 
        for j in range(n):
            if i==j:
                continue
            if knows(j, i)== False or knows(i, j)== True:
                isCelebrity= False
        if isCelebrity== True:
            return i
    return -1


# method 2:
# Note: very new concept and thought process. keep this concept into mind.
# Q: given 'n^2' relations(brute force one) find the ans in O(n).
# Algo:
# 1) put all 'n' people into stack.
# 2) pop two people and check which can't be the celebrity between two till len(stack)>=2.
# after comparing two we can surely say that one of them can't be celebrity.
# Put the people which can be celebrity in stack after comparing.
# By repeating this step, we will be left with only one people in stack.
# But surey we can't say that he will be the celebrity because we have not compared with many people.

# 3) for making sure whether the only left person in stack is celebrity or not.
# just check him with all people.
# if he is celebrity then return its id else return -1.

# Note: This method is based on like: if this happens then he can't be the ans and so on.

def findCelebrity(n, knows):
    stack= []
    for i in range(n):
        stack.append(i)
    while len(stack) >= 2:
        p1= stack.pop()
        p2= stack.pop()
        if knows(p2, p1): 
            # means p2 knows p1 -> p2 can't be celebrity but 'p1' can be celebrity so put 'p1' into stack
            stack.append(p1)
        else: 
            # means p2 doesn't knows p1 -> p1 can't be celebrity but 'p2' can be celebrity so put 'p2' into stack
            stack.append(p2)
    # now chekc the only person left in stack is celebrity or not.
    p= stack.pop()
    for i in range(n):
        if i==p:
            continue
        if knows(p, i) or not knows(i, p):   # then 'p' can't be celebrity
            return -1
    return p
