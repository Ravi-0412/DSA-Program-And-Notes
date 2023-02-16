# write the logic in notes for all steps in detail(VVI)
# notes: page 152
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    return Reward(n,3,points)

def Reward(day,last,points):
    if day== 0:
        return 0
    maxPoints= 0
    for task in range(3):
        if task!= last:
            maxPoints= max(maxPoints,points[day-1][task]+Reward(day-1,task,points))
    return maxPoints

# Not able to memoise and do Tabulation.
# check later.
# got ans by other approach. simple one.

# method2: memoization
# time complexity= O(n*4)*3. for each state you were making three function call
# space: O(n)recursion depth + O(n*4).

# Note: for dimension of dp variables, check range in which we are taking values from array.
# for day we are using from: day '0' to day 'n-1'. and for task : from '0' to '3'.

# Not able to memoise
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[-1 for last in range(4)] for day in range(n +1)]
    return Reward(n,3,points, dp)

def Reward(day,last,points, dp):
    if day== 0:   # we have processed one task on each day.
        return 0
    if dp[day-1][last]!= -1:
        return dp[day-1][last]
    maxPoints= 0
    for task in range(3):
        if task!= last:
            maxPoints= max(dp[day-1][last],points[day-1][task]+Reward(day-1,task,points, dp))
    dp[day-1][last]= maxPoints
    return dp[day-1][last]

# not able to convert into Tbaulation with same logic.
# def ninjaTraining(n: int, points: List[List[int]]) -> int:
#     dp= [[0 for last in range(4)] for day in range(n)]
#     for day in range(1, n+1):
#         for last in range(4): # 3 +1
#             for task in range(3):
#                 dp[day-1][last]= max(dp[day-1][last], points[day-1][task] + dp[day-1][task])
#     return dp[n-1][3]



# Approach 2: 
#  To make index of day same as function call.
# starting from day '0' with last task= 3.

def ninjaTraining(n: int, points: List[List[int]]) -> int:
    return Reward(0,3,points)

def Reward(day,last,points):
    if day== len(points):
        return 0
    maxPoints= 0
    for task in range(3):
        if task!= last:
            maxPoints= max(maxPoints,points[day][task]+Reward(day+1,task,points))
    return maxPoints

# memoization
# time complexity= O(n*4)*3. for each state you were making three function call
# space: O(n)recursion depth + O(n*4).
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[-1 for last in range(4)] for day in range(n +1)]
    return Reward(0,3,points, dp)

def Reward(day,last,points, dp):
    if day== len(points):
        return 0
    if dp[day][last]!= -1:
        return dp[day][last]
    maxPoints= 0
    for task in range(3):
        if task!= last:
            maxPoints= max(maxPoints,points[day][task]+Reward(day+1,task,points, dp))
    dp[day][last]= maxPoints
    return dp[day][last]

# Tabulation
# just convert the variable chnaging in function in for loop(from base case to value it can go) 
# and after that just copy paste the recursive Q after base case.
# keep the variabe name same in for loop as name variable in recursive function.
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[0 for last in range(4)] for day in range(n +1)]
    for day in range(n-1,-1,-1):
        for last in range(4): # 3 + 1
            maxPoints= 0
            for task in range(3):
                if task!= last:
                    maxPoints= max(maxPoints,points[day][task]+ dp[day +1][task])
            dp[day][last]= maxPoints
    return dp[0][3]
