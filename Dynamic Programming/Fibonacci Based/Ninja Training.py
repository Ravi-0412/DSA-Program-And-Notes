# Method 1; 

"""
logic: 

The first approach that comes to our mind is the greedy approach. Now see the below example and try to understand that how it doesn’t give the correct solution.
example : DAY 1 :  10 30 20
          DAY 2 :  10 100 20

          Greedily, we'll pick 30 from day 1 (MAX) and 20 (Second MAX after 100) from day 2 as 100 cannot be picked due same activity cannot take place in two consecutive days
          so we end up the total as (30 + 20) = 50 points

          But clearly we can see, the actual answer should be (20 from day1 + 100 from day2) = 120 points

          so greedy fails!!

          Now we try out all possible options and Recursion will be the one which generates all possible options.

          what two things we need to consider here is 
          i) the current day as day ranges from 0 to n-1
          ii) the last chosen activity what we chose for day-1 or day+1 (it depends on how we consider the recursion call (0 to n-1) or (n-1 to 0) )

          f(currDay, lastAct) --> The maximum points till currDay with lastAct acitivity on pervious day
          Base case :  considering recursion call (n-1 to 0):
                     when we reach at day = 0 we calculate the max points and return it

                     considering recursion call (0 to n-1);
                     when we reach at day = n-1 we calcuate the max points and return it.
"""

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

# Java Code 
"""
public class Solution {
    public int ninjaTraining(int n, int[][] points) {
        return reward(0, 3, points);
    }

    private int reward(int day, int last, int[][] points) {
        if (day == points.length)
            return 0;

        int maxPoints = 0;
        for (int task = 0; task < 3; task++) {
            if (task != last) {
                maxPoints = Math.max(maxPoints, points[day][task] + reward(day + 1, task, points));
            }
        }
        return maxPoints;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int ninjaTraining(int n, std::vector<std::vector<int>>& points) {
        return reward(0, 3, points);
    }

private:
    int reward(int day, int last, std::vector<std::vector<int>>& points) {
        if (day == points.size())
            return 0;

        int maxPoints = 0;
        for (int task = 0; task < 3; ++task) {
            if (task != last) {
                maxPoints = std::max(maxPoints, points[day][task] + reward(day + 1, task, points));
            }
        }
        return maxPoints;
    }
};
"""

# Method 2: 
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

# Java Code 
"""
public class Solution {
    public int ninjaTraining(int n, int[][] points) {
        int[][] dp = new int[n + 1][4]; // dp[day][last]
        for (int i = 0; i <= n; i++)
            java.util.Arrays.fill(dp[i], -1);

        return reward(0, 3, points, dp);
    }

    private int reward(int day, int last, int[][] points, int[][] dp) {
        if (day == points.length)
            return 0;

        if (dp[day][last] != -1)
            return dp[day][last];

        int maxPoints = 0;
        for (int task = 0; task < 3; task++) {
            if (task != last) {
                maxPoints = Math.max(maxPoints, points[day][task] + reward(day + 1, task, points, dp));
            }
        }

        return dp[day][last] = maxPoints;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int ninjaTraining(int n, std::vector<std::vector<int>>& points) {
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(4, -1));
        return reward(0, 3, points, dp);
    }

private:
    int reward(int day, int last, const std::vector<std::vector<int>>& points,
               std::vector<std::vector<int>>& dp) {
        if (day == points.size())
            return 0;

        if (dp[day][last] != -1)
            return dp[day][last];

        int maxPoints = 0;
        for (int task = 0; task < 3; ++task) {
            if (task != last) {
                maxPoints = std::max(maxPoints, points[day][task] + reward(day + 1, task, points, dp));
            }
        }

        return dp[day][last] = maxPoints;
    }
};
"""

# Method 3: 
# Tabulation
# just convert the variable changing in function in for loop(from base case to value it can go) 
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

# Java Code 
"""
public class Solution {
    public int ninjaTraining(int n, int[][] points) {
        int[][] dp = new int[n + 1][4];
        for (int day = n - 1; day >= 0; day--) {
            for (int last = 0; last < 4; last++) {
                int maxPoints = 0;
                for (int task = 0; task < 3; task++) {
                    if (task != last) {
                        maxPoints = Math.max(maxPoints, points[day][task] + dp[day + 1][task]);
                    }
                }
                dp[day][last] = maxPoints;
            }
        }
        return dp[0][3];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int ninjaTraining(int n, std::vector<std::vector<int>>& points) {
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(4, 0));
        for (int day = n - 1; day >= 0; --day) {
            for (int last = 0; last < 4; ++last) {
                int maxPoints = 0;
                for (int task = 0; task < 3; ++task) {
                    if (task != last) {
                        maxPoints = std::max(maxPoints, points[day][task] + dp[day + 1][task]);
                    }
                }
                dp[day][last] = maxPoints;
            }
        }
        return dp[0][3];
    }
};
"""