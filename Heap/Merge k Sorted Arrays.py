# Logic: 1st minimum can be 1st ele of any of the arrays.
# For getting this we can put 1st ele from all the arrays and select the minimum one.
# For this we can use min Heap.

# But next minimum can come from same array.
# So we need to put the array number with index as well so that we can insert next ele of this array in heap.

# time: O(n*logk), n= total no of elements

import heapq
class Solution:
    def mergeKArrays(self, arr, K):
        heap, ans= [], []
        # put the 1st ele of all the arrays in the heap with the array number and index
        for i in range(len(arr)):
            heapq.heappush(heap,(arr[i][0], i, 0))  # pushing the 1st ele of 'i'th arr
        
        # now to merge the array, just pop one ele from the heap and that will be minium at present
        while heap:
            val, arr_num, ind= heapq.heappop(heap)
            ans.append(val)
            # now add the next ele of the curr arr
            if ind+ 1 < len(arr[arr_num]):
                heapq.heappush(heap, (arr[arr_num][ind+1], arr_num, ind+1))
        return ans


# Related Q:
# 355. Design Twitter
