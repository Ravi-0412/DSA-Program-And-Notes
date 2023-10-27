# Method 1:
# Just sliding window  + SortedList()
# Additional thing , we need to keep tarck of max(included_robots).
# for keeping track maximum in  less than O(n), we can use 'sortedList()'.

# Note : for taking the maximum from cur included elements 
# We can use maxHeap also. 
# Sliding window + heap

# Time: O(n*logn), 
# O(logn): for getting maximu each time

from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) ->int:
        n = len(chargeTimes)
        minBudget =    chargeTimes[0] + runningCosts[0]
        sorted_time = SortedList()
        j = i = 0
        curSum = 0
        ans = 0
        while j < n:
            # keep adding the robot
            curSum += runningCosts[j]
            sorted_time.add(chargeTimes[j])
            # check if cost went out of budget.
            # top of 'sorted_time' will give maximum chargeTime of included robots.
            # 'j - i + 1' , no of robot included
            while i <= j and sorted_time[-1] + (j - i + 1) * curSum > budget:
                # keep removing from start
                sorted_time.remove(chargeTimes[i])
                curSum -= runningCosts[i]
                i += 1
            ans = max(ans, j -i + 1)
            j += 1
        return ans


# Method 2:
# For getting maximum in O(1) after each ele 
# we can use mono decreasing deque.
# Just similar to Q like : "239. Sliding Window Maximum" , "1425. Constrained Subsequence Sum".

# Time = space= O(n)

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) ->int:
        n = len(chargeTimes)
        j = i = 0
        curSum = 0
        ans = 0
        dq = deque()   # will store indexes according to their values i.e descending order
        while j < n:
            # keep adding the robot cost
            curSum += runningCosts[j]
            # Now remove those index from last of subarray that won't be possible maximum chargingTimes for upcoming elements
            # All those indexes having values <= chargingTimes[i] won't be possible maximum
            # 'j - i + 1' , no of robot included
            while dq and chargeTimes[dq[-1]] <= chargeTimes[j]:
                dq.pop()
            dq.append(j)
            # Now check if cost is out of budget
            # Note: Can't use while loop here because 'dq' starting ele may not be in same order as we have to remove like i, i + 1, i+ 2...
            # dq[0]: will store the index of maximum value of subarray
            if chargeTimes[dq[0]] + (j - i + 1) * curSum > budget:
                curSum -= runningCosts[i]
                # check if start of 'dq' is 'i'. Then remove from dq also.
                if dq[0] == i:
                    dq.popleft()
                i += 1
            ans = max(ans, j -i + 1)
            j += 1
        return ans


# Method 3: 
# Solve using binary search also