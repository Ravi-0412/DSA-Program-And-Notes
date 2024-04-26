# just same logic we find the 'next Greater element on the Right".
# But if  next greater is not on the right side, you have to start finding from start till that index.
# here only for max ele ans will be '-1' and for remaining ele ans will be any ele from array.
# from this thinking we can get initution to solve the problem.

# so to find the ans for last ele, we will start comparing from start only till 'n-2'.
# that's why append all these ele i.e from start to 'n-2' in the stack in reverse order since we will compare first with index '0' ele.
# after that apply the excatly same logic.

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


# method 2:
# Logic: Loop once, we can get the Next Greater Number of a normal array.
# Loop twice, we can get the Next Greater Number of a circular array.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2*n):
            num = nums[i % n]    # '%' will help in 2nd traversal.
            while stack and nums[stack[-1]] < num:
                ans[stack.pop()] = num
            stack.append(i % n)
        return ans