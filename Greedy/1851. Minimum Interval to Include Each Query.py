# sort both intervals and queries.
# why we are sorting both.
# if we sort both then both the intervals and query will be nearby .
# Time: O(nlogn + qlogq)
# Space:  O(n+q)
# where q = queries.size()

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap= []
        ans= {}  # since we have to store the ans to the queries index only and we are operatimng on sorted queries
        i= 0  # for ietrating over intervals
        for q in sorted(queries):
            # add all the intervals to whcih query can belong. \
            # it can only belong to any interval if starting time of that interval is <= the query
            while i < len(intervals)  and intervals[i][0] <= q:
                # get the start and end time of interval it belong
                s, e= intervals[i]
                # also inserting end time in case if the size of two intervals match then we will pop the intervals having less end time.
                heapq.heappush(minHeap, (e-s+1, e)) 
                i+= 1
            # now find out the minimum size interval to get the ans for the current query.

            # if no interval is added in minHeap or after poping if minHeap becomes empty then that query doesn't belong to any of the interval.
            # if the end time of interval is less than the query then that can't be the ans, so pop all such query.
            while minHeap and minHeap[0][1] < q :
                heapq.heappop(minHeap)
            # now we have found the ans so add the size of intervals if minHeap is not empty else '-1'.
            ans[q]= minHeap[0][0] if minHeap else -1  
        return [ans[q] for q in queries]   # inserting queries ans at their proper index


# also do by union find method in sheet(taken from discussion) latyeer