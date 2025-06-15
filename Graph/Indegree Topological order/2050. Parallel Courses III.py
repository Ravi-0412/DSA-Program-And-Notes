# Method 1: 

# Q: find the total months required when we will complete all the courses of last level.

"""
my mistake:
i was doing batch(level) by level 
Explanation:  The time taken for the batch will be maximum time taken for any course in the batch. 
Thus solving batch-wise, the minimum total time taken to complete all the courses will be the sum of time taken for each batch.

This greedy approach won't work.
e.g : Input: n = 5, relations = [[1,2],[2,5],[3,4],[4,5]], time = [2, 7, 10, 2, 3]
if we apply this logic then ans = 20 .

"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        AdjList= defaultdict(list)
        for prev,next in relations:
            AdjList[prev -1].append(next -1)  # converting to zero based indexing
        
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1
        
        # now applying the BFS to get the topological order
        Q  = collections.deque()
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)

        months = 0
        while Q:
            curMonth = 0   # minimum month required to complete the courses at cur level
            for i in range(len(Q)): 
                u= Q.popleft()
                curMonth = max(curMonth, time[u])
                # after poping decrease the indegree of all node adjacent to 'u'
                for j in AdjList[u]:
                    indegree[j] -= 1   
                    if indegree[j]== 0:   # the preRequisite of this courses is studied in pre sem so we can study this course in next sem.
                        Q.append(j)
                    
            months += curMonth
        return months


# Correct method:


"""

Note: 1st draw above example on pen and paper  for proper visualisation.

Explanation for ans = 20: If we take all available courses as a single batch, 
and then extend the new batch by adding courses with all prerequisites fulfilled,
then the time taken will be max⁡(2,10) + max⁡(7,2) + max⁡(3) = 10+7+3 = 20

note vvi: However, we can realize that by end of 12 months, we can complete courses [1, 2, 3, 4]. Then complete [5] afterwards.
 Thus, the minimum time taken is 12+3=15 Hence, 15 is the optimal solution.

vvi How?
Bottom-line: Solving batch-by-batch and taking the maximum time taken for any course in the batch, 
and then summing up the time taken for each batch, is not optimal. 
The logical intuition of failure of THIS VERSION of Greedy is that the moment one course 
in the current batch is being learned, we may complete other courses which are not in the 
current batch but available NOW because its prerequisites are satisfied by some just-completed 
courses of the current batch. It's not necessary to wait for all courses in the current 
batch to be completed to start newly available courses.

So for handling this we need to keep track of maxTime taken by any course to complete.
Then our ans = max(max Time taken by any course to complete) means in this time we can complete all the courses.
"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        AdjList= defaultdict(list)
        for prev,next in relations:
            AdjList[prev -1].append(next -1)  # converting to zero based indexing
        
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1

        # now applying the BFS to get the topological order
        Q  = collections.deque()
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)
        maxTime = time.copy()
        months = 0
        while Q:
            for i in range(len(Q)): 
                u= Q.popleft()
                months = max(months, maxTime[u])
                # after poping decrease the indegree of all node adjacent to 'u'
                for j in AdjList[u]:
                    indegree[j] -= 1
                    maxTime[j] = max(maxTime[j] , maxTime[u] + time[j])
                    if indegree[j]== 0:   # the preRequisite of this courses is studied in pre sem so we can study this course in next sem.
                        Q.append(j)
                    
        return months

# java
"""
import java.util.*;

class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());

        // building the adjacency list
        for (int[] rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            adjList.get(prev).add(next);  // converting to zero-based indexing
        }

        int[] indegree = new int[n];
        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList.get(i)) {
                indegree[neighbor]++;  // if neighbor is adj to 'i' means there is one indegree edge to 'neighbor'
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        int[] maxTime = Arrays.copyOf(time, n);
        int months = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int u = queue.poll();
                months = Math.max(months, maxTime[u]);

                // after popping, decrease the indegree of all nodes adjacent to 'u'
                for (int v : adjList.get(u)) {
                    indegree[v]--;
                    maxTime[v] = Math.max(maxTime[v], maxTime[u] + time[v]);

                    // if indegree becomes zero, we can take this course next
                    if (indegree[v] == 0) {
                        queue.offer(v);
                    }
                }
            }
        }

        return months;
    }
}

"""

# C++
"""
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<vector<int>> adjList(n);

        // building the adjacency list
        for (auto& rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            adjList[prev].push_back(next);  // converting to zero-based indexing
        }

        vector<int> indegree(n, 0);
        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            for (int neighbor : adjList[i]) {
                indegree[neighbor]++;  // if neighbor is adj to 'i' means there is one indegree edge to 'neighbor'
            }
        }

        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        vector<int> maxTime = time;  // copy initial times
        int months = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int u = q.front(); q.pop();
                months = max(months, maxTime[u]);

                // after popping, decrease the indegree of all nodes adjacent to 'u'
                for (int v : adjList[u]) {
                    indegree[v]--;
                    maxTime[v] = max(maxTime[v], maxTime[u] + time[v]);

                    // if indegree becomes zero, we can take this course next
                    if (indegree[v] == 0) {
                        q.push(v);
                    }
                }
            }
        }

        return months;
    }
};

"""


# Method 2: Good way
"""
our ans = total months required when we will complete all the courses of last level.
And for reaching the last level we need to go through some paths i.e we have to complete all the prerequisite.

vvi: So we can reduce this Q to : 
"Find the maximum path sum we can get".

For max_path_sum we need to check from course with indegree '0' i.e at 1st level to course at last level i.e highest indegree.
    
Note vvi: Whenever you have to add the current value by taking min/max from all sub-problems then apply this method only.
Note: Keep this method in mind, will help in lot of problems.


Note vvi: when time 't' will be equal for all the courses then 
ans = no_level * t.
"""

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        AdjList= defaultdict(list)
        for prev,next in relations:
            AdjList[prev -1].append(next -1)  # converting to zero based indexing
        # will give max_path_sum when we will start from this given 'course'
        def dfs(course):
            if dp[course] != -1:
                return dp[course]
            if not AdjList[course]:
                # If there is no adjacent node to this course i.e this course at last level.
                dp[course] = time[course]
                return dp[course]
            # find max path from all it's adjacent and add his time to get max_path+sum from this 'course'
            max_path_sum = 0  # will store max_path_sum from all its neighbours
            for next in AdjList[course]:
                max_path_sum = max(max_path_sum, dfs(next))
            dp[course] = time[course] + max_path_sum
            return dp[course]

        dp = [-1 for i in range(n)]
        # wiil called from here only for 1st level i.e indegree '0' . 
        # for other courses it will get calculated inside 'dfs' automatically.
        # Calling for all course one by one to take care of multiple component.
        for course in range(n):  
            dfs(course)
        return max(dp)


# java
"""
import java.util.*;

class Solution {
    List<List<Integer>> adjList;
    int[] dp;
    int[] time;

    public int minimumTime(int n, int[][] relations, int[] time) {
        this.time = time;
        adjList = new ArrayList<>();
        for (int i = 0; i < n; i++) adjList.add(new ArrayList<>());
        
        for (int[] rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            adjList.get(prev).add(next); // converting to zero-based indexing
        }

        dp = new int[n];
        Arrays.fill(dp, -1);

        // will be called only for 1st level i.e indegree '0'. 
        // For other courses it will get calculated inside 'dfs' automatically.
        // Calling for all courses one by one to take care of multiple components.
        for (int i = 0; i < n; i++) {
            dfs(i);
        }

        int maxTime = 0;
        for (int t : dp) {
            maxTime = Math.max(maxTime, t);
        }
        return maxTime;
    }

    // will give max_path_sum when we start from this given 'course'
    private int dfs(int course) {
        if (dp[course] != -1) return dp[course];

        if (adjList.get(course).isEmpty()) {
            // If there is no adjacent node to this course i.e. this course is at last level.
            dp[course] = time[course];
            return dp[course];
        }

        // find max path from all its adjacents and add its time to get max_path_sum from this 'course'
        int maxPathSum = 0;
        for (int next : adjList.get(course)) {
            maxPathSum = Math.max(maxPathSum, dfs(next));
        }
        dp[course] = time[course] + maxPathSum;
        return dp[course];
    }
}

"""
    

# C++
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> adjList;
    vector<int> dp;
    vector<int> time;

    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        this->time = time;
        adjList.resize(n);

        for (auto& rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            adjList[prev].push_back(next);  // converting to zero-based indexing
        }

        dp.assign(n, -1);

        // will be called only for 1st level i.e indegree '0'. 
        // For other courses it will get calculated inside 'dfs' automatically.
        // Calling for all courses one by one to take care of multiple components.
        for (int i = 0; i < n; ++i) {
            dfs(i);
        }

        int maxTime = 0;
        for (int t : dp) {
            maxTime = max(maxTime, t);
        }
        return maxTime;
    }

    // will give max_path_sum when we start from this given 'course'
    int dfs(int course) {
        if (dp[course] != -1) return dp[course];

        if (adjList[course].empty()) {
            // If there is no adjacent node to this course i.e. this course is at last level.
            dp[course] = time[course];
            return dp[course];
        }

        // find max path from all its adjacents and add its time to get max_path_sum from this 'course'
        int maxPathSum = 0;
        for (int next : adjList[course]) {
            maxPathSum = max(maxPathSum, dfs(next));
        }
        dp[course] = time[course] + maxPathSum;
        return dp[course];
    }
};
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> adjList;
    vector<int> dp;
    vector<int> time;

    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        this->time = time;
        adjList.resize(n);

        for (auto& rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            adjList[prev].push_back(next);  // converting to zero-based indexing
        }

        dp.assign(n, -1);

        // will be called only for 1st level i.e indegree '0'. 
        // For other courses it will get calculated inside 'dfs' automatically.
        // Calling for all courses one by one to take care of multiple components.
        for (int i = 0; i < n; ++i) {
            dfs(i);
        }

        int maxTime = 0;
        for (int t : dp) {
            maxTime = max(maxTime, t);
        }
        return maxTime;
    }

    // will give max_path_sum when we start from this given 'course'
    int dfs(int course) {
        if (dp[course] != -1) return dp[course];

        if (adjList[course].empty()) {
            // If there is no adjacent node to this course i.e. this course is at last level.
            dp[course] = time[course];
            return dp[course];
        }

        // find max path from all its adjacents and add its time to get max_path_sum from this 'course'
        int maxPathSum = 0;
        for (int next : adjList[course]) {
            maxPathSum = max(maxPathSum, dfs(next));
        }
        dp[course] = time[course] + maxPathSum;
        return dp[course];
    }
};


"""