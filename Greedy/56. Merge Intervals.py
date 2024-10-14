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
            if output[-1][1]>= start: 
		# i.e if overlapping then merge , make end of last added one max(end of last addded, end)
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else:
		# If not overlapping then add directly 
                output.append([start, end])  # just the cur interval only.
        return output

# Java code.

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
