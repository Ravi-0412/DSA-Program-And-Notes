# just we have to find the 'Next Greater ele on left'.
# for first ele ans== 1 as for default ans ==1.

# Here we need to store the index in stack.

# submitted on GFG
class Solution:
    def calculateSpan(self,a,n):
        stack, ans= [0], [1]   # initialsing with this to handle the base case for index==0
        for i in range(1,n):
            while stack and a[stack[-1]]<=a[i]:
                stack.pop()
            if not stack:  # means this ele is the greatest till now, so span= 'i+1'
                ans.append(i+1)
            else:  # means we have found an ele greater than curr ele in stack. so ans will be equal to 'i-stack[-1]'
                ans.append(i- stack[-1])
            stack.append(i)
        return ans
