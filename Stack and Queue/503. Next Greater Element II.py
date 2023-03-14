# just same logic we find the 'next Greater element on the Right".
# But if  next greater is not on the right side, you have to start finding from start before that index.
# here only for max ele ans will be '-1' and for remaining ele ans will be any ele from array.
# from this thinking we can get initution to solve the problem.

# so to find the ans for last ele, we will start comparing from start only till 'n-1.
# that's why append all these ele i.e from start to 'n-2' in the stack in reverse order since we will compare first with index '0' ele.
# after that apply the excatly same logic.

# logic: 
# Pick up the leaf node with minimum value.
# Combine it with its inorder neighbor which has smaller value between neighbors.
# Once we get the new generated non-leaf node, the node with minimum value is useless (For the new generated subtree will be represented with the largest leaf node value.)
# Repeat it until there is only one node.

# Note: Here we will have to find the greater ele in circluar form (right then to left till just before curr index).
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n= len(nums)
        stack, ans= [], []
        for i in range(n-2,-1,-1):  # appending the ele from 'n-2' to '0' in the reverse order.
            stack.append(nums[i])
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1]<= nums[i]:
                stack.pop()
            if not stack:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(nums[i])
        return ans[::-1]


# method 3:
# 2nd method only.
# Just find the next greater element in the array, on the left and one right.
# time= O(n)= space
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans= 0
        stack= [float('inf')]  # to handle the base case
        for num in arr:
            # when you get any greater ele from the stack top then keep on poping since smaller ele is already in stack so we have to use it first to minimise the ans.
            while stack[-1] <= num: 
                mid= stack.pop()    # this will be the one of the ele we will use as leaf and now we have to find the min ele to just left or just right of it.
                ans+= mid * min(stack[-1], num)    # stack[-1] will be on left side of mid and num will be on right side of mid and we have to take minimum of both.
            stack.append(num)   # every ele we have to append in stack
        # Now pop ele from stack till only 2 ele is left (one 'inf' one and one the greatest ele of the array)
        while len(stack) > 2:
            ans+= stack.pop() * stack[-1]   # minimum will be on top.
        return ans
