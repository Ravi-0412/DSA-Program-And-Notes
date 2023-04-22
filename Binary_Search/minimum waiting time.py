
# time:O(n*logn)
class Solution:
    def minimumWaitTime(self, n, m, c, arr):
        
        def isPossible(mid):
            check= arr[0]
            bus, student, capacity= 1, 1, 1
            for i in range(1, n):
                if arr[i] - check <= mid:
                    student+= 1
                    capacity+= 1
                    if capacity > c :
                        check= arr[i]
                        bus+= 1
                        capacity= 1
                else:
                    check= arr[i]
                    bus+= 1
                    capacity= 1
                    
            # print(mid, bus)
            return bus <= m
                
        arr.sort()
        start, end= 0, max(arr)
        while start < end:
            mid= start + (end- start)//2
            if isPossible(mid):
                end= mid
            else:
                start= mid + 1
        return start