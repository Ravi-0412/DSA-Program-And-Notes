# just sort the intervals by the starting time and if they overlap then.
# logic: if start time of next intervals is <= end time of pre interval means they are overlapping i.e
#  current ongoing meeting has not ended till and next one has started=> intervals are overlapping so merge them.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # it will automatically sort the intervals based on strating val of intervals
        # intervals.sort(key= lambda i: i[0])   # 'i': intervals, i[0] index value on which we want to sort
        output= [intervals[0]]  # to handle the edge case and make comparison easy
        for start, end in intervals[1:]:
            # check if ending of last added interval is >= than starting of the currnet one
            if output[-1][1]>= start: # then merge , make end of last added one max(end of last addded, end)
                output[-1][1]= max(output[-1][1], end)    # [[1,4],[2,3]]= [[1,4]]
            else: 
                output.append([start, end])
        return output

