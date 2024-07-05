# Logic: for each query find all intervals we can consider and then take interval having minimum range.
# for taking minimum among all possible we can use minHeap.
# for this we can sort both the intervals and query in ascending order.

# Time: O(nlogn + qlogq)
# Space:  O(n+q)
# where q = queries.size()

import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap= []
        queries = [[queries[i], i] for i in range(len(queries))]   # we need to keep track of index also 
        queries.sort()
        ans= [0]*len(queries)  # since we have to store the ans to the queries index only and we are operatimng on sorted queries
        i= 0  # for ietrating over intervals
        for q in queries:
            query , ind = q[0], q[1]
            # add all the intervals to which this query can belong.
            # it can only belong to any interval if starting time of that interval is <= the query
            while i < len(intervals)  and intervals[i][0] <= query:
                # get the start and end time of interval it belong
                s, e= intervals[i]
                # also inserting end time to remove the invalid intervals later whose end time will be less than the current query.
                heapq.heappush(minHeap, (e - s + 1, e)) 
                i+= 1
            # now find out the minimum size interval to get the ans for the current query.
            # Before this remove the intervals whose end time is less than the current query.
            while minHeap and minHeap[0][1] < query :
                heapq.heappop(minHeap)
            # now we have found the ans so add the size of intervals if minHeap is not empty else '-1'.
            ans[ind] = minHeap[0][0] if minHeap else -1  
        return ans


# Java
"""
class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        int[][] sortedQueries = new int[queries.length][2];
        for (int i = 0; i < queries.length; i++) {
            sortedQueries[i][0] = queries[i];
            sortedQueries[i][1] = i;
        }
        Arrays.sort(sortedQueries, (a, b) -> a[0] - b[0]);

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int[] result = new int[queries.length];
        Arrays.fill(result, -1);

        int i = 0; // index for intervals
        for (int[] q : sortedQueries) {
            int query = q[0], ind = q[1];

            // Add all intervals that can include this query
            while (i < intervals.length && intervals[i][0] <= query) {
                int start = intervals[i][0];
                int end = intervals[i][1];
                minHeap.offer(new int[]{end - start + 1, end});
                i++;
            }

            // Remove intervals that cannot include this query
            while (!minHeap.isEmpty() && minHeap.peek()[1] < query) {
                minHeap.poll();
            }

            // Get the smallest interval that can include this query
            if (!minHeap.isEmpty()) {
                result[ind] = minHeap.peek()[0];
            }
        }
        return result;
    }
}
"""

# also do by union find method in sheet(taken from discussion) later