# write the logic in notes for all steps in detail(VVI)
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    days= len(points)-1
    return Reward(days,3,points)

def Reward(day,last,points):
    maxPoints= 0
    if day==0:
        for task in range(3):
            if task!= last:
                maxPoints= max(maxPoints,points[0][task])
        return maxPoints
    for task in range(3):
        if task!= last:
            maxPoints= max(maxPoints,points[day][task]+Reward(day-1,task,points))
    return maxPoints


# method2: memoization
# time complexity= O(n*4)*3. for each state you were making three function call
# space: O(n)recursion depth + O(n*4)
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[-1 for i in range(4)] for i in range(n)]
    days= len(points)-1
    return Reward(days,3,points,dp)

def Reward(day,last,points,dp):
    maxPoints= 0
    if day==0:
        for task in range(3):  # as no of task= 3 each day
            if task!= last:
                maxPoints= max(maxPoints,points[0][task])
        dp[day][last]= maxPoints
        return dp[day][last]
    if dp[day][last]!= -1:
        return dp[day][last]
    for task in range(3):
        if task!= last:
            maxPoints= max(maxPoints,points[day][task]+Reward(day-1,task,points,dp))
    dp[day][last]= maxPoints
    return dp[day][last]

# tabulation: Bottom up
# time complexity= O(n*4)*3. for each state you were making three function call
# space:O(n*4)
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    dp= [[0 for i in range(4)] for i in range(n)]
    dp[0][0]= max(points[0][1], points[0][2])
    dp[0][1]= max(points[0][0], points[0][2])
    dp[0][2]= max(points[0][0], points[0][1])
    dp[0][3]= max(points[0][0],points[0][1], points[0][2])
    for day in range(1,n):
        for last in range(4):  # 3+1
            for task in range(3):
                if task!= last:
                    dp[day][last]= max(dp[day][last], points[day][task] + dp[day-1][task])
    return dp[n-1][3]


# space optimisation
# for calculating the ans for current cell, we only did the value of just pre row
# time: O(4)  # no of task+1
def ninjaTraining(n: int, points: List[List[int]]) -> int:
    pre= [0 for i in range(4)]
    pre[0]= max(points[0][1], points[0][2])
    pre[1]= max(points[0][0], points[0][2])
    pre[2]= max(points[0][0], points[0][1])
    pre[3]= max(points[0][0],points[0][1], points[0][2])
    for day in range(1,n):
        curr= [0 for i in range(4)]
        for last in range(4):  # 3+1
            for task in range(3):
                if task!= last:
                    curr[last]= max(curr[last], points[day][task] + pre[task])
         # now copy the value of curr in pre
        pre= curr.copy()
    return pre[3]
