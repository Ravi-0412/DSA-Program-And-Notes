# just we have to find the 'no of connected components' cell value= 1.
# we can use either Bfs or dfs for this.

# By DSU.
# logic: just count the no of unique ultimate parent. This will give the no of connected components.
# for this just fill the parent array then then run a for loop to check :
# if n= parent[n]: coun+= 1. and at last return count
# or simply store the parent in a set and return the len(set).

# Reason: Every component will have same parent for each ele in that component.

# Note VVI: jahan jahan '1' h usko union karne ka prayas karo, agar indirectly connecte hoga ek dusre to ek component form lega.
# agar nhi hoga then alag component form karega.
# Then at last count no of component i.e distinct parent ka no count karo wahi ans hoga.

# how to do union : Try to bring all the connected nodes(value==1) into one component.
# if we can't do union of any two node their parent node will differ and will go into other component.

# time: O(n^2) to traverse into matrix.

# Note: see the union function properly.
class DSU:
    def __init__(self, n):
        self.v= n
        self.parent=  [i for i in range(n)]     # here '0' based indexing is used in Q.
        self.size=    [1 for i in range(n)]   # will give thesize of each parent component.
            # initially size of all be '1'(node itself).
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
                                            
        self.parent[n]= self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)

        # no need of this because it means they are already connected to each other so if they are already connected
        # then me must have processed them before only.  so everytime we will get diff p1 and p2.
        # if p1== p2:  
        #     return 
        
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2   
            self.size[p2]+= self.size[p1] 
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1  
            self.size[p1]+= self.size[p2]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        dsu= DSU(n)
        # try to connected all the vertices which are connected(matrix[i][j]= 1) into one component.
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]== 1:   
                    dsu.unionBySize(i, j)   # here 'i' and 'j' represent city. so we are passing (i, j) to combine into one.

        # now count  the no of distinct parent
        count= 0
        for p in range(n):  
            if p== dsu.parent[p]:
                count+= 1
        return count


# Note: This method of counting distinct parent is always valid to count the connected components but in other Q you have to modify a bit.

# Note for union: Q) Here we are not doing union with any previous ele but we only do union with already added ele or 
# we can do union with one connected component with another connected component. But why still giving correct ans?

# Reason: Because whenever there is '1' between any two node means they are connected to each other. 
# And a single node is connected componnet in itself. So we are trying to connect two connected component only.
# So the node which is directly or indirectly connected('1' between them) will form a single component.
# e.g: [0][1]= 1 then after union (0,1) will come together. now let [1][3]= 1 then '3' will get attached to parent of '1' and finally 
# all three (0,1,3) will get connected into one single component.  In this way we will get all connected nodes.

# Q) Why we are making parent array of 'n' only desite we are working on 'n*n' matrix?
# Reason: Because there can be max 'n' connected components(only 'n' vertices).



# Method 2: Dfs solution of above.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        count= 0
        visited= set()

        def dfs(i):
            # any other city will be only connected if there is value= '1' between that city.
            # also we have to check whether other city is already visited(already in one component).
            for j in range(n):
                if isConnected[i][j] ==1 and j not in visited:
                    visited.add(j)
                    dfs(j)  # connecting all cities together whcih are indirectly connected

        # from each noode try to get all the nodes connected to each other.
        for city in range(n):
            if city not in visited:
                count+= 1
                dfs(city)
        
        return count
        