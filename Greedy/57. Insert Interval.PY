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
            if output[-1][1]>= start: # then merge , make end of last added one max(end of last addded, end)
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
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


