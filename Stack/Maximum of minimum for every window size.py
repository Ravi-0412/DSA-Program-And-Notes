# Brute force:
# check for each possible length.
# Time: O(n^3)

# can see gfg code


# method 2: Optimisation using stack

# Similar to q :"84. Largest Rectangle in Histogram".

# Logic: For every element find the range(length) in which it can be maxiumum.
# and any element can be minimum on it's left or right side until we don't find any smaller ele than this ele.
# 1) first find the nextsmallerLeft and nextSmallerRight for each ele
# 2) then calculate the length in which each element can be minimum.
# length = nextSmallerRight[i] - nextsmallerLeft[i] - 1

# 3) Now update the ans by traversing array again for each length by taking maximum
# value of element that can contribute for that much length.
# ans[length - 1] = max(ans[length - 1], arr[i]) 
# ans[i] : 'maximum of the minimum value' for length of all subarrays of length 'i+1'

# 4) But in 3rd case we can still left with some element in answer that won't be updated.
# for this traverse array again from right to left and update ans like:
# ans[i] = max(ans[i], ans[i + 1])
# why from right to left only?
# because right side contains answer for greater length then it can also contribute to ans of lesser length.

# Time = space = O(n)

class Solution:
    def maxOfMin(self,arr,n):
        left_smaller=  self.LeftSmallerNext(arr,n)     # will contain the indices of next smaller left for each ele
                                                           # means before that index they can go in the left
        right_smaller= self.RightSmallerNext(arr,n)
        
        ans = [float('-inf')] *n    # ans[i] : 'maximum of the minimum value' for length of all subarrays of length 'i+1'
        for i in range(n):
            length = right_smaller[i] - left_smaller[i] - 1
            ans[length - 1] = max(ans[length - 1], arr[i])  # taking value of all the elements that can contribute to ans for this length
        
        #  Some places in answer[] may not be filled yet.
	    # so fill them by taking maximum from right side because right side contains answer for greater length then it can also contribute
	    # to ans of lesser length
	    for i in range(n -2, -1, -1):
	        ans[i] = max(ans[i], ans[i+1])
        
        return ans
        
    
    def LeftSmallerNext(self,arr,n):
        stack, ans= [],[]
        for i in range(n):
            while stack and arr[stack[-1]]>= arr[i]:
                stack.pop()
            if not stack:  # if no next smaller exist means it can go till zero
                ans.append(-1)   # appending '-1' it means that ele can go before the index -1 i.e till zero
            else:  # means you have found the ans
                ans.append(stack[-1])    # in this case ele can go before the index of top of the stack in the left
            stack.append(i)
        return ans
    
    def RightSmallerNext(self,arr,n):
        stack,ans= [], []
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>= arr[i]:
                stack.pop()
            if not stack:   # if no next smaller exist means it can go till 'n'
                ans.append(n)
            else:   # means you have found the ans
                ans.append(stack[-1])   # in this case ele can go before the index of top of the stack in the right
            stack.append(i)
        return ans[::-1]
