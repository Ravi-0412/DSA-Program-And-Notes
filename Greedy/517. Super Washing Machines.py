# Read properly this line of Q:
# "For each move, you could choose any m (1 <= m <= n) washing machines, 
# and pass one dress of each washing machine to one of its adjacent washing machines at the same time".

# i.e giving out loads and receiving loads are different. 
# One machines can at most give 1 load each step, but can receive at most 2 loads each step.

# Method 1:
# if sum(machine) is not divisible by no_machine then, distribution is not possible.

# Otherwise, we can always transfer a dress from one machine to another, 
# one at a time until every machines reach the same number,so there must be a solution.
# In this way, the total actions is sum of operations on every machine.

# Note: Since we can operate several machines at the same time, 
# the minium number of moves is the maximum number of necessary operations on every machine.

# How to calculate for single machine:
# For a single machine, necessary operations is to transfer dresses from one side to another 
# until sum of both sides and itself reaches the average number. 
# We can calculate (required dresses) - (contained dresses) of each side as L and R:

# 1) L > 0 && R > 0: both sides lacks dresses, and we can only export 
# one dress from current machines at a time, so result is abs(L) + abs(R)
# 2) L < 0 && R < 0: both sides contains too many dresses, and 
# we can import dresses from both sides at the same time, so result is max(abs(L), abs(R))
# 3) L < 0 && R > 0 or L >0 && R < 0: the side with a larger absolute value will import/export its extra dresses from/to 
# current machine or other side, so result is max(abs(L), abs(R))

# '2' and '3' can be combined together.

# Note: 'l' and 'r' can be negative also.

# For example, [1, 0, 5], average is 2
# for 1, L = 0 * 2 - 0 = 0, R = 2 * 2 - 5= -1, result = 1
# for 0, L = 1 * 2 - 1= 1, R = 1 * 2 - 5 = -3, result = 3
# for 5, L = 2 * 2 - 1= 3, R = 0 * 2 - 0= 0, result = 3
# so minium moves is 3

# Link: https://leetcode.com/problems/super-washing-machines/solutions/99181/C++-16ms-O(n)-solution-(with-trivial-proof)/comments/103242/

# Time = space = O(n)

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n  != 0:
            return -1

        prefixSum = [0] * (n+ 1)
                    # prefix[i] will contains before index 'i' i.e index 'i-1'.
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + machines[i]
        avg = total // n
        ans = 0
        for i in range(n):
            # 'jitna hona chahiye before index i' - 'kitna h'
            # 'kitna h' = sum till 'i-1'.
            l = i * avg - prefixSum[i]   # required_extra_left_side_i
            # 'jitna hona chahiye after index i' - 'kitna h'
            # 'kitna h' = sum from index 'i + 1' to 'n-1'.
            r = (n - i - 1) * avg - (prefixSum[n] - prefixSum[i + 1])  # required_extra_right_side_i
            if l > 0 and r > 0:
                ans = max(ans, abs(l) + abs(r))
            else:
                ans = max(ans, max(abs(l) , abs(r)))
        return ans


# Method 2:
# Explanation with example:
# For example, your machines[] is [0,0,11,5]. So your total is 16 and the target value for each machine is 4. 
# Convert the machines array to a kind of gain/lose array, we get: [-4,-4,7,1]. 
# Now what we want to do is go from the first one and try to make all of them 0.

# To make the 1st machines 0, you need to give all its "load" to the 2nd machines.
# So we get: [0,-8,7,1]
# then: [0,0,-1,1]
# lastly: [0,0,0,0], done.

# In this process, the least steps we need to eventually finish this process is determined by the 
# peak of abs(cnt) and the max of "gain/lose" array. In this case, the peak of abs(cnt) is 8 
# and the max of gain/lose array is 7. So the result is 8.

# Why this one is working?
# The logic here is to find the max/peak 'throughput' going from the leftmost washer to the rightmost washer,
# and the max of the 'GIVE-OUT' washer. The max of these two is the answer. 

#  We want the max/peak of the 'throughput' because for washer(s) from one side, 
# giving/receiving its load to/from washer(s) from the other side, their to-give/to-receive 
# loads accumulate during the transportation, like for [-2 -2 0 1, 3]. 
# (its original nums could be [1, 1, 3, 4, 6]), the leftmost -2 cannot be balanced 
# directly without going through the 2nd -2. So it is the same as [0, -4, 0, 1, 3] or [0, 0, -4, 1, 3]. 
# Only adjacent machines can transfer loads, and potentially balance each other or accumulate to-balance values.
# Here, 4 is the max absolute to-balance value we found going from left to right, so it is 4.

# Q) Why not Math.abs(load-avg)?
# Because [-1, 2 ,-1] and [1, -2, 1] are different!! 
# The former can be balanced with 2 steps, but the latter can be balanced with only 1 step!

# That is to say, giving out loads and receiving loads are different.
# One machines can at most give 1 load each step, but can receive at most 2 loads each step.

# Therefore, finding the max positive to-balance load is what we want. Like [0, -7, 8, -1], 
# no matter what you do or how you do it, the machines with 8 loads need no less than 8 to balance itself and become 0.

# Link: https://leetcode.com/problems/super-washing-machines/solutions/99185/super-short-easy-java-o-n-solution/

# Time = O(n)
# Space = O(1)

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n  != 0:
            return -1
        avg = total //n
        ans = 0
        cnt = 0
        for m in machines:
            load = m -avg   # can be negative
            ans = max(ans, load)
            cnt += load    # 'cur' can be negative also.
            ans = max(ans, abs(cnt))
        return ans
        