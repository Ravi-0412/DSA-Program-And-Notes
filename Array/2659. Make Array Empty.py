# used heap to find the minimum ele after each deletion but giving Tle in last few test cases.

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n= len(nums)
        q= collections.deque(nums)
        heap= nums.copy()
        heapq.heapify(heap)
        # print(q, heap)
        count= 0
        while q:
            if q[0]== heap[0]:
                q.popleft()
                heapq.heappop(heap)
            else:
                temp= q[0]
                q.popleft()
                q.append(temp)
            count+= 1   
        return count