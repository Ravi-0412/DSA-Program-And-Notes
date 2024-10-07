# just print the order of topological sort
# method 1: By  Bfs

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        AdjList = defaultdict(list)
        indegree = [0]*n
        # first convert into adjacency list(edges) for directed graph and calculate indegree
        for second,first in prerequisites:
            AdjList[first].append(second)
            indegree[second] += 1
        
        count, ans = 0, []
        Q = collections.deque()
        # now applying the BFS to get the topological order
        # find the node with indegree '0' as this node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS
        for i in range(n):
            if indegree[i] == 0: 
                Q.append(i)
    
        while Q:
            count += 1  
            u = Q.popleft()
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j] -= 1
                if indegree[j] == 0:  # after decreasing if any node has indegree == 0 then put in the Q
                    Q.append(j)

        if count != n:  # means cycle so no order is possible 
            return []
        return ans


# another way using dfs: this submitted in Q "269 Alien dictionary"
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:
            AdjList[first].append(second)
        visited= [0]*numCourses
        stack= []   # store the course completion in reverse order
        for i in range(numCourses):
            if not self.FindTopoSort(AdjList,i,stack,visited):    # if cycle simply return False, else continue checking for another node
                return []
        return stack[::-1]
        

    def FindTopoSort(self, adj,src, stack,visited):
        # base case for checking whether we have visited all the adjacent node.. if visited then check on another node
        if visited[src]== 1:   # been visited and added to the stack(ans). so simply return true so that it can check for next node without repeating the work
            return True         # returning False will give wrong ans as when it will see 'False' funtion will return from there only.
        # base case for checking cycle 
        if visited[src]== -1:   # means cycle as the current node(src) is already visited in current cycle only
            return False        # if not '0' means the this has been visited(not) and if = '-1' then visited in current cycle , means there is cycle.

        # code starts from here
        visited[src]= -1   # Marking 'cur' node is visited in current cycle. Also it means till now we have only visited the 'src' not its adjacent node.
        for u in adj[src]:
            if not self.FindTopoSort(adj, u, stack, visited):
                return False
                
        # while traversing back make visited[src]= 1 and  put the node into the stack
        visited[src]= 1   # means we have visited the 'src' as well as its neighbour and added to the ans(stack)
        stack.append(src)
        return True   # means we have visited the current node as well as its neighbour successfully
