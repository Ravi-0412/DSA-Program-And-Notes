# 1st q: Next greater right
# Q: in case of no greater put '-1'.

# Logic: We need to check the element on right side for ans
# So we will start from right side only.

def nextLargerElement(arr,n):
    stack= [] # will store the all the larger ele till index 'i'
    ans= []
    for i in range(n-1,-1,-1):
        # Remove all element <= nums[i]
        while(stack and stack[-1] <= arr[i]):
                stack.pop()
        if stack:
            # Means we have found the ans for nums[i] and ans = top of stack
            ans.append(stack[-1])
        else:
            # Means i == n- 1 or nums[i] is the largest ele.
            ans.append(-1)
        stack.append(arr[i])  # arr[i] can be also the next greter ele for coming ele

    # now print the ans in reverse to get the ans
    for i in range(n-1,-1,-1):
        print(ans[i], end=" ")

arr= [0,1,8,3,2,4,6,7]
# nextLargerElement(arr,8)


# 2nd:  next greater left
# just same as next greater right

# Note vvi: All variations are same only just change the direction of 'for' loop and 
# condition of 'while' loop according to the question.

# Logic: We need to check the element on left side for ans
# So we will start from left side only.

def nextGreaterLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        # Remove all element <= nums[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    return ans
# arr= [0,1,8,3,2,4,6,7]
arr= [100, 80, 60, 70, 60, 75, 85]
print(nextGreaterLeft(arr))


# 3rd: Next smaller left program

def nextSmallerLeft(arr):
    stack= []
    ans= []
    for i in range(len(arr)):
        # Remove all element >= nums[i]
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
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
#     # 'i' will be ans for all the elements in stack till top of stack is > a[i].
#     while stack2 and a[stack2[-1]] > a[i]:
#         ind = stack2.pop()
#         next_smaller_left[ind] = i
#     stack2.append(i)


# 4th: Next smaller right program
def nextSmallerRight(arr):
    stack= []
    ans= []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack :
            ans.append(stack[-1])
        else:
            ans.append(-1)
        stack.append(arr[i])
    result= ans[::-1]
    return result
arr= [2,5,8,3,2,4,1,7]
# print(nextSmallerRight(arr))


# other way:
# traverse left to right
# Here will store index as ans not actual value.

# Same logic as method 3rd.

# next_smaller_right = [-1] * n
# stack1 = []
# for i in range(n):
#     while stack1 and a[stack1[-1]] > a[i]:
#         ind = stack1.pop()
#         next_smaller_right[ind] = i
#     stack1.append(i)