# Exactly same as : "84. Largest Rectangle in Histogram".
# Just we need to check if range of cur ele contain index 'k' or not.

# Reason: Every good subarray must contain index 'k'.

# Logic : if we consider each ele as minimum ele then how far we can go in left or right.
# We can go in left or right until we find any smaller ele than cur ele.
# Which is same as "84. Largest Rectangle in Histogram".

# Note: If without 'k' , it will be totally same as "Largest rectangle in the histogram" problem.\
# No need to make any changes.


# Time = space = O(n)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n, max_score = len(nums), 0
        left_smaller=  self.LeftSmallerNext(nums)     # will contain the indices of next smaller left for each ele
                                                           # means before that index they can go in the left.
        right_smaller= self.RightSmallerNext(nums)    # will contain the indices of next smaller right for each ele
                                                           # means before that index they can go in the right.
        for i in range(n):
            if left_smaller[i] < k < right_smaller[i]:
                width= (right_smaller[i] - left_smaller[i]) -1    # range in which they can go 
                local_score = nums[i]*width   
                max_score = max(max_score, local_score)
        return max_score
               
    def LeftSmallerNext(self, nums):
        stack, ans= [], []
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>= nums[i]:
                stack.pop()
            if not stack:  # if no next smaller exist means it can go till zero
                ans.append(-1)   # appending '-1' it means that ele can go before the index -1 i.e till zero
            else:  # means you have found the ans
                ans.append(stack[-1])    # in this case ele can go before the index of top of the stack in the left
            stack.append(i)
        return ans
    
    def RightSmallerNext(self, nums):
        n = len(nums)
        stack,ans= [], []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]]>= nums[i]:
                stack.pop()
            if not stack:   # if no next smaller exist means it can go till 'n'
                ans.append(n)
            else:   # means you have found the ans
                ans.append(stack[-1])   # in this case ele can go before the index of top of the stack in the right
            stack.append(i)
        return ans[::-1]


# Method 2: 
# Optimising above to space = O(1)
# Logic: Every good subarray must include nums[k]. (i <= k <= j)
# so start from index 'k' and keep expanding subarray either left or right of 'k'.

# We want to maximise min(A[i]..A[j]) slowly.
# To do this, we can check the values on both sides of the window.
# If nums[i - 1] <  nums[j + 1], we do j = j + 1
# If nums[i - 1] >= nums[j + 1], we do i = i - 1

# Time : O(N) , space : O(1)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = minimum = nums[k]
        i , j = k , k 
        while i > 0 or j < n-1:
            temp_left = nums[i -1] if i else 0
            temp_right = nums[j + 1] if j < n-1 else 0
            if temp_right > temp_left:
                j += 1
            else:
                i -= 1
            minimum = min(minimum , nums[i] , nums[j])
            ans = max(ans , minimum * (j - i + 1))
        return ans


# Method 3: Later try by Binary serach also