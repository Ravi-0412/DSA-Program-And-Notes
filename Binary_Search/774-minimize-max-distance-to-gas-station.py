# logic:Similar logic like "Allocate minimum no of pages" but very good Q.
# Q asking : 'k' gas station add karne ke bad minimum distance kisi bhi gas station ke beech kitna ho sakta h.

# we can check for each posible ans(difference only) like if it is possible to keep all the stations with this 'diff' 
# by adding at most 'k' extra stations ??
# how to calculate the no of stations for 'diff'? (VVI)
# Ans: check for adjacent station difference and if it is greater than 'diff' means we have to put extra station between these two stations.
# But to find exactly how many extra stations we have to put to keep the max diff between adjacent station equal to 'diff' .
# and count+= (stations[i]- stations[i-1])//diff.
# e.g: if diff is greater than two times but less tahn three times then we need to put '2' station and so on. It's very practical to think.
# so we will add ceilig value.

# Raeson: Every adjacent gas staion can have max distance 'mid', so checking between every station.


# submitted on lintcode(LC premium).
# time: O(n* log(max(stations)))
class Solution:
    def minmax_gas_dist(self, stations: List[int], k: int) -> float:

        def isPossible(diff):  # kisi 2 station ka beech ka min distance 'd' chahiye to kya hm 'k' additional gas station add karke kar sakte h?
            count= 0
            for i in range(1, len(stations)):
                count+= (stations[i]- stations[i-1])//diff   # no of additional gas station required between these two to take the min diff <= 'diff'.
            return count <= k   # means it is possible to keep all the adjacent stations with max diff = diff by putting additional 'k' stations.

        delta= 1e-6   # mini diff can be this . Also given ans must within this only.
        start= 0  # nearly equal to '0'.
        end=   max(stations)  # max difference can be this at start
        while end- start > delta:
            mid= start + (end- start)/2
            if isPossible(mid):
                end= mid
            else:
                start= mid + delta
        return start
