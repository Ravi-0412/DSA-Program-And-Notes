# Simple only

# Time: O(n*n*k) but it will never go till here.
# It will reach the base case faster i.e k==0 or also choosing next ele will also reduce the function call.

# Note vvi: When you have to select 'next' possible ele based on some condition then, no need to take 
# one more parameter 'pre' in function call, just do like this only.

# Raecursion + memoisation
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = cur + 1
            while next  < len(events):
                if events[next][0] > events[cur][1]:
                    break
                next += 1
            # max(notTake, take)
            return max(solve(cur + 1, k), events[cur][2] + solve(next, k - 1))

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
                        # To decide easily which event we can pick next.
        return solve(0, k)


# Note vvi: Finding the next in worst case can be O(n).
# But we can use binary search to find the 'next' in O(logn).
# Reason: we need to find the 1st event whose startDate > endDate of cur event.
# Since our events is already sorted acc to startDate, we can use binary search.
next = cur + 1
while next  < len(events):
    if events[next][0] > events[cur][1]:
        break
    next += 1

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, Comparator.comparingInt(a -> a[0]));  // sort acc to start time

        Map<String, Integer> memo = new HashMap<>();

        return solve(0, k, events, memo);
    }

    private int solve(int cur, int k, int[][] events, Map<String, Integer> memo) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.length || k == 0)
            return 0;

        String key = cur + "," + k;
        if (memo.containsKey(key))
            return memo.get(key);

        // we have two choices:
        // 1) either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if their start time is greater than the end time of this event.
        int next = binarySearch(events, events[cur][1]);

        int take = events[cur][2] + solve(next, k - 1, events, memo);
        int notTake = solve(cur + 1, k, events, memo);

        memo.put(key, Math.max(take, notTake));
        return memo.get(key);
    }
    // Note vvi: Finding the next in worst case can be O(n).
    // But we can use binary search to find the 'next' in O(logn).
    // Reason: we need to find the 1st event whose startDate > endDate of cur event.
    // Since our events is already sorted acc to startDate, we can use binary search.
    private int binarySearch(int[][] events, int endTime) {
        int left = 0, right = events.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (events[mid][0] > endTime)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}
"""
# C++ Code 
"""
class Solution {
    using pii = std::pair<int, int>;
    using tiii = std::tuple<int, int, int>;

    std::vector<tiii> events;
    std::unordered_map<std::string, int> memo;

public:
    int maxValue(std::vector<std::vector<int>>& input, int k) {
        for (auto& e : input)
            events.emplace_back(e[0], e[1], e[2]);  // start, end, value

        std::sort(events.begin(), events.end());  // sort acc to start time

        return solve(0, k);
    }

private:
    int solve(int cur, int k) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.size() || k == 0)
            return 0;

        std::string key = std::to_string(cur) + "," + std::to_string(k);
        if (memo.count(key))
            return memo[key];

        // we have two choices:
        // 1) either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if their start time is greater than the end time of this event.
        int next = binarySearch(std::get<1>(events[cur]));

        int take = std::get<2>(events[cur]) + solve(next, k - 1);
        int notTake = solve(cur + 1, k);

        return memo[key] = std::max(take, notTake);
    }
     // Note vvi: Finding the next in worst case can be O(n).
    // But we can use binary search to find the 'next' in O(logn).
    // Reason: we need to find the 1st event whose startDate > endDate of cur event.
    // Since our events is already sorted acc to startDate, we can use binary search.
    int binarySearch(int endTime) {
        int left = 0, right = events.size();
        while (left < right) {
            int mid = (left + right) / 2;
            if (std::get<0>(events[mid]) > endTime)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
};
"""

# Optimised one:
# Time: O(n*k*logn)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(None)
        def solve(cur, k):
            # either we have traversed all the events or we have chosen the maximum no of events allowed.
            if cur >= len(events) or k == 0:
                return 0
            # we have two choices:
            # 1)  either don't take the cur event
            # 2) if we take it then we need to find the next event we can take after this
            # next event we can only take if there start time is greater than the end time of this event.
            next = bisect.bisect_right(startDate, events[cur][1])
            return max(solve(cur + 1, k), events[cur][2] + solve(next, k - 1))

        events.sort()   # will sort acc to start time and if start timme equal then acc to end time
        startDate = [start for start, end, value in events]

        return solve(0, k)

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maxValue(int[][] events, int k) {
        // will sort acc to start time and if start time equal then acc to end time
        Arrays.sort(events, Comparator.comparingInt(a -> a[0]));
        int[] startDate = new int[events.length];
        for (int i = 0; i < events.length; i++) {
            startDate[i] = events[i][0];
        }

        Map<String, Integer> memo = new HashMap<>();
        return solve(0, k, events, startDate, memo);
    }

    private int solve(int cur, int k, int[][] events, int[] startDate, Map<String, Integer> memo) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.length || k == 0) return 0;

        String key = cur + "," + k;
        if (memo.containsKey(key)) return memo.get(key);

        // we have two choices:
        // 1) either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if their start time is greater than the end time of this event.
        int next = upperBound(startDate, events[cur][1]);

        int take = events[cur][2] + solve(next, k - 1, events, startDate, memo);
        int notTake = solve(cur + 1, k, events, startDate, memo);

        int res = Math.max(take, notTake);
        memo.put(key, res);
        return res;
    }

    private int upperBound(int[] arr, int target) {
        int left = 0, right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= target) left = mid + 1;
            else right = mid;
        }
        return left;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxValue(std::vector<std::vector<int>>& events, int k) {
        // will sort acc to start time and if start time equal then acc to end time
        std::sort(events.begin(), events.end());
        std::vector<int> startDate;
        for (auto& e : events)
            startDate.push_back(e[0]);

        std::unordered_map<std::string, int> memo;
        return solve(0, k, events, startDate, memo);
    }

private:
    int solve(int cur, int k, const std::vector<std::vector<int>>& events, const std::vector<int>& startDate,
              std::unordered_map<std::string, int>& memo) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.size() || k == 0)
            return 0;

        std::string key = std::to_string(cur) + "," + std::to_string(k);
        if (memo.count(key))
            return memo[key];

        // we have two choices:
        // 1) either don't take the cur event
        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if there start time is greater than the end time of this event.
        int next = std::upper_bound(startDate.begin(), startDate.end(), events[cur][1]) - startDate.begin();

        int take = events[cur][2] + solve(next, k - 1, events, startDate, memo);
        int notTake = solve(cur + 1, k, events, startDate, memo);

        return memo[key] = std::max(take, notTake);
    }
};
"""

# Using custom binary search for interview
"""
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
        
"""

# Java Code 
"""
import java.util.*;

public class Solution {
    public int maxValue(int[][] events, int k) {
        // Sort events according to start time and then by end time
        Arrays.sort(events, Comparator.comparingInt((int[] e) -> e[0]).thenComparingInt(e -> e[1]));
        int[] startDate = new int[events.length];
        for (int i = 0; i < events.length; i++) {
            startDate[i] = events[i][0];
        }

        // Initialize the memoization table
        int n = events.length;
        int[][] dp = new int[n + 1][k + 1];
        for (int[] row : dp) Arrays.fill(row, -1);

        return solve(0, k, events, startDate, dp);
    }

    private int solve(int cur, int k, int[][] events, int[] startDate, int[][] dp) {
        // Base case: either we have traversed all events or we have chosen the maximum number of events allowed.
        if (cur >= events.length || k == 0)
            return 0;

        // Check if we've already computed this state
        if (dp[cur][k] != -1)
            return dp[cur][k];

        // Option 1: Don't take the current event
        int option1 = solve(cur + 1, k, events, startDate, dp);

        // Option 2: Take the current event and find the next event we can take
        int next_event_index = findNextEventIndex(events[cur][1], startDate);
        int option2 = events[cur][2] + solve(next_event_index, k - 1, events, startDate, dp);

        // Store the result in the dp table and return it
        return dp[cur][k] = Math.max(option1, option2);
    }

    // Custom binary search function to find the next event index
    // Just we find the last index.
    private int findNextEventIndex(int endTime, int[] startDate) {
        int left = 0, right = startDate.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (startDate[mid] > endTime)
                right = mid - 1;
            else
                left = mid + 1;
        }
        // 'right' will point to last index having startTime = endTime. So 'right + 1' will give the next one
        return right + 1;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxValue(std::vector<std::vector<int>>& events, int k) {
        // Sort events according to start time and then by end time
        std::sort(events.begin(), events.end(), [](auto& a, auto& b) {
            return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
        });

        std::vector<int> startDate;
        for (auto& e : events)
            startDate.push_back(e[0]);

        // Initialize the memoization table
        int n = events.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, -1));

        return solve(0, k, events, startDate, dp);
    }

private:
    int solve(int cur, int k, const std::vector<std::vector<int>>& events,
              const std::vector<int>& startDate, std::vector<std::vector<int>>& dp) {
        // Base case: either we have traversed all events or we have chosen the maximum number of events allowed.
        if (cur >= events.size() || k == 0)
            return 0;

        // Check if we've already computed this state
        if (dp[cur][k] != -1)
            return dp[cur][k];

        // Option 1: Don't take the current event
        int option1 = solve(cur + 1, k, events, startDate, dp);

        // Option 2: Take the current event and find the next event we can take
        int next_event_index = findNextEventIndex(events[cur][1], startDate);
        int option2 = events[cur][2] + solve(next_event_index, k - 1, events, startDate, dp);

        // Store the result in the dp table and return it
        return dp[cur][k] = std::max(option1, option2);
    }

    // Custom binary search function to find the next event index
    // Just we find the last index.
    int findNextEventIndex(int endTime, const std::vector<int>& startDate) {
        int left = 0, right = startDate.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (startDate[mid] > endTime)
                right = mid - 1;
            else
                left = mid + 1;
        }
        // 'right' will point to last index having startTime = endTime. So 'right + 1' will give the next one
        return right + 1;
    }
};
"""
# My doubt
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


# Java Code 
"""
import java.util.*;

public class Solution {
    public int maxValue(int[][] events, int k) {
        // will sort acc to start time and if start time equal then acc to end time
        Arrays.sort(events, Comparator.comparingInt(a -> a[0]));
        return solve(0, k, events);
    }

    private int solve(int cur, int k, int[][] events) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.length || k == 0)
            return 0;

        // we have two choices:
        // 1) either don't take the cur event
        int notTake = solve(cur + 1, k, events);

        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if there start time is greater than the end time of this event.
        int take = 0;
        for (int next = cur + 1; next < events.length; next++) {
            if (events[next][0] > events[cur][1]) {
                take = events[cur][2] + solve(next, k - 1, events);
                break; // early exit as only the first such event matters
            }
        }

        return Math.max(take, notTake);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxValue(std::vector<std::vector<int>>& events, int k) {
        // will sort acc to start time and if start time equal then acc to end time
        std::sort(events.begin(), events.end());
        return solve(0, k, events);
    }

private:
    int solve(int cur, int k, const std::vector<std::vector<int>>& events) {
        // either we have traversed all the events or we have chosen the maximum no of events allowed.
        if (cur >= events.size() || k == 0)
            return 0;

        // we have two choices:
        // 1) either don't take the cur event
        int notTake = solve(cur + 1, k, events);

        // 2) if we take it then we need to find the next event we can take after this
        // next event we can only take if there start time is greater than the end time of this event.
        int take = 0;
        for (int next = cur + 1; next < events.size(); ++next) {
            if (events[next][0] > events[cur][1]) {
                take = events[cur][2] + solve(next, k - 1, events);
                break; // early exit as only the first valid next matters
            }
        }

        return std::max(take, notTake);
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

public class Solution {
    public int jobScheduling(int[] startTime, int[] endTime, int[] profit, int k) {
        List<int[]> jobs = new ArrayList<>();
        for (int i = 0; i < startTime.length; i++) {
            jobs.add(new int[]{startTime[i], endTime[i], profit[i]});
        }
        jobs.sort(Comparator.comparingInt(a -> a[0]));
        return helper(0, -1, jobs, k);
    }

    // '-1' last included index, '0': current index
    private int helper(int curr, int pre, List<int[]> jobs, int k) {
        if (curr == jobs.size() || k == 0)
            return 0;

        if (pre < 0 || jobs.get(curr)[0] >= jobs.get(pre)[1]) {
            // we can include this ele. but we have two choices either include in ans or not include.
            return Math.max(
                jobs.get(curr)[2] + helper(curr + 1, curr, jobs, k - 1),
                helper(curr + 1, pre, jobs, k)
            );
        }

        // only one choice we can't include this ele
        return helper(curr + 1, pre, jobs, k);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int jobScheduling(std::vector<int>& startTime, std::vector<int>& endTime, std::vector<int>& profit, int k) {
        std::vector<std::vector<int>> jobs;
        for (int i = 0; i < startTime.size(); ++i) {
            jobs.push_back({startTime[i], endTime[i], profit[i]});
        }
        std::sort(jobs.begin(), jobs.end());  // sort by start time
        return helper(0, -1, jobs, k);
    }

private:
    // '-1' last included index, '0': current index
    int helper(int curr, int pre, const std::vector<std::vector<int>>& jobs, int k) {
        if (curr == jobs.size() || k == 0)
            return 0;

        if (pre < 0 || jobs[curr][0] >= jobs[pre][1]) {
            // we can include this ele. but we have two choices either include in ans or not include.
            return std::max(
                jobs[curr][2] + helper(curr + 1, curr, jobs, k - 1),
                helper(curr + 1, pre, jobs, k)
            );
        }

        // only one choice we can't include this ele
        return helper(curr + 1, pre, jobs, k);
    }
};
"""
