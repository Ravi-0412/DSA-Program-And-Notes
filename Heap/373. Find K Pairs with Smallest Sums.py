# smallest ele will at the start only so at start we will push in heap :((nums1[0]+ nums2[0],0,0)).

# When we will pop any ele say at index (i, j) then next minimum we will get at (i+1, j) or (j+1, i) only.
# Since there are two possibility we can get same index from other way also.
# e.g: (2,2) -> (1,2) or (2, 1) so we will use visited set to keop track of visited indices.

# 

#  so we are marking the ele already visited
# time: O(k*log(m+n))

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited= set()
        visited.add((0,0))
        heap, ans= [], []
        heapq.heappush(heap,(nums1[0]+ nums2[0],0,0))   # (sum, i, j)  # i, j index of nums1 and nums2.

        while len(ans) < k and heap:
            sum,i,j= heapq.heappop(heap)
            ans.append([nums1[i],nums2[j]])
            if j+1 < len(nums2) and (i,j+1) not in visited:
                visited.add((i,j+1))
                heapq.heappush(heap,(nums1[i]+ nums2[j+1],i,j+1))
            if i+1 < len(nums1) and (i+1,j) not in visited:
                visited.add((i+1,j))
                heapq.heappush(heap,(nums1[i+1]+ nums2[j], i+1, j))

        return ans