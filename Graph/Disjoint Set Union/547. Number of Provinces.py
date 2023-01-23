# just we have to find the 'no of connected components'.
# we can use either Bfs or dfs for this.

# By DSU.
# logic: just count the no of unique ultimate parent. This will give the no of connected components.
# for this just fill the parent array then then run a for loop to check :
# if n= parent[n]: coun+= 1. and at last return count
# or simply store the parent in a set and return the len(set).


# how to do union : Try to bring all the connected nodes(value==1) into one component.
# if we can't do union of nay two node their parent node will differ and will go into other component.

# time: O(n^2) to traverse into matrix.
class DSU:
    def __init__(self, n):
        self.v= n
        self.parent=  [i for i in range(n)]     # here '0' based indexing is used in Q.
        self.size=    [1 for i in range(n)]   # will give thesize of each parent component.
            # initially size of all be '1'(node itself).
    
    def findUPar(self, n):   # finding the ultimate parent
        if n== self.parent[n]:   # Root parent will be the parent of itself. so continue till we find that.
            return n
        # return self.parent[n]= self.findUPar(self.parent[n])    # this will assign the root parent of every node coming in that ultimate root.
                                                #    This is called path compression.
        self.parent[n]= self.findUPar(self.parent[n])   # writing above in same link is giving error
        return self.parent[n]
        # return self.findUPar(self.parent[n])   # This will only give the parent node, will not assign.
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return 
        # wherever we are assigning the parent means we are directly connecting those two nodes.
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2   # attaching ultimate parent of 'n1' i.e p1 to ultimate parent of 'n2' i.e p2.
            self.size[p2]+= self.size[p1]   # increase the size of p2 by size of p1.
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   # attaching ultimate parent of 'n2' i.e p2 to ultimate parent of 'n1' i.e p1.
            self.size[p1]+= self.size[p2]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        dsu= DSU(n)
        # try to connected all the vertices which are connected(matrix[i][j]= 1) into one component.
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]== 1:
                    dsu.unionBySize(i, j)
        
        # now count  the no of distinct parent
        count= 0
        for p in range(n):  
            if p== dsu.parent[p]:
                count+= 1
        return count


