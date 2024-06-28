# just the topological sorting
# how to reach think about topo sort?: 
# Ans: we can only finish all the courses if there exist any order for completing all the courses.
# and order is only possible when we will make a directed graph between the dependency given and graph should have no cycle.
# and for finding any ordering with checking cycle , only thing comes into mind is 'Topological Sort'  
# if no cycle then it is possible.

# Note vvi: But for this Q, we don't need to do topological sort,
# Because here we only need to check if there exist cycle or not.
# If no cycle then it is possible to complete all courses else not.

# So we can apply simple bfs and dfs to check cycle in directed graph ()

# But in Q. "210.course Schedule 2", we need to go by topological sort only since we have to find the completion order.
# And order we can only get by topological sorting.

# method 1 :
# dfs to check cycle
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:
            AdjList[first].append(second)

        def checkCycle(src):
            visited.add(src)
            path_visited.add(src)
            for u in AdjList[src]:
                if u not in visited:
                    if checkCycle(u):
                        return True
                elif u in path_visited:
                    return True
            path_visited.remove(src)
            return False

        visited= set()
        path_visited= set()
        for i in range(numCourses):
            if i not in visited and checkCycle(i):    # if cycle simply return False, else continue checking for another node
                return False
        return True
    
    
# method 2: using topological sort

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for first,second in prerequisites:
            AdjList[second].append(first)  # phle 2nd wala course karenge tb hi first kar sakte h.
        
        n = numCourses
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1
        
        # now applying the BFS to get the topological order
        count, ans = 0, []
        Q  = collections.deque()
        # count will tell how many courses we have finished(how many nodes we have visited).
        # 'ans' will store the sequence of course completion

        # find all the nodes with indegree '0' as these node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS.
        # since we are putting all the nodes having indegree = 0, so it will also take care if there is multiple components.
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)
    
        while Q:
            count+= 1  
            u= Q.popleft()
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j] -= 1   # matlab ek course jispe dependent tha wo complete hua.
                if indegree[j]== 0:  # after decreasing if any node has indegree == 0 i.e agar sb dependent course complete ho gya ho then put in the Q.
                    Q.append(j)

        if count != n:  # for checking the cycle in directed graph using BFS. count will always less than 'n' in case of cycle
            return False
        return True
        
        


# # method 3: Dfs (already done in topological sorting)
# # very better solution: used only one array (we can use another array 'path_visited' also like we used to do)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:
            AdjList[first].append(second)
        visited= [0]*numCourses
        stack= []   # store the course completion in reverse order
        for i in range(numCourses):
            if not self.FindTopoSort(AdjList,i,stack,visited):    # if cycle simply return False, else continue checking for another node
                return False
        return True
        
    # Returns true if path is possible i.e no cycle.
    def FindTopoSort(self, adj,src, stack,visited):
        # base case for checking whether we have visited all the adjacent node.. if visited then check on another node
        if visited[src]== 1:   # been visited and added to the stack(ans). so simply return true so that it can check for next node without repeating the work
            return True         # returning False will give wrong ans as when it will see 'False' funtion will return from there only.
        # base case for checking cycle 
        if visited[src]== -1:   # means cycle as the current node(src) is already visited in current cycle only
            return False        # if not '0' means the this has been visited(not their adj) and if = '-1' then visited in current cycle , means there is cycle.

        # code starts from here
        visited[src]= -1   # Marking 'cur' node is visited in current cycle. Also it means till now we have only visited the 'src' not its adjacent node.
        for u in adj[src]:
            if not self.FindTopoSort(adj, u, stack, visited):
                return False   # cycle 
                
        # while traversing back make visited[src]= 1 and  put the node into the stack
        visited[src]= 1   # means we have visited the 'src' as well as its neighbour and added to the ans(stack)
        stack.append(src)
        return True   # means we have visited the current node as well as its neighbour successfully. No cycle


# Java
""""
// Method 1:
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        // first convert into adjacency list(edges) for directed graph
        for (int[] prerequisite : prerequisites) {
            int second = prerequisite[0];
            int first = prerequisite[1];
            if (!AdjList.containsKey(first)) {
                AdjList.put(first, new ArrayList<>());
            }
            AdjList.get(first).add(second);
        }

        Set<Integer> visited = new HashSet<>();
        Set<Integer> pathVisited = new HashSet<>();
        for (int i = 0; i < numCourses; i++) {
            if (!visited.contains(i) && checkCycle(i, AdjList, visited, pathVisited)) {
                return false;
            }
        }
        return true;
    }

    private boolean checkCycle(int src, Map<Integer, List<Integer>> AdjList, Set<Integer> visited, Set<Integer> pathVisited) {
        visited.add(src);
        pathVisited.add(src);
        for (int u : AdjList.getOrDefault(src, new ArrayList<>())) {
            if (!visited.contains(u)) {
                if (checkCycle(u, AdjList, visited, pathVisited)) {
                    return true;
                }
            } else if (pathVisited.contains(u)) {
                return true;
            }
        }
        pathVisited.remove(src);
        return false;
    }
}

// Method 2:
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        // first convert into adjacency list(edges) for directed graph
        for (int[] prerequisite : prerequisites) {
            int first = prerequisite[1];
            int second = prerequisite[0];
            if (!AdjList.containsKey(second)) {
                AdjList.put(second, new ArrayList<>());
            }
            AdjList.get(second).add(first);
        }

        int n = numCourses;
        int[] indegree = new int[n];

        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            if (AdjList.containsKey(i)) {
                for (int k : AdjList.get(i)) {
                    indegree[k]++;
                }
            }
        }

        // now applying the BFS to get the topological order
        int count = 0;
        List<Integer> ans = new ArrayList<>();
        Deque<Integer> Q = new LinkedList<>();

        // find all the nodes with indegree '0' as these node will come 1st in the topological order
        // i.e it will be the source node and after that apply the BFS.
        // since we are putting all the nodes having indegree = 0, so it will also take care if there is multiple components.
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                Q.offerLast(i);
            }
        }

        while (!Q.isEmpty()) {
            count++;
            int u = Q.pollFirst();
            ans.add(u);
            // after popping decrease the indegree of all node adjacent to 'u'
            if (AdjList.containsKey(u)) {
                for (int j : AdjList.get(u)) {
                    indegree[j]--;
                    if (indegree[j] == 0) {
                        Q.offerLast(j);
                    }
                }
            }
        }

        if (count != n) { // for checking the cycle in directed graph using BFS. count will always less than 'n' in case of cycle
            return false;
        }
        return true;
    }
}


// Method 3:

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        // first convert into adjacency list(edges) for directed graph
        for (int[] prerequisite : prerequisites) {
            int second = prerequisite[0];
            int first = prerequisite[1];
            if (!AdjList.containsKey(first)) {
                AdjList.put(first, new ArrayList<>());
            }
            AdjList.get(first).add(second);
        }
        int[] visited = new int[numCourses];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < numCourses; i++) {
            if (!findTopoSort(AdjList, i, stack, visited)) {
                return false;
            }
        }
        return true;
    }

    // Returns true if path is possible i.e no cycle.
    private boolean findTopoSort(Map<Integer, List<Integer>> adj, int src, Stack<Integer> stack, int[] visited) {
        // base case for checking whether we have visited all the adjacent node.. if visited then check on another node
        if (visited[src] == 1) {
            return true;
        }
        // base case for checking cycle
        if (visited[src] == -1) {
            return false;
        }

        // code starts from here
        visited[src] = -1;
        for (int u : adj.getOrDefault(src, new ArrayList<>())) {
            if (!findTopoSort(adj, u, stack, visited)) {
                return false;
            }
        }
        visited[src] = 1;
        stack.push(src);
        return true;
    }
}

"""