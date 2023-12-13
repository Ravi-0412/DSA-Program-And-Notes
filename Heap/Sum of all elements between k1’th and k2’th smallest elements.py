import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        heapq.heapify(A)  # will make a min heap
        count= 0
        sum1= 0
        while(len(A)):
            temp= heapq.heappop(A)
            count+= 1
            if count== K2:  
                return sum1
            if count > K1 and count < K2:  # this will be our one of the ans
                sum1+= temp


# using maxHEap
import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        heap= []
        for i in range(N):
            heapq.heappush(heap, -1*A[i])
            if len(heap)> K2-1:
                heapq.heappop(heap)
        ans= 0
        while heap:
            if len(heap)== K1: # because after poping in above 'for' it may reach to 'k1' also
                return ans
            temp = -1*heapq.heappop(heap)
            ans+= temp