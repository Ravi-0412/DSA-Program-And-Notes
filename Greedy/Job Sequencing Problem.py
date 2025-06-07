"""
NOTE: job is given as node not in form of array so we can't sort directly.

Note: Don't blindly start solving the problem, first:
1) study & understand problem properly.
2) See the input and output format 
3) VVI: Check if input is given in '0- based' indexing or '1-based' indexing.
4) Check the constraint 

Then only start to solve problem.


Logic: we will try to include job with maximum profit first.
But to get maximum ans, we will try to include other job as well.

So we will put job having maximum profit as far as possible.
steps:
1) create array of size = max_deadline_among_all_jobs
2) Sort jobs based on profit in descending order
3) Take the job one by one and place it at appropriate empty slot.
Place as far as possible so that we can include other job also.
For this start checking for empty slot from 'job_deadline' in reverse direction.

4) Once you find any empty slot then add the profit of that job in ans and 
mark that empty slot as occupied.
5) Return ans

Submitted on gfg.

time: O(n^2)
"""

'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    def JobScheduling(self,Jobs_given,n):
        Jobs.sort(key= lambda x: x.profit, reverse= True) 
        max_deadline_job= max(Jobs, key = lambda x : x.deadline)   # it will return the job details having max deadline
        max_deadline= max_deadline_job.deadline                   # it will return the job having max deadline among all jobs
        # print(max_deadline_job)
        # print(max_deadline)
        
        position= [-1]*(max_deadline + 1)   # '1-based' indexing so adding '1'.
        jobs_done, maxProfit= 0, 0
        # now place the job with maximum profit as far as possible.
        for job in Jobs:
            for j in range(job.deadline, 0, -1):   # '1-based' indexing so going till index '1' only
                if position[j] == -1:
                    position[j]= job.id
                    maxProfit += job.profit
                    jobs_done += 1
                    break   # after you fina any empty slot
        return [jobs_done, maxProfit]

# Java
"""
import java.util.Arrays;

class Job {
    int id, deadline, profit;
    Job(int id, int deadline, int profit) {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }
}

class Solution {
    public int[] JobScheduling(Job[] Jobs, int n) {
        // Sort jobs by profit in descending order
        Arrays.sort(Jobs, (a, b) -> b.profit - a.profit); 

        // Find the job with the maximum deadline
        Job max_deadline_job = Jobs[0];
        for (Job job : Jobs) {
            if (job.deadline > max_deadline_job.deadline) {
                max_deadline_job = job;
            }
        }
        int max_deadline = max_deadline_job.deadline; // it will return the job having max deadline among all jobs

        // '1-based' indexing so adding '1'
        int[] position = new int[max_deadline + 1];  
        Arrays.fill(position, -1);

        int jobs_done = 0, maxProfit = 0;

        // now place the job with maximum profit as far as possible
        for (Job job : Jobs) {
            for (int j = job.deadline; j > 0; j--) {  // '1-based' indexing so going till index '1' only
                if (position[j] == -1) {
                    position[j] = job.id;
                    maxProfit += job.profit;
                    jobs_done += 1;
                    break;  // after you find any empty slot
                }
            }
        }

        return new int[]{jobs_done, maxProfit};
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

struct Job {
    int id;
    int deadline;
    int profit;
};

class Solution {
public:
    vector<int> JobScheduling(Job Jobs[], int n) {
        // Sort jobs by profit in descending order
        sort(Jobs, Jobs + n, [](Job a, Job b) {
            return a.profit > b.profit;
        });

        // Find the job with the maximum deadline
        int max_deadline = 0;
        for (int i = 0; i < n; i++) {
            max_deadline = max(max_deadline, Jobs[i].deadline);  // it will return the job having max deadline among all jobs
        }

        vector<int> position(max_deadline + 1, -1);  // '1-based' indexing so adding '1'
        int jobs_done = 0, maxProfit = 0;

        // now place the job with maximum profit as far as possible
        for (int i = 0; i < n; i++) {
            for (int j = Jobs[i].deadline; j > 0; j--) {  // '1-based' indexing so going till index '1' only
                if (position[j] == -1) {
                    position[j] = Jobs[i].id;
                    maxProfit += Jobs[i].profit;
                    jobs_done += 1;
                    break;  // after you find any empty slot
                }
            }
        }

        return {jobs_done, maxProfit};
    }
};

"""
# If jobs are given in form of array like Jobs[i] = [job_id, deadline, profit]

def JobScheduling(Jobs,n):
    Jobs.sort(key= lambda x : x[2], reverse= True)
    max_deadline_job= max(Jobs, key = lambda x : x[1])   # it will return the job details having max deadline
    max_deadline= max_deadline_job[1]                   # it will return the job having max deadline among all jobs
    # print(max_deadline_job)
    # print(max_deadline)
    
    position= [-1]*max_deadline  # '0-based' indexing so no need to add '1' like above.
    jobs_done, maxProfit= 0, 0
    # now place the job with maximum profit as far as possible.
    for job in Jobs:
        id, deadline, profit= job[0], job[1], job[2]
        for j in range(deadline-1, -1, -1):   # '0-based' indexing so going till '0' index.
            if position[j]== -1:
                position[j]= id
                maxProfit+= profit
                jobs_done+= 1
                break
    return [jobs_done, maxProfit]


# Jobs= [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
# Jobs= [(1,2,100),(2,1,19),(3,2,27),(4,1,25),(5,1,15)]
# Jobs= [(1,3,2),(2,3,4),(3,3,3),(4,4,1),(5,4,10)]
Jobs= [(1,5,200),(2,3,180),(3,3,190),(4,2,300),(5,4,120),(6,2,100)]
n= len(Jobs)
print(JobScheduling(Jobs,n))

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] JobScheduling(int[][] Jobs, int n) {
        // Sort jobs by profit in descending order
        Arrays.sort(Jobs, (a, b) -> b[2] - a[2]);

        // It will return the job having max deadline among all jobs
        int max_deadline = 0;
        for (int[] job : Jobs) {
            max_deadline = Math.max(max_deadline, job[1]);
        }

        // '0-based' indexing so no need to add '1' like above
        int[] position = new int[max_deadline];
        Arrays.fill(position, -1);

        int jobs_done = 0, maxProfit = 0;

        // Now place the job with maximum profit as far as possible
        for (int[] job : Jobs) {
            int id = job[0], deadline = job[1], profit = job[2];
            for (int j = deadline - 1; j >= 0; j--) {  // '0-based' indexing so going till index '0'
                if (position[j] == -1) {
                    position[j] = id;
                    maxProfit += profit;
                    jobs_done += 1;
                    break;  // after you find any empty slot
                }
            }
        }

        return new int[]{jobs_done, maxProfit};
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
    vector<int> JobScheduling(vector<vector<int>>& Jobs, int n) {
        // Sort jobs by profit in descending order
        sort(Jobs.begin(), Jobs.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[2] > b[2];
        });

        // It will return the job having max deadline among all jobs
        int max_deadline = 0;
        for (const auto& job : Jobs) {
            max_deadline = max(max_deadline, job[1]);
        }

        // '0-based' indexing so no need to add '1' like above.
        vector<int> position(max_deadline, -1);

        int jobs_done = 0, maxProfit = 0;

        // Now place the job with maximum profit as far as possible
        for (const auto& job : Jobs) {
            int id = job[0], deadline = job[1], profit = job[2];
            for (int j = deadline - 1; j >= 0; j--) {  // '0-based' indexing so going till index '0'
                if (position[j] == -1) {
                    position[j] = id;
                    maxProfit += profit;
                    jobs_done += 1;
                    break;  // after you find any empty slot
                }
            }
        }

        return {jobs_done, maxProfit};
    }
};

"""
# python used function and methods
# https://www.geeksforgeeks.org/python-list-sort-method/
# https://www.askpython.com/python/built-in-methods/python-max-method
