# Basic:
# My doubt & mistakes
# After finding the next , i am not breaking the loop.
# So giving incorrect because in this take will always take last index satisfying the condition and
# breaking one we can't do in for loop because 'recursion' call is also associated .

# Either do like above one or take one more parameter 'pre' in function call.

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            notTake = solve(cur + 1 , k)
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            take = 0
            for next in range(cur + 1 , len(events)):
                if events[next][0] > events[cur][1]:
                    take = events[cur][2] + solve(next, k -1)
            return max(take, notTake)

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        return solve(0, k)

# Correct Method
# Method 1: 
# Recursion + Memoisation
# Simple only

# Time: O(n*n*k) but it will never go till here.
# It will reach the base case faster i.e k==0 or also choosing next ele will also reduce the function call.

# Note vvi: When you have to select 'next' possible ele based on some condition then, no need to take 
# one more parameter 'pre' in function call, just do like this only.

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
                        # To decide easily which event we can pick next.
        n = len(events)
        
        # Create memo array with -1 (means uncalculated)
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= n or k == 0:
                return 0
            
            if dp[cur][k] != -1:
                return dp[cur][k]
            
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = cur + 1
            while next < n:
                if events[next][0] > events[cur][1]:
                    break
                next += 1
            
            dp[cur][k] = max(
                solve(cur + 1, k),
                events[cur][2] + solve(next, k - 1)
            )
            return dp[cur][k]

        return solve(0, k)

# Java Code 
"""
import java.util.*;

class Solution {
    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));  // will sort acc to start time and if start time equal then acc to end time
                                                                     // To decide easily which event we can pick next.
        int n = events.length;

        // Create memo array with -1 (means uncalculated)
        int[][] dp = new int[n][k + 1];
        for (int[] row : dp) Arrays.fill(row, -1);

        return solve(0, k, events, dp);
    }

    public int solve(int cur, int k, int[][] events, int[][] dp) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.length || k == 0)
            return 0;

        if (dp[cur][k] != -1)
            return dp[cur][k];

        // we have two choices:
        // 1)  either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if their start time is greater than the end time of this event.
        int next = cur + 1;
        while (next < events.length) {
            if (events[next][0] > events[cur][1]) {
                break;
            }
            next++;
        }

        dp[cur][k] = Math.max(
            solve(cur + 1, k, events, dp),
            events[cur][2] + solve(next, k - 1, events, dp)
        );
        return dp[cur][k];
    }
}
"""
# C++ Code
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        sort(events.begin(), events.end());   // will sort acc to start time and if start time equal then acc to end time
                                              // To decide easily which event we can pick next.
        int n = events.size();

        // Create memo array with -1 (means uncalculated)
        vector<vector<int>> dp(n, vector<int>(k + 1, -1));

        return solve(0, k, events, dp);
    }

    int solve(int cur, int k, vector<vector<int>>& events, vector<vector<int>>& dp) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.size() || k == 0)
            return 0;

        if (dp[cur][k] != -1)
            return dp[cur][k];

        // we have two choices:
        // 1)  either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if their start time is greater than the end time of this event.
        int next = cur + 1;
        while (next < events.size()) {
            if (events[next][0] > events[cur][1]) {
                break;
            }
            next++;
        }

        dp[cur][k] = max(
            solve(cur + 1, k, events, dp),
            events[cur][2] + solve(next, k - 1, events, dp)
        );
        return dp[cur][k];
    }
};
"""

# Method 2:
# Take one more parameter 'pre' in function call.
# Replaced events -> jobs

# Can further optimise using binary search.

class Solution:
    def jobScheduling(self, jobs: List[List[int]], k: int) -> int:
        jobs = []
        for i in range(len(startTime)):
            jobs.append([startTime[i], endTime[i], profit[i]])
        jobs.sort()
        return self.helper(0, -1, jobs)  # '-1' last included index, '0': current index
    
    def helper(self, curr, pre, jobs, k):
        if curr == len(jobs) or k == 0:
            return 0
        if pre < 0 or jobs[curr][0] >= jobs[pre][1] :  # we can include this ele. but we have two choices either include in ans or not include.
            return max(jobs[curr][2] + self.helper(curr + 1, curr, jobs, k - 1), self.helper(curr + 1, pre, jobs, k))
        # only one choice we can't include this ele
        return self.helper(curr + 1, pre, jobs)

# Java Code 
"""
import java.util.*;

class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit, int k) {
        List<int[]> jobs = new ArrayList<>();
        for (int i = 0; i < startTime.length; i++) {
            jobs.add(new int[] { startTime[i], endTime[i], profit[i] });
        }

        jobs.sort(Comparator.comparingInt(a -> a[0]));  // sort by start time

        return helper(0, -1, k, jobs);  // '-1' last included index, '0': current index
    }

    public int helper(int curr, int pre, int k, List<int[]> jobs) {
        if (curr == jobs.size() || k == 0)
            return 0;

        if (pre < 0 || jobs.get(curr)[0] >= jobs.get(pre)[1]) {
            // we can include this element. but we have two choices either include or not
            return Math.max(
                jobs.get(curr)[2] + helper(curr + 1, curr, k - 1, jobs),
                helper(curr + 1, pre, k, jobs)
            );
        }

        // only one choice, we can't include this element
        return helper(curr + 1, pre, k, jobs);
    }
}
"""
# C++ Code
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit, int k) {
        vector<vector<int>> jobs;
        for (int i = 0; i < startTime.size(); ++i) {
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        }

        sort(jobs.begin(), jobs.end());  // sort by start time

        return helper(0, -1, k, jobs);  // '-1' last included index, '0': current index
    }

    int helper(int curr, int pre, int k, vector<vector<int>>& jobs) {
        if (curr == jobs.size() || k == 0)
            return 0;

        if (pre < 0 || jobs[curr][0] >= jobs[pre][1]) {
            // we can include this element. but we have two choices either include or not
            return max(
                jobs[curr][2] + helper(curr + 1, curr, k - 1, jobs),
                helper(curr + 1, pre, k, jobs)
            );
        }

        // only one choice, we can't include this element
        return helper(curr + 1, pre, k, jobs);
    }
};
"""

# Method 3: 

# Note vvi: Finding the next in worst case can be O(n).
# But we can use binary search to find the 'next' in O(logn).
# Reason: we need to find the 1st event whose startDate > endDate of cur event.
# Since our events is already sorted acc to startDate, we can use binary search.

"""
next = cur + 1
while next  < len(events):
    if events[next][0] > events[cur][1]:
        break
    next += 1
"""

# Optimised one:
# Time: O(n*k*logn)
# Note: you can use inbuilt ' next = bisect.bisect_right(startDate, events[cur][1])' as well.

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        # Custom binary search function to find the next event index
        # Just we find the last index.
        def find_next_event_index(start_time):
            left, right = 0, len(startDate) - 1
            while left <= right:
                mid = (left + right) // 2
                if startDate[mid] > start_time:  # We need to find the first event that starts after current event ends
                    right = mid -1
                else:
                    left = mid + 1
            return right + 1  # 'right' will point to last index having startTime = start_time. So 'right + 1' will give the next one

        # Sort events according to start time and then by end time
        events.sort(key=lambda x: (x[0], x[1]))
        startDate = [start for start, end, value in events]

        # Initialize the memoization table
        n = len(events)
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(cur, k):
            # Base case: either we have traversed all events or we have chosen the maximum number of events allowed.
            if cur >= n or k == 0:
                return 0
            
            # Check if we've already computed this state
            if dp[cur][k] != -1:
                return dp[cur][k]
            
            # Option 1: Don't take the current event
            option1 = solve(cur + 1, k)
            
            # Option 2: Take the current event and find the next event we can take
            next_event_index = find_next_event_index(events[cur][1])
            option2 = events[cur][2] + solve(next_event_index, k - 1)
            
            # Store the result in the dp table and return it
            dp[cur][k] = max(option1, option2)
            return dp[cur][k]

        return solve(0, k)

# Java Code 
"""
import java.util.*;

class Solution {
    public int maxValue(int[][] events, int k) {
        // Sort events according to start time and then by end time
        Arrays.sort(events, (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);

        // Create a list of start times for binary search
        int[] startDate = new int[events.length];
        for (int i = 0; i < events.length; i++) {
            startDate[i] = events[i][0];
        }

        // Initialize the memoization table
        int[][] dp = new int[events.length + 1][k + 1];
        for (int[] row : dp) Arrays.fill(row, -1);

        return solve(0, k, events, startDate, dp);
    }

    // Custom binary search function to find the next event index
    public int findNextEventIndex(int time, int[] startDate) {
        int left = 0, right = startDate.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (startDate[mid] > time) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return right + 1;  // 'right' will point to last index having startTime = time. So 'right + 1' will give the next one
    }

    public int solve(int cur, int k, int[][] events, int[] startDate, int[][] dp) {
        // Base case
        if (cur >= events.length || k == 0)
            return 0;

        if (dp[cur][k] != -1)
            return dp[cur][k];

        // Option 1: Don't take the current event
        int option1 = solve(cur + 1, k, events, startDate, dp);

        // Option 2: Take the current event and find the next available event
        int nextEventIndex = findNextEventIndex(events[cur][1], startDate);
        int option2 = events[cur][2] + solve(nextEventIndex, k - 1, events, startDate, dp);

        dp[cur][k] = Math.max(option1, option2);
        return dp[cur][k];
    }
}
"""
# C++ Code
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) {
        // Sort events according to start time and then by end time
        sort(events.begin(), events.end());

        // Create start time array for binary search
        vector<int> startDate;
        for (const auto& e : events) {
            startDate.push_back(e[0]);
        }

        // Initialize the memoization table
        int n = events.size();
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, -1));

        return solve(0, k, events, startDate, dp);
    }

    // Custom binary search function to find the next event index
    int findNextEventIndex(int time, const vector<int>& startDate) {
        int left = 0, right = startDate.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (startDate[mid] > time) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return right + 1;  // 'right' will point to last index having startTime = time. So 'right + 1' will give the next one
    }

    int solve(int cur, int k, const vector<vector<int>>& events, const vector<int>& startDate, vector<vector<int>>& dp) {
        // Base case
        if (cur >= events.size() || k == 0)
            return 0;

        if (dp[cur][k] != -1)
            return dp[cur][k];

        // Option 1: Don't take the current event
        int option1 = solve(cur + 1, k, events, startDate, dp);

        // Option 2: Take the current event and find the next available one
        int nextEventIndex = find
"""