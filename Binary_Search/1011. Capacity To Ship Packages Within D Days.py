# just copy pasted the logic of 'Allocate minimum no of pages'.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N, M= len(weights), days
        start, end= max(weights), sum(weights)
        while start< end:
            mid= start + (end-start)//2
            if self.IsValid(weights,N,M,mid):  # search for even more smaller but mid can be the ans also.
                end= mid
            else:
                start= mid + 1
        return start

    def IsValid(self, A, N, M, max_cap):
        days, capacity= 1, 0
        for i in range(N):
            capacity+= A[i]
            if capacity > max_cap: 
                days+= 1
                capacity= A[i]
        return False if days > M else True