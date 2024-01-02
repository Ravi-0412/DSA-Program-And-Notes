# for connecting n ropes with minimum cost
# you will have to pick the two smallest length always and connect them
# Because we have to choose the minimum weight to get minimum cost.

# so min heap will work prefectly
# after connecting two ropes put them again into the heap 
# since there can be other combination possible with two smaller length
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        if len(arr)==1:   # cost is zero
            return 0
        cost= 0
        heapq.heapify(arr)   # first make a min heap
        # now start taking the smaller two length and cal the cost
        while len(arr)>=2:   # go till length of rod becomes = 1
            first= heapq.heappop(arr)  # pick the 1st smallest ele
            sec= heapq.heappop(arr)    # pick the 1st smallest ele
            curr_min= first+sec        # cost of conne the curr two rod of smaller length
            cost+= curr_min            # update the cost
            heapq.heappush(arr,curr_min)    # now push the cost of two picked one into heap 
                                            # as we have to connect all the rods into one connected rod so put the
                                            # connected one so that other rod also get connected to this one till the form one connected rod
        return cost




