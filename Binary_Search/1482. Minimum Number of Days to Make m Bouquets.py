# just same logic as "alllocate minimum no of pages".
# Difference between both Q: Here we can excatly allocate 'k' no of adjacent books to each student,
# instead of allocating any no of books if no of pages in that book is <= max_page_allowed.(i.e mid) .

# And we must allocate to at least 'm' students.

# our ans will lie in range [min(bloomDay), max(bloomDay)]. At least we will have to wait till min(bloomDay) and max can go upto max(bloomDay)

# time: O(n*log(max(bloomDay)))
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):  # not possible 
            return -1
        start, end= min(bloomDay), max(bloomDay) 
        while start < end:
            mid= start + (end- start)//2
            if self.isPossible(bloomDay, mid, m , k):
                end= mid 
            else:
                start= mid + 1
        return start 

    def isPossible(self, arr, mid, m , k):
        bouquet, count= 0, 0
        for i in range(len(arr)):
            if arr[i] > mid:
                count= 0   # we have start searching from '0' only
            else:
                count+= 1
            if count== k:  # means we have found 'k' adjacent flower so we can make one bouquet.
                bouquet+= 1
                count= 0  # to chekc for next possible bouquet.
        return bouquet >= m


# other way we can do is:
# 1) jst sort the array 
# 2) apply binaty search on range ' [min(bloomDay), max(bloomDay)]' .
# 3) Check the last insertion point of mid in sorted array
# if insertion_point >= m * k then means for this 'mid' , it is possible to get all 'm' boquet.
# Reason: it means that we can get >= m * k flowers at days == mid.