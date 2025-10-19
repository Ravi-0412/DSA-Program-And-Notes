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

public class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        // prices will store the actual ans
        int[] prices = new int[n];
        Arrays.fill(prices, Integer.MAX_VALUE);
        prices[src] = 0;  // make the source price as 0
        
        // we have to run loop k+1 time to get the optimal ans as every edge should be relaxed k+1 times for k stops
        for (int i = 0; i <= k; i++) {
            // copying like this (changing the value at an index) will update the values in new array also
            // when we will update the values in original array or vice versa( it creates the reference for the same object). 
            // But we have change the value only in tempPrices for each edge 
            
            int[] tempPrices = prices.clone();  // this create another copy of the original array
            
            // we will update the current iteration ans in the tempPrices seeing the previous optimise ans(prices), so we copied 
            for (int[] flight : flights) {
                int s = flight[0], d = flight[1], p = flight[2];
                if (prices[s] == Integer.MAX_VALUE) {
                    // it means that the stopage s(source) is not reachable till ith stop
                    // it basically means that 'd' is not connected to the any node that has been updated(relaxed) till now
                    continue;
                }
                if (prices[s] + p < tempPrices[d]) {
                    tempPrices[d] = prices[s] + p;
                }
            }
            // prices = tempPrices;  // here this will also work as we are not updating prices array anywhere            
            prices = tempPrices;  // this will always work fine 
        }
        return (prices[dst] == Integer.MAX_VALUE) ? -1 : prices[dst];
    }
}

"""
# C++ Code 
"""
#include <vector>
#include <climits>  // For INT_MAX
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // prices will store the actual ans
        vector<int> prices(n, INT_MAX);
        prices[src] = 0;  // make the source price as 0
        
        // we have to run loop k+1 time to get the optimal ans as every edge should be relaxed k+1 times for k stops
        for (int i = 0; i <= k; i++) {
            // copying like this (changing the value at an index) will update the values in new array also
            // when we will update the values in original array or vice versa( it creates the reference for the same object). 
            // But we have change the value only in tempPrices for each edge 
            
            vector<int> tempPrices = prices;  // this create another copy of the original array
            
            // we will update the current iteration ans in the tempPrices seeing the previous optimise ans(prices), so we copied 
            for (auto& flight : flights) {
                int s = flight[0], d = flight[1], p = flight[2];
                if (prices[s] == INT_MAX) {
                    // it means that the stopage s(source) is not reachable till ith stop
                    // it basically means that 'd' is not connected to the any node that has been updated(relaxed) till now
                    continue;
                }
                if (prices[s] + p < tempPrices[d]) {
                    tempPrices[d] = prices[s] + p;
                }
            }
            // prices = tempPrices;  // here this will also work as we are not updating prices array anywhere            
            prices = tempPrices;  // this will always work fine 
        }
        return (prices[dst] == INT_MAX) ? -1 : prices[dst];
    }
};

"""


# Method 2: 
# use the logic of Dijkastra, inserting 'stops' also in heap.

# Mistakes 
# a) 
"""
it fails for case : 
n = 4, flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src = 0, dst = 3, k = 1

Why  ?
Think of situatio like : you poped one node having minimum cost & marked visited.
Later you try to go through that node then stop may increase & you may miss some paths resulting in no answer.
Just dry run Above example.

Note: Here only cost is not a factor, no_stop is also one of the factor.
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)  # converting into adjacency list 
        for u,v,p in flights:
            edges[u].append((v,p))
        # price = ['inf']*n
        minHeap = [(0, src, 0)]   #[price, city, no_stops]
        visited = set()
        while minHeap:
            p1, c1, no_stops = heapq.heappop(minHeap)
            if c1 in visited:
                continue
            if c1 == dst:
                return p1
            visited.add(c1)
            if no_stops <= k:
                for c2, p2 in edges[c1]:
                    if c2 not in visited :
                        heapq.heappush(minHeap, (p1 + p2, c2, no_stops + 1))
        return -1


# b) How to solve above issue ? 
# Just remove visited set & try all approaches, this will work for sure but result in TLE.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)  # converting into adjacency list 
        for u,v,p in flights:
            edges[u].append((v,p))
        minHeap = [(0, src, 0)]   #[price, city, no_stops]
        while minHeap:
            p1, c1, no_stops = heapq.heappop(minHeap)
            if c1 == dst:
                return p1
            if no_stops <= k:
                for c2, p2 in edges[c1]:
                    heapq.heappush(minHeap, (p1 + p2, c2, no_stops + 1))
        return -1

# Correct & optimal way
"""
Instead of simply putting node in visited set
If we keepy track of no_stops like in how many stops , we have reached this node.
We can keep on adding the same node if we come through less stop than before. 
"""

from collections import defaultdict
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, price in flights:
            edges[u].append((v, price))

        # (total_price, current_city, stops_so_far)
        minHeap = [(0, src, 0)]
        # Keep track of the minimum stops to a city
        visited = dict()

        while minHeap:
            cost, city, stops = heapq.heappop(minHeap)
            # Reached destination
            if city == dst:
                return cost
                
            # If we already visited this city with fewer stops, skip
            if city in visited and visited[city] <= stops:
                continue
            visited[city] = stops
            
            if stops <= k:
                for neighbor, price in edges[city]:
                    heapq.heappush(minHeap, (cost + price, neighbor, stops + 1))
        return -1

# Java
"""
import java.util.*;

class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int[] flight : flights) {
            edges.computeIfAbsent(flight[0], x -> new ArrayList<>()).add(new int[]{flight[1], flight[2]});
        }

        // (total_price, current_city, stops_so_far)
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{0, src, 0});

        // Keep track of the minimum stops to a city
        Map<Integer, Integer> visited = new HashMap<>();

        while (!minHeap.isEmpty()) {
            int[] curr = minHeap.poll();
            int cost = curr[0], city = curr[1], stops = curr[2];

            // Reached destination
            if (city == dst) return cost;

            // If we already visited this city with fewer stops, skip
            if (visited.containsKey(city) && visited.get(city) <= stops) continue;
            visited.put(city, stops);

            if (stops <= k) {
                if (edges.containsKey(city)) {
                    for (int[] neighbor : edges.get(city)) {
                        int nextCity = neighbor[0], price = neighbor[1];
                        minHeap.offer(new int[]{cost + price, nextCity, stops + 1});
                    }
                }
            }
        }

        return -1;
    }
}
"""


# C++ 
"""
#include <vector>
#include <unordered_map>
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        unordered_map<int, vector<pair<int, int>>> edges;
        for (auto& flight : flights) {
            edges[flight[0]].emplace_back(flight[1], flight[2]);
        }

        // (total_price, current_city, stops_so_far)
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> minHeap;
        minHeap.emplace(0, src, 0);

        // Keep track of the minimum stops to a city
        unordered_map<int, int> visited;

        while (!minHeap.empty()) {
            auto [cost, city, stops] = minHeap.top();
            minHeap.pop();

            // Reached destination
            if (city == dst) return cost;

            // If we already visited this city with fewer stops, skip
            if (visited.count(city) && visited[city] <= stops) continue;
            visited[city] = stops;

            if (stops <= k) {
                for (auto& [neighbor, price] : edges[city]) {
                    minHeap.emplace(cost + price, neighbor, stops + 1);
                }
            }
        }

        return -1;
    }
};
"""
