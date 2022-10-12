# i thought in correct way onl;y but not able to get the last occured input as ans in acse of more than one
# like when two greater node value is connected to a smaller node value all forming a cycle
# tried a lot 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # first convert into adjacency list say "graph"
        graph= defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)
        # now apply bfs 
        Q= collections.deque()
        # while adding vertex to Q, add its parent node also
        Q.append((1, -1))    # appending the (node, parent)
        visited= set()      
        visited.add(1)       # adding the starting node in visited as here there is only one component this will work fine
        ans= edges[0] 
        while Q:
            (curr, parent)= Q.popleft()
            for u in graph[curr]:
                print("parent and u: ",parent,u)
                if u not in visited:
                    visited.add(u)
                    Q.append((u,curr))
                elif u!= parent:  # u is visited as well as not parent means cycle so store in the ans
                    print(ans, (parent,u))
                    if edges.index([parent,u]) >=edges.index(ans):
                        ans= [parent,u]
                    print("updated",ans, (parent,u))
                    
        return ans


# the problem that was occuring in above solution is solved by 'union-find' and path compression method
# Note: this Q was made on this approach only like we have to find the last input in case of more than one ans and this approach we will get that only
# https://www.youtube.com/watch?v=FXWRE67PLL0&t=945s   # for this q 

# for better understanding the 'union find'. general and better one.. 
# https://www.youtube.com/watch?v=3gbO7FDYNFQ&t=306s

# every node will be parent of itself at start and rank of all will be '0' initially

# for union(merging the two into one): find the root parent of both the node and attach the node with smaller rank to the node with larger rank 
# and parent_larger_rank= parent[node_with_smaller_rank]

# when attaching the node, only increment the rank by '1'  for parent node(to which we are attaching) if rank of both the parent node is equal otherwise don't incr 
# increment in rank by '1' means increment in height by '1'
# and icreasing the rank always will increase the height of tree  and will lead to high time complexity

# to find whether two node belong to the same component or not, just find the parent of both
# if parent of both is equal then they belong to same component otherwise not
# this one is the basic to check whether adding any edge will lead to the cycle or not
# if we want to add an edge between two node belonging to same component(having same root parent) then adding that edge will lead to the cycle

# time for union: O(4 alpha) nearly = O(1), space: O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent= [i for i in range(len(edges)+1)]  # node starting from '1' to 'n' but starting from  '0' for easier calculation(direct geeting the value from node number)
                # willc ontain the value of root parent at last for each node
        rank= [0] *(len(edges)+1)  # initally rank of all will be '0' since all are at height '0' (single node)
        
        # finding the root parent and the 1st level parent
        # for root level parent, compress the path till parent[p]!= p as root will parent as root only
        def find(n):
            p= parent[n]
            # path compression so that you can directly go to the root parent of each node
            while p!= parent[p]:
                parent[p]= parent[parent[p]]  # for checking the next level node(grandparent) in next cycle
                p= parent[p]
            return p

        # Recursive way to find the parent
        # def find(n):
        #     if n== parent[n]:
        #         return n
        #     find(parent[n])
        
        def union(n1,n2):
            p1,p2= find(n1), find(n2)
            if p1== p2:             # means both have same root parent then adding this edge will lead to a cycle 
                                    # also acc to Q we have to return the ans coming at last in input so this will be our ans only
                return False        # will check this condition while adding any edge to the graph
            
            if rank[p1]> rank[p2]:
                parent[p2]= p1
                
            else:
                parent[p1]= p2
                if rank[p2]== rank[p1]:
                    rank[p2]+= 1

            # return True    # without this it is also fine as we have to check when we can't add any more edges(False condition)
        
        # code starts from here
        for n1,n2 in edges:
            if union(n1,n2)== False:
                return [n1,n2]

