# Brute force : O(k*n)

# Optiomised:

# range:
# 1) start: max(weights). if less than this then max package weight won't be get delivered.
# 2) end:   sum(weights). when we have to deliver all packages in a single day.

# just copy pasted the logic of 'Allocate minimum no of pages'.
# time: O(n* 2*logA), A= sum(weights) -max(weights).  space= O(n)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N, M= len(weights), days
        start, end= max(weights), sum(weights)
        while start< end:
            mid= start + (end-start)//2
            # if maximum weight capacity of the ship id 'mid' then is it possible to deliver in 'd' days ?
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
        return days <= M
    

# Other way, change in while loop condition
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        N, M= len(weights), days
        start, end= max(weights), sum(weights)
        while start <= end:
            mid = start + (end - start)//2
            # if maximum weight capacity of the ship id 'mid' then is it possible to deliver in 'd' days ?
            if self.IsValid(weights,N,M,mid):  # search for even more smaller but mid can be the ans also.
                end = mid - 1
            else:
                start= mid + 1
        return start

    def IsValid(self, A, N, M, max_cap):
        days, capacity= 1, 0
        for i in range(N):
            capacity += A[i]
            if capacity > max_cap: 
                days += 1
                capacity = A[i]
        return days <= M
