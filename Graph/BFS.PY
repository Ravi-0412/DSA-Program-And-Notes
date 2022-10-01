from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.size= n
        self.distance= [0]*n
        self.colors= ['white']*n
        self.pred= [-1]*n
        self.adjMatrix= []
        for i in range(n):
            self.adjMatrix.append([0 for i in range(n)])  # intilaise all ele with '0' and creating a matrix
    # add the add
    def addEdge(self,v1,v2):
        if v1==v2:
            print("both the vertices are same")
        else:
            self.adjMatrix[v1][v2]= 1
            self.adjMatrix[v2][v1]= 1  # since making for undirected graph
                                      # so it will be symmetric
    # function to print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)
        print()

    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("no edge exist bw these vertices")
        else:
            self.adjMatrix[v1][v2]= 0
            self.adjMatrix[v2][v1]= 0

# use deque as poping starting ele from q when using as list will be take O(n) for eacch element

    def BFS(self,s):   # s: starting vertex
        # first store adjacent of all vertices into a dictionary
        graph= defaultdict(list)  # will contain the vertices mapped with their adjacent vertices
                                  # values(adjacent vertices) will be in the list
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j]== 1:
                    graph[i].append(j)
        print(graph)
        # for key,val in graph.items():
        #     print(val)
        
        # now apply BFS on the graph
        self.colors[s] ='gray'
        self.distance[s]= 0
        self.pred[s]= -1
        Q= []   # queue to store vertices
        # add source into the Q
        Q.append(s)
        # now run a loop till 'Q' becomes empty
        print("bfs traversal of following graph is: ")
        while Q:
            # pop the first ele from 'Q' 
            curr= Q.pop(0)
            print(curr, end=" ")
            # now push all the adjacent vertices of poped ele into the 'Q'
            # if that has not been seen yet
            for i in range(len(graph[curr])):
                # check whether seen or not
                if self.colors[graph[curr][i]]== 'white': # if seeing for 1st time then push into the Q
                    self.colors[graph[curr][i]]= 'gray'
                    self.distance[graph[curr][i]]= self.distance[curr] +1
                    self.pred[graph[curr][i]]= curr
                    Q.append(graph[curr][i])
            # now you have visited all the nodes ajacent to 1st ele of Q(poped one)
            # so make its colour as 'black'
            # print("queue is ", Q)
            self.colors[curr]= 'black'
        print("distance of all vertices from source",self.distance)
            # print(Q)

g= Graph(8)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(4,7)
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(6,7)
g.print_matrix()
g.BFS(2)
