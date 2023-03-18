# logic in notes: 128.

# my mistakes:
# Approach one: just sort the take the minimum leaf nodes from start.

# Reason: we are checking the order of inorder traversal so this will not work.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n= len(arr)
        arr.sort()
        if n== 2:
            return arr[0]*arr[1]
        ans= arr[0]*arr[1]
        leftMax= arr[1]
        for i in range(2, n):
            rightMax= arr[i]
            ans+= leftMax * rightMax
            leftMax= rightMax
        return ans


# Approach 2:
# logic why it won't work in notes.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n= len(arr)
        if n== 2:
            return arr[0]*arr[1]
        # 1) left to right.
        ans1= arr[0]*arr[1]
        leftMax= max(arr[0], arr[1])
        for i in range(2, n):
            ans1+= leftMax * arr[i]
            leftMax= max(leftMax, arr[i])
        
        ans2= arr[-1]*arr[-2]
        rightMax= max(arr[-1], arr[-2])
        for i in range(n-3, -1, -1):
            ans2+= rightMax*arr[i]
            rightMax= max(rightMax, arr[i])
        return min(ans1, ans2)


# means greedy way it's not working anyway.
# what we have to do?
# Ans: we have to maximise the value of particular non-leaf nodes but we have to minimise the overall sum of values of non-leaf nodes.
# so we have to chekc evry possibilty like any node can go to left and right side respectively.
# means we can divide from every node.

# so we have to try every possibilty.
# MCM type pattern.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n= len(arr)
        maxInRange= collections.defaultdict(int)
        for i in range(n):
            maxInRange[(i, i)]= arr[i]
            for j in range(i+1, n):
                maxInRange[(i, j)]= max(arr[j], maxInRange[(i, j-1)])
        
        def minCost(i, j):
            if i== j:  # we can't form non-leaf full node with two children with one leaf node.
                return 0
            ans= float('inf')
            for k in range(i, j):  # there must be at least one node left on right side so going till ;j-1' only.
                tempAns= maxInRange[(i,k)]*maxInRange[(k+1, j)] + minCost(i, k) + minCost(k+1, j)
                ans= min(ans, tempAns)
            return ans


        return minCost(0, n-1)


# memoisation
# time: O(n^3), space: O(n^2)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n= len(arr)
        maxInRange= collections.defaultdict(int)
        for i in range(n):
            maxInRange[(i, i)]= arr[i]
            for j in range(i+1, n):
                maxInRange[(i, j)]= max(arr[j], maxInRange[(i, j-1)])
                
        @lru_cache(None)
        def minCost(i, j):
            if i== j:  # we can't form non-leaf full node with two children with one leaf node.
                return 0
            ans= float('inf')
            for k in range(i, j):  # there must be at least one node left on right side so going till j-1' only.
                tempAns= maxInRange[(i,k)]*maxInRange[(k+1, j)] + minCost(i, k) + minCost(k+1, j)
                ans= min(ans, tempAns)
            return ans

# memoise using hashmap or array.
# later do by Tabulation


# other optimised way
# method 2: 
# time: O(n^2), space: O(n)
# vvi: Here tree is being build from bottom to up(root).

# note: we will try to put the larger value leaf node closer to root so that that value is not counted in upper level.

# logic: when we build each level of the binary tree, it is the max left leaf node and max right lead node that are being used,
#  so we would like to put big leaf nodes close to the root. Otherwise, taking the leaf node with max value in the array as an example,
#  if its level is deep, for each level above it, its value will be used to calculate the non-leaf node value, which will result in a big total sum.

#  the greedy approach is to find the smallest value in the array, use it and its smaller neighbor to build a non-leaf node,
#  then we can safely delete it from the array since it has a smaller value than its neightbor so it will never be used again.
#  Repeat this process until there is only one node left in the array (which means we cannot build a new level any more). 

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans= 0
        while len(arr) > 1:  # go until only one ele is left in the array.
            i= arr.index(min(arr))  # our minium ele in array is at this index only.
            ans+= arr[i] * min(arr[i-1: i] + arr[i+1: i+2])
            arr.pop(i)  # keep removing the minimum ele
        return ans


# best one : using stack
# just the optimisation of above logic.
# logic: Just find the next greater element in the array, on the left and one right.
# vvi: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/solutions/478708/rz-summary-of-all-the-solutions-i-have-learned-from-discuss-in-python/

# why stack ?
# In the above approach, every time we delete the current minimum value, we need to start over and find the next smallest value again,
#  so repeated operations are more or less involved. To further accelerate it, one observation is that for each leaf node in the array,
#  when it becomes the minimum value in the remaining array,
#  its left and right neighbors will be the first bigger value in the original array to its left and right. This observation is a clue of a possible monotonic stack solution

# time= space= O(n^2).
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans= 0
        stack= [float('inf')]  # to handle the base case. stack will store ele in decreasing order.
        for num in arr:
            # when you get any smaller ele in stack then keep on poping since we have to minimse the ans
            while stack[-1] <= num:  # means top of stack is minimum till you so pop it and search for next greater tahn this ele i.e 'min of its neighbour'.
                mid= stack.pop()    # this will be the minimum ele and we have to take min of its left and right
                ans+= mid * min(stack[-1], num)    # stack[-1] will be on left side and num will be on right side  and we have to take minimum of both.
            stack.append(num)   # every ele we have to append in stack since it can be the next greater after poping any ele later.

        # Now pop ele from stack till only 2 ele is left (one 'inf' one and one the greatest ele of the array)
        while len(stack) > 2:  # minimum ele will on top of stack since stack is storing ele in decreasing order.
            ans+= stack.pop() * stack[-1]   # minimum will be on top.
        return ans