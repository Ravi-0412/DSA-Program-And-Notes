# 1st q: Next greater right

def nextLargerElement(arr,n):
    stack= [] # will store the all the larger ele till index 'i'
              # no maximum then it will become empty
    ans= []
    # traverse the array from right to left
    for i in range(n-1,-1,-1):
        while(stack and stack[-1]<= arr[i]):
                stack.pop()
        if stack== []:  # since we are poping in above steps so we have to check for empty stack
                        # empty stack means either it is the largest ele or the last ele
            ans.append(-1)
            stack.append(arr[i])
        else:  # means stack top is greater than arr[i]
            ans.append(stack[-1])
            stack.append(arr[i])  # as arr[i] can be also the next greter ele for coming ele
    # now print the ans in reverse to get the ans
    for i in range(n-1,-1,-1):
        print(ans[i], end=" ")

arr= [0,1,8,3,2,4,6,7]
# nextLargerElement(arr,8)


# program for next greater left
# just same as next greater right
# all variations are same only just change the condition of while loop
# and direction of traversing the array

def nextGreaterLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack== []:
            ans.append(-1)
            stack.append(arr[i])
        else:
            ans.append(stack[-1])
            stack.append(arr[i])
    return ans
# arr= [0,1,8,3,2,4,6,7]
arr= [100, 80, 60, 70, 60, 75, 85]
print(nextGreaterLeft(arr))


# Next smaller left program
def nextSmallerLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack== []:
            ans.append(-1)
            stack.append(arr[i])
        else:
            ans.append(stack[-1])
            stack.append(arr[i])
    return ans
arr= [2,5,8,3,2,4,1,7]
# print(nextSmallerLeft(arr))



# other way:
# Traverse right to left.
# Here will store ans as index not actual value.

# next_smaller_left = [-1]*n
# stack2 = []
# for i in range(n-1, -1, -1):
#     while stack2 and a[stack2[-1]] > a[i]:
#         # means we got the next_smaller left  < for stack.pop(). 
#         ind = stack2.pop()
#         next_smaller_left[ind] = i
#     stack2.append(i)


# Next smaller right program
def nextSmallerRight(arr):
    stack= []
    ans= []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack== []:
            ans.append(-1)
            stack.append(arr[i])
        else:
            ans.append(stack[-1])
            stack.append(arr[i])
    result= ans[::-1]
    return result
arr= [2,5,8,3,2,4,1,7]
# print(nextSmallerRight(arr))


# other way:
# traverse left to right
# Here will store ans as index not actual value.

# next_smaller_right = [-1] * n
# stack1 = []
# for i in range(n):
#     while stack1 and a[stack1[-1]] > a[i]:
#         # means we got the next_smaller right  < for stack.pop().
#         ind = stack1.pop()
#         next_smaller_right[ind] = i
#     stack1.append(i)