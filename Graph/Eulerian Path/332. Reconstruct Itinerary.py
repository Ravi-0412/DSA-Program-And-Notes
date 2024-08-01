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

# method 1: using dfs
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


# method 2: converted the above code into iterative form
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

# Other way : use minHeap to get smaller lexographically flight
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

public class Solution {

    Map<String, PriorityQueue<String>> flights;
    LinkedList<String> path;

    public List<String> findItinerary(String[][] tickets) {
        flights = new HashMap<>();
        path = new LinkedList<>();
        for (String[] ticket : tickets) {
            flights.putIfAbsent(ticket[0], new PriorityQueue<>());
            flights.get(ticket[0]).add(ticket[1]);
        }
        dfs("JFK");
        return path;
    }

    public void dfs(String departure) {
        PriorityQueue<String> arrivals = flights.get(departure);
        while (arrivals != null && !arrivals.isEmpty())
            dfs(arrivals.poll());
        path.addFirst(departure);
    }
}

"""