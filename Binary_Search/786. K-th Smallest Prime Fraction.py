# used the similar 'heap' logic as :"378. Kth Smallest Element in a Sorted Matrix" .
# first put all the elements from where we can get all the minimum i.e starting indexes.

# time: O(n*logn) + O(k*logn)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        minHeap = []
        # first add all pair of index from which we can get all minimum fraction possible by poping those numbers.
        # smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        # numerator index should from the start of the arr and denominator index should be from the last of the array for minimum fraction.
        for i in range(n-1):   
            heapq.heappush(minHeap, (arr[i]/ arr[n-1], i, n-1))
        # now pop first 'k' elements. 
        for _ in range(k):
            _, i, j= heapq.heappop(minHeap)
            # next smaller may be arr[i]/ arr[j-1] or will be already in the heap. 
            # e.g: [1,2,3,5]  2nd min= (2,5) not (1,3) that's why we put all arr[i]/arr[n-1] at first.
            if j-1 >= 0:  
                heapq.heappush(minHeap, (arr[i]/ arr[j-1], i, j-1))  # not pushed (i+1, j) since this we get pushed automatically when 'i+1, j' will be poped.
        return [arr[i], arr[j]]   # last poped index will be our ans.


# Note: Inserting both (i, j- 1) and (i+ 1, j) will give ans because (i + 1, j) may already in heap before
# when we are adding 1st and last i.e (i , j - 1)
# e.g: say n = 5 . in heap = [(0, 4) , (1, 4) ....]
# suppose 1st (0, 4) i.e i = 0, j = 4 get poped and if we insert (i + 1, j) i.e (1, 4) then this will be duplication.

# So insert only (i , j- 1).
    

# Or take a visited set and insert both pair if not already visited.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        minHeap = []
        visited = set()
        # first add all pair of index from which we can get all minimum fraction possible by poping those numbers.
        # smallest fraction we will get arr[i]/arr[n-1] since array is sorted. 
        # numerator index should from the start of the arr and denominator index should be from the last of the array for minimum fraction.
        for i in range(n-1):   
            heapq.heappush(minHeap, (arr[i]/ arr[n-1], i, n-1))
            visited.add((i , n -1))
        # now pop first 'k' elements. 
        for _ in range(k):
            _, i, j= heapq.heappop(minHeap)
            # next smaller may be arr[i]/ arr[j-1] or will be already in the heap. 
            # e.g: [1,2,3,5]  2nd min= (2,5) not (1,3) that's why we put all arr[i]/arr[n-1] at first.
            if j-1 >= 0 and (i, j -1) not in visited:  
                heapq.heappush(minHeap, (arr[i]/ arr[j-1], i, j-1))  # not pushed (i+1, j) since this we get pushed automatically when 'i+1, j' will be poped.
                visited.add((i, j -1))
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (arr[i + 1]/ arr[j], i + 1, j))
                visited.add((i + 1, j))
        return [arr[i], arr[j]]   # last poped index will be our ans.


# using binary search.
# used the similar concept of "719. Find K-th Smallest Pair Distance".
# logic: first find the range in which our fraction can lie. 
# for possible fraction calculate the no of pair smaller than that and keep storing the largest fraction pair smaller than mid. 
# And if count of any 'mid' value== k: return that pair .
    
# vvi: Here we need to return simply when we will find the ans.So in while loop we will use 'start<=end'.
# note: while updating start and end , here we will make both equal to mid only because we are deaing in fraction and 
# max possible value is '1' only so we can't update start like 'mid+1' and end like 'mid -1'.

# time: O(NlogW), where N is array size, and W is the range size between the smallest and the largest fraction, in float number space.

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)

        def countLess(mid):
            cnt= 0
            j= 1  # will work as denominator
            p, q= 0, 1   # will store the largest fraction pair <= mid
            for i in range(n-1):  # 'i' will work as nominator and will go till 'n-2' 
                # move 'j' till you start getting fraction value <= mid.
                # after finding such 'j' then all number from 'n-j' will have fraction <= mid for curr 'i'.
                while j < n and arr[i]/arr[j] > mid:  # move 'j' till you start getting fraction value<= mid 
                    j+= 1
                # update p, q
                if j < n and p/q < arr[i]/ arr[j]:   # since we have to find the largest fraction <= mid so we are updating the value first time while loop break for any 'i'. 
                    p, q= arr[i], arr[j]                                                           # after this 'j' all will be smaller tahn current 'i'.
                cnt+= n- j   # all ele after 'j' will have fraction less than mid.
            return cnt, p, q

        # start, end= arr[0]/arr[n-1], 1  # can do like this also since we are sure that min can be this much only. And for max it will nearly equal to 1 but eaxctly '1'.
        start, end= 0, 1
        while start <= end:  # end -start>=0
            mid= start + (end- start)/2
            cnt, p, q= countLess(mid)
            if cnt== k:
                return [p, q]
            elif cnt > k:
                end= mid
            elif cnt < k:
                start= mid

