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
            if count>K1 and count< K2:  # this will be our one of the ans
                sum1+= temp