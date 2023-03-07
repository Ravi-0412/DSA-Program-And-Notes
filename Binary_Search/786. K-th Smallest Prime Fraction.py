# used the similar logic as :"378. Kth Smallest Element in a Sorted Matrix" of heap.
# first put all the elements from where we can get all the minimum i.e starting indexes.

# time: O(n*logn) + O(k*logn)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        minHeap = []
        # first add all pair of index from whcih we are dividing by 'n-1' index.
        # smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        # numerator index should from the start of the arr and denominator index should be from the last of the array for minimum fraction.
        for i in range(n-1):   
            heapq.heappush(minHeap, (arr[i]/ arr[n-1], i, n-1))
        # now pop first 'k' elements. 
        for _ in range(k):
            _, i, j= heapq.heappop(minHeap)
            if j-1 >= 0:  # next smaller may be arr[i]/ arr[j-1] or will be already in the heap
                heapq.heappush(minHeap, (arr[i]/ arr[j-1], i, j-1))
        return [arr[i], arr[j]]   # last poped index will be our ans.


# using binary search.
# used the similar concept of "719. Find K-th Smallest Pair Distance".
# logic: first find the range in which our fraction can lie. for possible fraction calculate the no of pair smaller than that and
#  keep storing the largest fraction pair smaller than mid. 
# And if count of any 'mid' value== k: retrun that pair
# vvi: Here we need to return simply when we will find the ans.So in while loop we will use 'start<=end'.
# note: while updating start and end , here we will make both equal to mid only because we are deaing in fraction and 
# max possible value is '1' only so we can't update start like 'mid+1' and end like 'mid -1'.

# time: O(NlogW), where N is array size, and W is the range size between the smallest and the largest fraction, in float number space.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)

        def countLess(mid):
            cnt= 0
            j= 0  # will work as denominator
            p, q= 0, 1   # will store the largest fraction pair smaller than mid
            for i in range(n):
                # move 'j' till you start getting fraction value<= mid.
                # after finding such 'j' then all number from 'n-j' will have fraction <= mid for curr 'i'.
                while j < n and arr[i]/arr[j] > mid:  # move 'j' till you start getting fraction value<= mid 
                    j+= 1
                # update p, q
                if j < n and p/q < arr[i]/ arr[j]:
                    p, q= arr[i], arr[j]
                cnt+= n- j   # all ele after 'j' will have fraction less than mid.
            return cnt, p, q

        start, end= 0, 1
        while start <= end:
            mid= start + (end- start)/2
            cnt, p, q= countLess(mid)
            if cnt== k:
                return [p, q]
            elif cnt > k:
                end= mid
            elif cnt < k:
                start= mid

