class Graph:
    def __init__(self,n):
        self.adjMatrix= []
        for i in range(n):
            self.adjMatrix.append([0 for i in range(n)])  # intilaise all ele with '0'
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
# g.remove_edge(0,2)
# g.print_matrix()

