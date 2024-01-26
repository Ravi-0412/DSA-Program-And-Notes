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
# so we have to check every possibilty like any node can go to left and right side respectively.
# means we can divide from every node.

# so we have to try every possibilty.
# MCM type pattern.

# tree will from from top to bottom.
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n= len(arr)
        maxInRange= collections.defaultdict(int)
        # finding the max value in range (i, j). Time: O(n^2).
        for i in range(n):
            maxInRange[(i, i)]= arr[i]
            for j in range(i+1, n):
                maxInRange[(i, j)]= max(arr[j], maxInRange[(i, j-1)])
        
        def minCost(i, j):
            if i== j:  # we can't form non-leaf full node with two children with one leaf node.
                return 0
            ans= float('inf')
            for k in range(i, j):  # there must be at least one node left on right side so going till ;j-1' only.
                tempAns= maxInRange[(i,k)]*maxInRange[(k+1, j)] + minCost(i, k) + minCost(k+1, j)   # maximising the value of particular node i.e it is finding all the possible way sum.
                ans= min(ans, tempAns)   # minimising overall sum i.e taking the minimum of all possible way.
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


# method 2: other optimised way
# logic: 
# Pick up the leaf node with minimum value.
# Combine it with its inorder neighbor which has smaller value between neighbors.
# Once we get the new generated non-leaf node, the node with minimum value is useless 
# (For the new generated subtree will be represented with the largest leaf node value.)
# Repeat it until there is only one node.

# time: O(n^2), space: O(n)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans= 0
        while len(arr) > 1:  # go until only one ele is left in the array.
            i= arr.index(min(arr))  # our minium ele in array is at this index only.
            ans+= arr[i] * min(arr[i-1: i] + arr[i+1: i+2])
            arr.pop(i)  # keep removing the minimum ele
        return ans


# best one : using stack
# 2nd method only.
# Just find the next greater element in the array, on the left and one right.
# time= O(n)= space

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans= 0
        stack= [float('inf')]  # to handle the base case
        for num in arr:
            # when you get any greater ele from the stack top then keep on poping 
            # since smaller ele is already in stack so we have to use it first to minimise the ans.
            while stack[-1] <= num: 
                mid= stack.pop()    # this will be the one of the ele we will use as leaf and now we have to find the min ele to just left or just right of it.
                ans+= mid * min(stack[-1], num)    # stack[-1] will be on left side of mid and num will be on right side of mid and we have to take minimum of both.
            stack.append(num)   # every ele we have to append in stack
        # Now pop ele from stack till only 2 ele is left (one 'inf' one and one the greatest ele of the array)
        while len(stack) > 2:
            ans+= stack.pop() * stack[-1]   # minimum will be on top.
        return ans