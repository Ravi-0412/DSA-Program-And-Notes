"""
using min heap, time: 0(E*logV). Every edge will get relaxed exactly one time. 
logic: same as Bfs only diff is we use here min_heap instead of Queue with weight.

Note vvi: We don't mark visited when we see the node for 1st time itself in case, 
when there are possibility of getting more better path OR
 when we are not able to decide the exact min time(or distance) in which we will see the same node again.
In this case we mark visited after poping the node. It means we got the min time in which we can visit the poped node.
So after poping we relax all its edges to minimise other nodes connected to it.

Note: But when we are sure that we will get ans when we will see the node for 1st time itself and at that time we can mark visited and check the ans at 1st time itself.
e.g: "Q. 778.swimming in Rising water"


Note: Whenever we are asked to find the shortest path having no weight or equal we use bfs. 
Reason: we go breadth wise to reach the other cell as soon as possible.

If weighted then think of Dijkastra Algo.

Related Q:
1) 2092. Find All People With Secret
"""

from collections import defaultdict
import heapq
def ShortestPath(adj,n, src):
    edges= defaultdict(list)  # converting into adjacency list with adjacent edges and their weights
    for u,v,w in adj:
        edges[u].append((v,w))
    distance = ['inf']*n
    distance[src] = 0   # will conatin the distance of source to all other vertices
    minHeap = [(0,src)]  # first ele should be weight as it will create the heap using 1st ele always
    visited = set()  
    while minHeap:
        w1,n1 = heapq.heappop(minHeap)    # it means for this node, we have got the optimal ans so we will relax all the nodes to this node and mark this node as visited
        # since we are marking any node visited only we have relaxed all the outgoing edge through that vertex
        #  so there can be many instances of same node in the minHeap and once we have releaxed all the edges through that node 
        # then, no need to relax all the edged through that node again anymore so simply skip
        if n1 in visited:    
            continue
        visited.add(n1)     # only mark visited if we have are going to relax all of the outgoing edge from the curr node. 
        for n2, w2 in edges[n1]:
            if n2 not in visited:
                if distance[n2] > w1+ w2:
                    distance[n2]= w1+w2
                    # visited.add(n2)       # this will give incorrect ans. this is one more diff from Bfs
                                            # you can only add any node to visited if you have found the optimal ans for that node i.e when you will pop

                # when we push more than one ele in heap, 
                # it create the min/max heap acc to the 1st ele(1st pushed ele)
                heapq.heappush(minHeap,(distance[n2], n2))  
    return distance


# another way of writing (better one)
def ShortestPath1(adj,n, src):
    edges= defaultdict(list)  # converting into adjacency list with adjacent edges and their weights
    for u,v,w in adj:
        edges[u].append((v,w))
    distance= [9999999]*n
    distance[src]= 0   # will conatin the distance of source to all other vertices
    minHeap= [(0,src)]  # first ele should be weight as it will create the heap using 1st ele always
    visited= set()  
    while minHeap:
        w1,n1= heapq.heappop(minHeap)    # it means for this node, we have got the optimal ans so we will relax all the nodes to this node
        if n1 in visited:
            continue
        distance[n1] = w1  # poped one means we have found minimum distance of that
        visited.add(n1)     # only mark visited if we have are going to relax all of the outgoing edge from the curr node. 
        for n2, w2 in edges[n1]:
            if n2 not in visited:  # if not viisted then simply add in minHeap. 'n2' with MinDistance will be automatically on the first of heap.
                heapq.heappush(minHeap,(w1+w2, n2))  
    return distance
adj= [[0,1,10],[0,2,5],[1,3,1],[1,2,2],[2,1,3],[2,4,2],[2,3,9],[3,4,4],[4,0,7],[4,3,6]]
# print(ShortestPath(adj, 5, 0))
print(ShortestPath1(adj, 5, 0))

# Java
"""
public class Solution {
    public int[] shortestPath1(int[][] adj, int n, int src) {
        // Convert input edge list to adjacency list with weights
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edges.put(i, new ArrayList<>());
        }

        for (int[] e : adj) {
            int u = e[0];
            int v = e[1];
            int w = e[2];
            edges.get(u).add(new int[]{v, w});
        }

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[src] = 0;  // will contain the shortest distance from source to all vertices

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        minHeap.offer(new int[]{0, src});  // first element = weight, second = node

        Set<Integer> visited = new HashSet<>();

        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int w1 = top[0];
            int n1 = top[1];

            if (visited.contains(n1)) continue;

            distance[n1] = w1;  // finalized shortest distance for n1
            visited.add(n1);    // mark as visited only when we're about to relax outgoing edges

            for (int[] edge : edges.get(n1)) {
                int n2 = edge[0];
                int w2 = edge[1];

                if (!visited.contains(n2)) {
                    minHeap.offer(new int[]{w1 + w2, n2});  // add with updated weight
                }
            }
        }

        return distance;
    }
}
"""

"""
Now if we want to print shortest path from source to any node.

We need to keep track of through which node we got the optimal one so store parent also in node and also maintain
an parent array for this.
Traverse back from each node till you reach parent of source.
Just same we find for other shortest path like bfs etc.

time: 0(E*logV + V^2) , V^2: for printing path for each node.
"""

from collections import defaultdict
import heapq

def ShortestPath1(adj,n, src):
    edges= defaultdict(list)  
    for u,v,w in adj:
        edges[u].append((v,w))
    parent = [-1] * n
    distance= [9999999]*n
    distance[src]= 0   
    minHeap= [(0,src, -1)]  
    visited= set()  
    while minHeap:
        w1, n1, p1 = heapq.heappop(minHeap)    
        if n1 in visited:    
            continue
        distance[n1] = w1
        parent[n1] = p1
        visited.add(n1)     
        for n2, w2 in edges[n1]:
            if n2 not in visited:  
                heapq.heappush(minHeap,(w1 + w2, n2, n1))
    
    # print shortest path from source to each node
    for i in range(n):
        path = []
        cur = i
        # continue till you reaches parent of source i.e '-1' 
        while cur != -1:
            path.append(cur)
            cur = parent[cur]
        print("path and distance of node {} from source {} is : {} and {}".format(i, src, path[::-1], distance[i]))
        
# adj= [[0,1,10],[0,2,5],[1,3,1],[1,2,2],[2,1,3],[2,4,2],[2,3,9],[3,4,4],[4,0,7],[4,3,6]]
# n = 5 
# src = 0
# adj = [[0, 1, 2], [1, 4, 5], [1, 2, 4], [0, 3, 1], [3, 2, 3], [2, 4, 1]]
# n = 5
# src = 0
adj = [[0, 1, 2], [1, 2, 4], [0, 3, 1], [3, 2, 3]]
n = 4
src = 0
print("shostest from source to each node: ", ShortestPath1(adj, n, src))

# Java
"""
import java.util.*;

public class Solution {
    public void shortestPath1(int[][] adj, int n, int src) {
        // Adjacency list with weights
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edges.put(i, new ArrayList<>());
        }

        for (int[] e : adj) {
            int u = e[0], v = e[1], w = e[2];
            edges.get(u).add(new int[]{v, w});
        }

        int[] parent = new int[n];
        Arrays.fill(parent, -1);

        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[src] = 0;

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]); // (weight, node, parent)
        minHeap.offer(new int[]{0, src, -1});

        Set<Integer> visited = new HashSet<>();

        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int w1 = top[0];
            int n1 = top[1];
            int p1 = top[2];

            if (visited.contains(n1)) continue;

            distance[n1] = w1;
            parent[n1] = p1;
            visited.add(n1);

            for (int[] nei : edges.get(n1)) {
                int n2 = nei[0];
                int w2 = nei[1];
                if (!visited.contains(n2)) {
                    minHeap.offer(new int[]{w1 + w2, n2, n1});
                }
            }
        }

        // Print paths and distances
        for (int i = 0; i < n; i++) {
            List<Integer> path = new ArrayList<>();
            int cur = i;
            while (cur != -1) {
                path.add(cur);
                cur = parent[cur];
            }
            Collections.reverse(path);
            System.out.println("Path and distance of node " + i + " from source " + src + " is : " + path + " and " + distance[i]);
        }
    }
 }
"""
