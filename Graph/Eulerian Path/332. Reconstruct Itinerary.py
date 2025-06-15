# Logic: Just we have to print eulerian path starting from source.

"""
# Eulerian path: 
Eulerian Path is a path in a graph that visits every edge exactly once.
 Eulerian Circuit : is an Eulerian Path that starts and ends on the same vertex. 

Eulerian Cycle: An undirected graph has Eulerian cycle if following two conditions are true. 

1)All vertices with non-zero degree are connected. 
We don’t care about vertices with zero degree because they don’t belong to Eulerian Cycle or Path (we only consider all edges). 
2) All vertices have even degree.
Eulerian Path: An undirected graph has Eulerian Path if following two conditions are true. 

1) Same as condition (a) for Eulerian Cycle.
2) If zero or two vertices have odd degree and all other vertices have even degree. 
Note that only one vertex with odd degree is not possible in an undirected graph 
(sum of all degrees is always even in an undirected graph)

Note : that a graph with no edges is considered Eulerian because there are no edges to traverse.

How does this work? 
In Eulerian path, each time we visit a vertex v, we walk through two unvisited edges 
with one end point as v. Therefore, all middle vertices in Eulerian Path must have even degree. 
For Eulerian Cycle, any vertex can be middle vertex, therefore all vertices must have even degree.
"""

# Logic: All the airports are vertices and tickets are directed edges. Then all these tickets form a directed graph.
# The graph must be Eulerian since we know that a Eulerian path exists.
# Thus, start from "JFK", we can apply the Hierholzer's algorithm to find a Eulerian path in the graph which is a valid reconstruction.



# method 1: 
# using dfs
# time: O(ElogE +(V+E))= O(ElogE)
# space: O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dept_to_dest= collections.defaultdict(list)
        # to get the edges in ascending order just sort the edges in descending order
        # now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first 
        # so we can take the last one just by poping and that will be lexographically small.
        for dept,dest in sorted(tickets,reverse= True):
            dept_to_dest[dept].append(dest)
        route= []
        
        def dfs(airport):
            while dept_to_dest[airport]:  # go till it get stuck and traverse back
                dfs(dept_to_dest[airport].pop())  # it will always take the path with less lexographical order in case of more than one path
            route.append(airport)  # if got stuck then append it to the ans
        
        dfs('JFK')
        return route[::-1]


# Java
"""
import java.util.*;

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, Deque<String>> deptToDest = new HashMap<>();
        
        // to get the edges in ascending order just sort the edges in descending order
        // now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first 
        // so we can take the last one just by poping and that will be lexographically small.
        tickets.sort((a, b) -> b.get(1).compareTo(a.get(1)));
        for (List<String> ticket : tickets) {
            deptToDest
                .computeIfAbsent(ticket.get(0), k -> new ArrayDeque<>())
                .addLast(ticket.get(1));
        }

        List<String> route = new ArrayList<>();

        dfs("JFK", deptToDest, route);

        Collections.reverse(route); // reverse to get correct order
        return route;
    }

    // go till it get stuck and traverse back
    private void dfs(String airport, Map<String, Deque<String>> deptToDest, List<String> route) {
        while (deptToDest.containsKey(airport) && !deptToDest.get(airport).isEmpty()) {
            // it will always take the path with less lexographical order in case of more than one path
            dfs(deptToDest.get(airport).pollLast());
        }
        // if got stuck then append it to the ans
        route.add(airport);
    }
}


"""

# C++
"""
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <deque>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> route;

    void dfs(string airport, unordered_map<string, deque<string>>& deptToDest) {
        // go till it get stuck and traverse back
        while (!deptToDest[airport].empty()) {
            // it will always take the path with less lexographical order in case of more than one path
            string next = deptToDest[airport].back();
            deptToDest[airport].pop_back();
            dfs(next, deptToDest);
        }
        // if got stuck then append it to the ans
        route.push_back(airport);
    }

    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, deque<string>> deptToDest;

        // to get the edges in ascending order just sort the edges in descending order
        // now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first 
        // so we can take the last one just by popping and that will be lexographically small.
        sort(tickets.rbegin(), tickets.rend());
        for (auto& ticket : tickets) {
            deptToDest[ticket[0]].push_back(ticket[1]);
        }

        dfs("JFK", deptToDest);

        reverse(route.begin(), route.end()); // reverse to get correct order
        return route;
    }
};


"""

# method 2: 
# converted the above code into iterative form
# time: O(ElogE +(V+E))= O(ElogE)
# space: O(E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dept_to_dest= collections.defaultdict(list)
        # to get the edges in ascending order just sort the edges in descending order
        # now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first so we can take the last one just by poping 
        for dept,dest in sorted(tickets,reverse= True):  # will get sorted according to the 1st item, if tie then according to the 2nd item
            dept_to_dest[dept].append(dest)
        stack,ans= [],[]
        stack.append('JFK')
        while stack:
            while dept_to_dest[stack[-1]]:
                dest= dept_to_dest[stack[-1]].pop()  # if more than two paths are possible then it will take the path with lesser lexographic order 
                stack.append(dest)
            # when you get stuck then pop and add to the ans
            ans.append(stack.pop())
        return ans[::-1]
    

# Java
"""
import java.util.*;

class Solution {
    public List<String> findItinerary(List<List<String>> tickets) {
        Map<String, Deque<String>> deptToDest = new HashMap<>();

        // to get the edges in ascending order just sort the edges in descending order
        // now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first 
        // so we can take the last one just by popping
        tickets.sort((a, b) -> {
            int cmp = b.get(0).compareTo(a.get(0));
            return cmp == 0 ? b.get(1).compareTo(a.get(1)) : cmp;
        });

        for (List<String> ticket : tickets) {
            deptToDest
                .computeIfAbsent(ticket.get(0), k -> new ArrayDeque<>())
                .addLast(ticket.get(1));
        }

        Stack<String> stack = new Stack<>();
        List<String> ans = new ArrayList<>();
        stack.push("JFK");

        while (!stack.isEmpty()) {
            while (deptToDest.containsKey(stack.peek()) && !deptToDest.get(stack.peek()).isEmpty()) {
                // if more than two paths are possible then it will take the path with lesser lexographic order 
                stack.push(deptToDest.get(stack.peek()).pollLast());
            }
            // when you get stuck then pop and add to the ans
            ans.add(stack.pop());
        }

        Collections.reverse(ans);  // reverse the result as we added in postorder
        return ans;
    }
}

"""


# C++
"""
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
#include <deque>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, deque<string>> deptToDest;

        // to get the edges in ascending order just sort the edges in descending order
        // now add the adjacent vertices into hashmap. Edges bigger in lexographic order will come first 
        // so we can take the last one just by popping
        sort(tickets.rbegin(), tickets.rend());
        for (auto& ticket : tickets) {
            deptToDest[ticket[0]].push_back(ticket[1]);
        }

        stack<string> st;
        vector<string> ans;
        st.push("JFK");

        while (!st.empty()) {
            while (!deptToDest[st.top()].empty()) {
                // if more than two paths are possible then it will take the path with lesser lexographic order 
                string next = deptToDest[st.top()].back();
                deptToDest[st.top()].pop_back();
                st.push(next);
            }
            // when you get stuck then pop and add to the ans
            ans.push_back(st.top());
            st.pop();
        }

        reverse(ans.begin(), ans.end());  // reverse the result as we added in postorder
        return ans;
    }
};


"""

# Method 3: 
# use minHeap to get smaller lexographically flight
# Since the problem asks for lexical order smallest solution, we can put the neighbors in a min-heap. 
# In this way, we always visit the smallest possible neighbor first in our trip.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = defaultdict(list)
        for ticket in tickets:
            heapq.heappush(flights[ticket[0]], ticket[1])
        
        path = deque()
        
        def dfs(departure):
            arrivals = flights[departure]
            while arrivals:
                next_destination = heapq.heappop(arrivals)
                dfs(next_destination)
            path.appendleft(departure)
        
        dfs("JFK")
        return list(path)

# java
"""
import java.util.*;

class Solution {
    Map<String, PriorityQueue<String>> flights = new HashMap<>();
    LinkedList<String> path = new LinkedList<>();

    public List<String> findItinerary(List<List<String>> tickets) {
        for (List<String> ticket : tickets) {
            // Push destination into a min-heap for each departure
            flights
                .computeIfAbsent(ticket.get(0), k -> new PriorityQueue<>())
                .offer(ticket.get(1));
        }

        dfs("JFK");
        return path;
    }

    // DFS to build path in reverse post-order
    private void dfs(String departure) {
        PriorityQueue<String> arrivals = flights.get(departure);
        while (arrivals != null && !arrivals.isEmpty()) {
            String nextDestination = arrivals.poll();  // pop lexicographically smallest destination
            dfs(nextDestination);
        }
        path.addFirst(departure);  // build the path in reverse
    }
}


"""


# C++
"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <list>
#include <string>
using namespace std;

class Solution {
    unordered_map<string, priority_queue<string, vector<string>, greater<string>>> flights;
    list<string> path;

    // DFS to build path in reverse post-order
    void dfs(const string& departure) {
        auto& arrivals = flights[departure];
        while (!arrivals.empty()) {
            string nextDestination = arrivals.top();  // pop lexicographically smallest destination
            arrivals.pop();
            dfs(nextDestination);
        }
        path.push_front(departure);  // build the path in reverse
    }

public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        for (auto& ticket : tickets) {
            // Push destination into a min-heap for each departure
            flights[ticket[0]].push(ticket[1]);
        }

        dfs("JFK");
        return vector<string>(path.begin(), path.end());
    }
};


"""