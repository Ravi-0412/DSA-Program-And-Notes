# Method 1:

# Note: Here one interval must start after end of another interval.

'''
We need to merge the intervals into the minimum number of intervals such that no two intervals overlap.
To do this, we can sort the intervals based on their start times and then iterate through them, merging overlapping intervals as we go.

We will add the non-overlapped intervals into an result arry , which we are going to return at the last. 

Initially, the first array will be added to the result array.

Then onwards, we will compare the endTime of the last interval in the result array with the startTime of the current interval.
If the startTime of the current interval is greater than the endTime of the last interval in the result array, it means the intervals are non-overlapping, and we can add the current interval to the result array.

Also, if the startime is equal to, or less than the endtime of the previous, then it means they are overlapping, which means we cant add the current interval into the result.

But, here's a catch, which many might miss - don't forget to update the endtime of the previous intervals with the maximum of current endtTime and previous endTime.
Agar overlap kar rha then start time to pichle wale ka hi rhega but end me 'dono ka maximum ending time' ho jayega.

After the iteration, we will return the result array which will contain the merged intervals.
'''

# TIME COMPLEXITY :

'''
-> Sorting the array = 0(nlogn)
-> Iterating through the array = O(n)
-> Overall time complexity = O(nlogn)
'''

# SPACE COMPLEXITY :

'''
-> O(n) for the result array.
-> O(1) for the variables used.
-> Overall space complexity = O(n)
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  
        # intervals.sort(key= lambda i: i[0])   # 'i': intervals, i[0] index value on which we want to sort
        output= [intervals[0]]  # to handle the edge case and make comparison easy
        for start, end in intervals[1:]:
            # check if ending of last added interval is >= than starting of the currnet one 
            if output[-1][1] >= start: 
		# i.e if overlapping then merge , make end of last added one max(end of last addded, end)
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else:
		# If not overlapping then add directly 
                output.append([start, end])  # just the cur interval only.
        return output

# Java code.
"""
class Solution {
    public List<List<Integer>> merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        // intervals.sort(key= lambda i: i[0])   // 'i': intervals, i[0] index value on which we want to sort

        List<List<Integer>> output = new ArrayList<>();
        output.add(Arrays.asList(intervals[0][0], intervals[0][1])); 
        // to handle the edge case and make comparison easy

        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0], end = intervals[i][1];
            // check if ending of last added interval is >= than starting of the current one 
            if (output.get(output.size() - 1).get(1) >= start) {
                // i.e if overlapping then merge, make end of last added one max(end of last added, end)
                int updatedEnd = Math.max(output.get(output.size() - 1).get(1), end);
                output.get(output.size() - 1).set(1, updatedEnd);  // [[1,4],[2,3]] = [[1,4]]
            } else {
                // If not overlapping then add directly 
                output.add(Arrays.asList(start, end));  // just the curr interval only.
            }
        }

        return output;
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
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());  // sort based on starting time

        vector<vector<int>> output;
        output.push_back(intervals[0]);  // to handle the edge case and make comparison easy

        for (int i = 1; i < intervals.size(); i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            // check if ending of last added interval is >= than starting of the current one 
            if (output.back()[1] >= start) {
                // i.e if overlapping then merge, make end of last added one max(end of last added, end)
                output.back()[1] = max(output.back()[1], end);
            } else {
                // If not overlapping then add directly 
                output.push_back({start, end});  // just the current interval only
            }
        }

        return output;
    }
};

"""

# Follow ups:
"""
What if the intervals are already sorted by end time?
Answer: You would still need to sort by start time or process them in reverse (right-to-left). 
Sorting by start time is the standard "sweep-line" approach.
"""
