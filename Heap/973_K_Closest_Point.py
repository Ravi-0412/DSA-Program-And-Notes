# time: O(nlogk)
# just same logic as k closest points to x
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= []
        for i in range(len(points)):
            dist= math.sqrt((points[i][0]**2)+(points[i][1]**2))
            heapq.heappush(heap,(-1*dist,points[i]))
            if len(heap)>k:
                heapq.heappop(heap)
        ans= []
        for i in range(len(heap)):
            ans.append(heap[i][1])
        return ans

# better way of writing above code
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap= []
        for x,y in points:
            dist= sqrt(x**2 + y**2)
            heapq.heappush(heap,(-1*dist,x,y))
            if len(heap)>k:
                heapq.heappop(heap)
        return [(x,y) for (dist,x,y) in heap]


# try later by quicksort method 
# https://leetcode.com/problems/k-closest-points-to-origin/discuss/219442/Python-with-quicksort-algorithm
