# Method 1: add newInterval into intervals.
# After that question reduces to 'Merge overalpping intervals'.

# Time: O(n*logn)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        output= [intervals[0]]  # to handle the edge case and make comparison easy
        for start, end in intervals[1:]:
            # check if ending of last added interval is >= than starting of the currnet one
            if output[-1][1] >= start: # then merge , make end of last added one max(end of last addded, end)
                output[-1][1] = max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else: 
                output.append([start, end])
        return output

# Method 2:
# Using 'insort' method of 'bisect' module.
# insort(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, 
# if the element is already present in the list, the element is inserted at the rightmost possible position. 

# Do insertion in O(logn).

# Note: 'bisect' module function works only on sorted array.

# Time: O(logn + n) => O(n) only

# Read about 'bisect' module:
# https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/

import bisect
class Solution(object):
    def insert(self, intervals, newInterval):
        bisect.insort(intervals, newInterval)
        output= [intervals[0]]  # to handle the edge case and make comparison easy
        for start, end in intervals[1:]:
            # check with last added one.
            # if overlapping then merge i.e make end of last added one max(end of last addded, end)
            if output[-1][1] >= start:
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else: 
                # if not overlapping then simply add into the ans
                output.append([start, end])
        return output

# Method 3:
# Time: O(n)
# Just check all interval with 'newInterval' whether that will go right/left of newInterval OR
# they will overlap.

# Store left and right in separate 2d arrays and last
# insert updated 'newInetrval' values and return .

class Solution:
    def insert(self, intervals, newInterval):
        # Constant to help us access start point and end point of interval
        START, END = 0, 1
        s, e = newInterval[START], newInterval[END]
        left, right = [], []
        for cur_interval in intervals:
            if cur_interval[END] < s:
                # current interval is on the left-hand side of newInterval
                left += [ cur_interval ]
            elif cur_interval[START] > e:
                # current interval is on the right-hand side of newInterval
                right += [ cur_interval ]  
            else:
                # current interval has overlap with newInterval
                # merge and update boundary
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])   
        return left + [ [s, e] ] + right    


# Java . A lot of new java things to learn from this code.
"""
// Method 1:
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        
        // Add the new interval to the list of intervals
        List<int[]> intervalsList = new ArrayList<>(Arrays.asList(intervals));
        intervalsList.add(newInterval);
        
        // Sort intervals based on the starting times
        intervalsList.sort((a, b) -> a[0] - b[0]);

        // Initialize the first interval
        int[] currentInterval = intervalsList.get(0);
        result.add(currentInterval);

        for (int[] interval : intervalsList) {
            if (currentInterval[1] >= interval[0]) { // Merge intervals
                currentInterval[1] = Math.max(currentInterval[1], interval[1]);
            } else { // Add non-overlapping interval
                currentInterval = interval;
                result.add(currentInterval);
            }
        }

        return result.toArray(new int[result.size()][]);
    }
}

// If you want to do without converting into list .
// Then first you have to copy the given intervals and will have to make a new interval 2d- array of required size.

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        
        // Add the new interval to the array of intervals
        int[][] allIntervals = Arrays.copyOf(intervals, intervals.length + 1);
        allIntervals[intervals.length] = newInterval;
        
        // Sort intervals based on the starting times
        Arrays.sort(allIntervals, (a, b) -> a[0] - b[0]);

        // Initialize the first interval
        int[] currentInterval = allIntervals[0];

        for (int i = 1; i < allIntervals.length; i++) {
            int[] interval = allIntervals[i];
            if (currentInterval[1] >= interval[0]) { // Merge intervals
                currentInterval[1] = Math.max(currentInterval[1], interval[1]);
            } else {
                // No overlap, add the current interval to the result and update the current interval
                result.add(currentInterval);
                currentInterval = interval;
            }
        }

        // Add the last interval
        result.add(currentInterval);

        return result.toArray(new int[result.size()][]);
    }
}


// Method 2:

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // Create a list from the intervals array and add the new interval
        List<int[]> intervalList = new ArrayList<>(Arrays.asList(intervals));
        
        // Find the correct position to insert the new interval
        int pos = 0;
        while (pos < intervalList.size() && intervalList.get(pos)[0] < newInterval[0]) {
            pos++;
        }
        intervalList.add(pos, newInterval);

        // Create the output list and add the first interval
        List<int[]> output = new ArrayList<>();
        output.add(intervalList.get(0));

        // Merge intervals
        for (int i = 1; i < intervalList.size(); i++) {
            int[] currentInterval = intervalList.get(i);
            int[] lastInterval = output.get(output.size() - 1);
            
            if (lastInterval[1] >= currentInterval[0]) {
                // If overlapping, merge the intervals
                lastInterval[1] = Math.max(lastInterval[1], currentInterval[1]);
            } else {
                // If not overlapping, add the current interval to the output list
                output.add(currentInterval);
            }
        }

        // Convert the output list to a 2D array and return
        return output.toArray(new int[output.size()][]);
    }
}


// Can find the proper insert position using binary search also.
class Solution {
    public int findInsertionPoint(List<int[]> intervals, int[] newInterval) {
        int left = 0;
        int right = intervals.size() - 1;
        int targetStart = newInterval[0];

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int[] currentInterval = intervals.get(mid);
            int currentStart = currentInterval[0];

            if (currentStart == targetStart) {
                // Found an exact match, insert after this interval
                return mid + 1;
            } else if (currentStart < targetStart) {
                // Move to the right half
                left = mid + 1;
            } else {
                // Move to the left half
                right = mid - 1;
            }
        }

        // If the target is not found, return the insertion point
        return left;
    }
}

// or can use binary search inbuilt method also.

// modified code using binary search

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> intervalList = new ArrayList<>(Arrays.asList(intervals));
        
        // Find the correct insertion point using binary search
        int pos = Collections.binarySearch(intervalList, newInterval, (a, b) -> a[0] - b[0]);
        
        // If the position is negative, convert it to the insertion point
        if (pos < 0) {
            pos = -(pos + 1);
        }
        
        intervalList.add(pos, newInterval);

        // Create the output list and add the first interval
        List<int[]> output = new ArrayList<>();
        output.add(intervalList.get(0));

        // Merge intervals
        for (int i = 1; i < intervalList.size(); i++) {
            int[] currentInterval = intervalList.get(i);
            int[] lastInterval = output.get(output.size() - 1);
            
            if (lastInterval[1] >= currentInterval[0]) {
                // If overlapping, merge the intervals
                lastInterval[1] = Math.max(lastInterval[1], currentInterval[1]);
            } else {
                // If not overlapping, add the current interval to the output list
                output.add(currentInterval);
            }
        }

        // Convert the output list to a 2D array and return
        return output.toArray(new int[output.size()][]);
    }
}




// Method 3:
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        // Constants to help access the start and end points of intervals
        final int START = 0, END = 1;
        int s = newInterval[START], e = newInterval[END];
        List<int[]> left = new ArrayList<>();
        List<int[]> right = new ArrayList<>();

        for (int[] interval : intervals) {
            if (interval[END] < s) {
                // Current interval is on the left-hand side of newInterval
                left.add(interval);
            } else if (interval[START] > e) {
                // Current interval is on the right-hand side of newInterval
                right.add(interval);
            } else {
                // Current interval has overlap with newInterval
                // Merge and update boundaries
                s = Math.min(s, interval[START]);
                e = Math.max(e, interval[END]);
            }
        }

        // Merge the intervals
        int[][] result = new int[left.size() + 1 + right.size()][2];
        int index = 0;
        for (int[] interval : left) {
            result[index++] = interval;
        }
        result[index++] = new int[]{s, e};
        for (int[] interval : right) {
            result[index++] = interval;
        }

        return result;
    }
}

"""