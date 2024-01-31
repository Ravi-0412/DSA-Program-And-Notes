# Method 1: Brute force

# Logic: 
# Any no can be peak element so 
# Consider each of the element as the max point and then evaluate total sum.

# Element on left and right of 'peak' will be in decreasing order.

# Time: O(n^2)

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        ans = 0
        for i in range(n):
            curSum = pre = maxHeights[i]
            # calculating sum left of 'i'
            for j in range(i - 1, -1, -1):
                # value of next ele can't be more than pre.
                pre = min(maxHeights[j], pre)
                curSum += pre
            pre = maxHeights[i]
            # calculating sum left of 'i'
            for k in range(i + 1, n):
                pre = min(maxHeights[k], pre)
                curSum += pre
            
            ans = max(ans, curSum)
        return ans


# Method 2:
# optimising using stack to find the sum when a[i] is taken as peak element.

# Note: max value we can put for elements to left 'i' and right 'i' is a[i].
# But we can only put on both the sides until we get any index having value < a[i].

# First do for left side.
# suppose we found index 'j' on left such that a[i] > a[j].
# then you can replace from index 'j + 1' to 'i' by a[i] => no of ele = (i - j)
# and we can add res[j] to get sum on left when a[i] is peak.
# left_sum[i] = (i - j) * a[i] + left_sum[j]

# In same way we can do for right side for right sum.

# After that our ans = max(leftSum[i] + rightSum[i] - a[i]) for all indexes.

# subtracting 'a[i]' from ans because a[i] is added two times i.e in leftSum and rightSum both.

# Short: nums[i] ko us index tak rakh sakte h jb tak isse hmko chota na mile dono side.
# So 1st we need to find the next smaller index on both left/right for all elements.

# time = O(n)

class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        n = len(maxHeights)

        def nextSmallerLeft(a):
            stack2 = []
            for i in range(n-1, -1, -1):
                while stack2 and a[stack2[-1]] > a[i]:
                    # means we got the next_smaller left  < for stack.pop(). 
                    ind = stack2.pop()
                    next_smaller_left[ind] = i
                stack2.append(i)
        
        def nextSmallerRight(a):
            stack1 = []
            for i in range(n):
                while stack1 and a[stack1[-1]] > a[i]:
                    # means we got the next_smaller right  < for stack.pop().
                    ind = stack1.pop()
                    next_smaller_right[ind] = i
                stack1.append(i)
        
        next_smaller_left  = [-1]*n
        nextSmallerLeft(maxHeights)
        next_smaller_right = [-1] * n
        nextSmallerRight(maxHeights)
        leftSum =  [0]*n  # left sum when maxHeights[i] is peak including maxHeights[i]
        rightSum = [0]*n  # right sum when maxHeights[i] is peak including maxHeights[i]
        ans = 0
        # Finding sum on left side when a[i] is peak including a[i]
        for i in range(n):
            l = next_smaller_left[i]
            if l == -1:
                leftSum[i] = (i + 1)* maxHeights[i]
            else:
                leftSum[i] = (i - l)* maxHeights[i] + leftSum[l]
        
        # Finding sum on right side when a[i] is peak including a[i]
        for i in range(n-1, -1, -1):
            r = next_smaller_right[i]
            if r == -1:
                rightSum[i] = (n - i)* maxHeights[i]
            else:
                rightSum[i] = (r - i)* maxHeights[i] + rightSum[r]

            ans = max(ans , leftSum[i] + rightSum[i] - maxHeights[i])  
        return ans
    

# can be done in two traversal.
# calculate the leftSum and rightSum while findig the nextSmaller only.
# Do by this later.
    

# Similar questions:
# 907. Sum of Subarray Minimums