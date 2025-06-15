# Method 1: 

# logic: totally same as Bellman ford
# just relax the every edge in each iteration seeing the previous modified array
# relaxing edge one time will give the optimal ans till one stop and so on
# time: O(n*k) for this q

# Bellman ford: time- O(N*E) as each edge will get relaxed 'n' times, E= no of edges, N= no of vertices
# and we run the loop for n-1 times it will give the optimal ans from src to each node 
# and for checking the negative weight cycle, just run the loop n times nad compare the value of any node with previous one
# if it is less then it means cycle 

# working: phla bar run karne pe jo edge source se attach(directly connected) hoga uska optimal ans milega.
# 2nd time jo node abhi tak reached hua h uske help se remaining connected edge 
# optimise hoga + already optimise edge also if they are connected to any viisted node till now. 
# isi tarah se ye repeat hota rhega or har bar har edge optimise hota rhega agar wo connected hoga to
# Note: we will optimise seeing the previous iteration result not the current one 


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
            # we will update the current iteration ans in the tempPrices seeing the previous optimise ans(prices), so we copied 

            for s,d,p in flights:  # s: source, d: destination, p: prices
                if prices[s]== 'inf':  # it means that the stopage s(source) is not reachable till ith stop
                        # it basically means that 'd' is not connected to the any node that has been updated(relaxed) till now
                    continue
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d]= prices[s] + p
            # prices= tempPrices  # here this will also work as we are not updating prices array anywhere            
            prices= tempPrices.copy()  # this will always work fine 
        return -1 if prices[dst]== 'inf' else prices[dst]

# Java Code 
"""
import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] prices = new int[n];  // this will store the actual ans
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;   // make the source price as 0

        // we have to run loop k+1 time to get the optimal ans as every edge should be relaxed k+1 times for k stops
        for (int i = 0; i <= k; i++) {
            // copying like this (changing the value at an index) will update the values in new array also
            // when we will update the values in original array or vice versa( it creates the reference for the same object). 
            // But we have to change the value only in tempPrices for each edge 
            int[] tempPrices = prices.clone();  // this create another copy of the original array

            // we will update the current iteration ans in the tempPrices seeing the previous optimise ans(prices), so we copied 
            for (int[] flight : flights) {
                int s = flight[0], d = flight[1], p = flight[2];
                if (prices[s] == Integer.MAX_VALUE) {  // it means that the stopage s(source) is not reachable till ith stop
                    continue;
                }
                if (prices[s] + p < tempPrices[d]) {
                    tempPrices[d] = prices[s] + p;
                }
            }
            prices = tempPrices.clone();  // this will always work fine
        }
        return prices[dst] == Integer.MAX_VALUE ? -1 : prices[dst];
    }
}

"""
# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> prices(n, INT_MAX);  // this will store the actual ans
        prices[src] = 0;  // make the source price as 0

        // we have to run loop k+1 time to get the optimal ans as every edge should be relaxed k+1 times for k stops
        for (int i = 0; i <= k; ++i) {
            // copying like this (changing the value at an index) will update the values in new array also
            // when we will update the values in original array or vice versa( it creates the reference for the same object). 
            // But we have to change the value only in tempPrices for each edge 
            vector<int> tempPrices = prices;  // this create another copy of the original array

            // we will update the current iteration ans in the tempPrices seeing the previous optimise ans(prices), so we copied 
            for (auto& flight : flights) {
                int s = flight[0], d = flight[1], p = flight[2];
                if (prices[s] == INT_MAX) {  // it means that the stopage s(source) is not reachable till ith stop
                    continue;
                }
                if (prices[s] + p < tempPrices[d]) {
                    tempPrices[d] = prices[s] + p;
                }
            }
            prices = tempPrices;  // this will always work fine
        }
        return prices[dst] == INT_MAX ? -1 : prices[dst];
    }
};

"""