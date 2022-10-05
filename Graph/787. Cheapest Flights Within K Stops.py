# logic: totally same as Bellman ford
# just relax the every edge in each iteration seeing the previous modified array
# relaxing edge one time will give the optimal ans till one stop and so on
# time: O(n*k) for this q

# Bellman ford: time- O(N*E) as each edge will get relaxed 'n' times, E= no of edges, N= no of vertices
# and we run the loop for n-1 times it will give the optimal ans from src to each node 
# and for checking the negative weight cycle, just run the loop n times nad compare the value of any node with previous one
# if it is less then it means cycle 


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices= ['inf']*n  # this will store the actual ans
        # store the cheapest price for each city after each stop
        prices[src]= 0   # make the source price as 0
        # we have to run loop k+1 time to get the optimal ans as every edge should be relaxed k+1 times for k stops

        # in every iteration, update the values in tempPrices seeing the previous optimal ans(prices) and
        # end of every iteration copy the updated tempPrices to prices, in this way 'prices' will store the optimal ans after every iteration 
        for i in range(k+1):
            # tempPrices= prices   # here i was making mistake again and again
            # copying like this (changing the value at an index) will update the values in new array also
            # when we will update the values in original array or vice versa( it creates the reference for the same object). 
            # But we have change the value only in tempPrices for each edge 

            tempPrices= prices.copy()    # this create another copy of the original array
            # temp will conatin the cheapest price till previous iteration as we have updated values in the temp only seeing the optimal ans (prices ) till previous one

            # here no need to make the adjacency list as we are not using any data structure for push and pop like heap 
            # here we have to relax every edge so we can do it by the given 'flights' matrix also directly
            for s,d,p in flights:  # s: source, d: destination, p: prices
                if prices[s]== 'inf':  # it means that the stopage s(source) is not reachable till ith stop
                                        # it basically means that 'd' is not connected to the any node that has been updated(relaxed) till now
                    continue
                if prices[s] + p< tempPrices[d]:
                    tempPrices[d]= prices[s] + p
            # prices= tempPrices  # here this will also work as we are not updating prices array anywhere 
            prices= tempPrices.copy()  # this will always work fine 
        return -1 if prices[dst]== 'inf' else prices[dst]

