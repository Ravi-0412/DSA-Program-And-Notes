# Note: Here one interval must start after end of another interval.

# logic: if start time of next intervals is <= end time of pre interval means they are overlapping i.e
#  current ongoing meeting has not ended till and next one has started=> intervals are overlapping so merge them.

# 1st sort a/c to starting time and 
# Agar overlap kar rha then start time to pichle wale ka hi rhega but end me 'dono ka maximum ending time' ho jayega.

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  
        # intervals.sort(key= lambda i: i[0])   # 'i': intervals, i[0] index value on which we want to sort
        output= [intervals[0]]  # to handle the edge case and make comparison easy
        for start, end in intervals[1:]:
            # check if ending of last added interval is >= than starting of the currnet one
            if output[-1][1]>= start: # then merge , make end of last added one max(end of last addded, end)
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else: 
                output.append([start, end])  # just the cur interval only.
        return output


# java code.
# I tried to write in above form ,not able to write getting error.
# Have to ask someone
"""
class Solution {
	public int[][] merge(int[][] intervals) {
		if (intervals.length <= 1)
			return intervals;

		// Sort by ascending starting point
		Arrays.sort(intervals, (i1, i2) -> i1[0] -  i2[0]);
        // Arrays.sort(intervals); . It will give error because it don't sort automatically based on first parameter like python. So we have to pass a comparator function for sorting.
		List<int[]> result = new ArrayList<>();
		result.add(intervals[0]);
		for(int i = 1; i < intervals.length ; i ++) {
            int cap = result.length;
			if (result[cap - 1][0] <= intervals[i][1]) // Overlapping intervals, move the end if needed
				result[cap - 1][1] = Math.max(result[cap - 1][1], intervals[i][1]);
			else {                             // Disjoint intervals, add the new interval to the list
				result.add(intervals[i]);
			}
		}

		return result.toArray(new int[result.size()][]);
	}
}
"""

# other way of java code. correct one
"""
class Solution {
	public int[][] merge(int[][] intervals) {
		if (intervals.length <= 1)
			return intervals;

		// Sort by ascending starting point
		Arrays.sort(intervals, (i1, i2) -> i1[0], i2[0]);

		List<int[]> result = new ArrayList<>();
		int[] newInterval = intervals[0];
		result.add(newInterval);
		for (int[] interval : intervals) {
			if (interval[0] <= newInterval[1]) // Overlapping intervals, move the end if needed
				newInterval[1] = Math.max(newInterval[1], interval[1]);
			else {                             // Disjoint intervals, add the new interval to the list
				newInterval = interval;
				result.add(newInterval);
			}
		}

		return result.toArray(new int[result.size()][]);
	}
}

"""