# smallest ele will at the start only but can form from any combination.
# for any ele we will pop there are two possibility and while incr the pointers we can get the duplicates also.
# like we can get same value as (i, j+1) from (i+1, j)  and vice versa also. so we will get wrong ans.
#  so we are marking the ele already visited
# time: O(k*log(m+n))

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        visited= set()
        visited.add((0,0))
        heap, ans= [], []
        heapq.heappush(heap,(nums1[0]+ nums2[0],0,0))

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