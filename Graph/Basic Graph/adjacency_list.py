# code of graph(dsa notes, page:100)
class Node:
    def __init__(self,v):
        self.vertex= v    # just like we do in linklist
        self.next= None
    
class Graph:
    def __init__(self,size):
        self.size= size  # will givethe size of the graph(no of nodes)
        self.graph= [None]*size   # creating array of pointers
    
    def add_edge(self,s,d):  # s: source, d: destination
        # we are appending using insert first 
        # adding destination to source
        node= Node(d)
        node.next= self.graph[s]
        self.graph[s]= node  # now make that index of graph as destination node(insert at first)
        # since undirected so add links in other also
        # add  source to destination
        node= Node(s)
        node.next= self.graph[d]
        self.graph[d]= node
    
    def print_graph(self):
        for i in range(self.size):
            temp= self.graph[i]
            print("vertex adjacent to {}th vertex are: ".format(i))
            while temp:
                print(temp.vertex,end=" ")
                temp= temp.next
            print()

g= Graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,4)

g.print_graph()
            




