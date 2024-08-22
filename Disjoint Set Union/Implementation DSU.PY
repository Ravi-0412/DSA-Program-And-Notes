# There are two things in this: 1) FindParent  (ultimate parent)  2) Union.

# 1) find parent.
# it is used to check whether two node belong to same component or not.
# every node will be parent of itself at start.

# to find whether two node belong to the same component or not, just find the parent of both
# if parent of both is same then they belong to same component otherwise not.

# this one is the basic to check whether adding any edge will lead to the cycle or not
# if we want to add an edge between two node belonging to same component(having same root parent) then adding that edge will lead to the cycle.

# so we can only do union of two node if they belong to different component for avoiding cycle.


# 2) for union(merging the two into one): union tells whether we can connect two node or not by an edge.
#  if not then it means connecting these two node(given edge) will lead to cycle.

# logic for union: first find the root parent(ultimate parent) of both the node.
# if parent is different then it means they belong to different component and we can do the union otherwise not.
# then for doing union just use any of ways i.e rank or size.

# There are two ways we can do union:
# a) 'union by Rank':
# attach the ultimate parent  with smaller rank to the ultimate parent with larger rank.
# and make parent[node_with_smaller_rank]= parent_larger_rank.

# Here we only increase the rank of any of parent node, if rank of both is same.
# when attaching the node, only increment the rank by '1'  for parent node(to which we are attaching),
# if rank of both the parent node is equal otherwise don't incr..

# Reason: increment in rank by '1' means increment in height by '1'
# and icreasing the rank always will increase the height of tree  and will lead to high time complexity.


# b) Union by Size:
# increase the size of node to which you are attaching other node by 'size of node you are attaching'.
# i.e if parent[p1]= p2 then size[p2]+= size[p1].
# vvi: we merge the ultimate parent of both the nodes. so we add the size of one into other(new_parent).

# Note: 'UnionBySize' is more meaningful and initiutive than 'UnionByRank'.

# Q) why connect smaller to larger only in both rank in size cases?
# so that height doesn't increase much leading to higher time complexity.

# Note: After finding the root parent of each node, ultimate parent of both nodes are get attached to each other. not the two given node.

# Q) why we are calling 'findParent' to find the ultimate parent of each node.
#  why are we don't directly finding the parent from parent array?
# Ans: when we combine two node from different component then we are not able to update the 
# remaining nodes of 'node having lesser size/rank' to new ultimate parent. 
# Also while finding parent, only the nodes that belong to that component there parent get updated.


# time for union: O(4 alpha) nearly = O(1), space: O(n)
# time for find Parent= O(4* alpha)

class DSU:
    def __init__(self, n):
        self.rank=    [0 for i in range(n)]  
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   # will give the size of each parent component.
            # initially size of all be '1'(node itself). will tell no of nodes in each parent
    
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
    
    def unionByRank(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return
        if self.rank[p1] < self.rank[p2]:
            self.parent[p1]= p2
        else :   # rank[p1]>= rank[p2]
                self.parent[p2]= p1
                if self.rank[p1]== self.rank[p2]:  # only incr rank if rank of both are equal
                    self.rank[p1]+= 1

d= DSU(7)
# d.unionByRank(0, 1)
# d.unionByRank(1, 2)
# d.unionByRank(3, 4)
# d.unionByRank(5, 6)
# d.unionByRank(4, 5)
# d.unionByRank(2, 6)
# # check if '2' and '6' belong to the same component. by commenting and uncommenting the above line.
# if d.findUPar(2)== d.findUPar(6):
#     print("2 and 6 belong to same component")
# else:
#     print("2 and 6 not belong to same component")

# doing by 'unionBy size'.
d.unionBySize(0, 1)
d.unionBySize(1, 2)
d.unionBySize(3, 4)
d.unionBySize(5, 6)
d.unionBySize(4, 5)
# d.unionBySize(2, 6)
# check if '2' and '6' belong to the same component. by commenting and uncommenting the above line.
if d.findUPar(2)== d.findUPar(6):
    print("2 and 6 belong to same component")
else:
    print("2 and 6 not belong to same component")
print(d.size)
print(d.parent)


# Template to use in Qs.

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findParent(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        p1, p2= self.findParent(n1), self.findParent(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            # return
            # return False
            return 0
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # size[p1]>= size[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        # return True
        # return 1


# Note: every time we will get our ans while doing 'union' only. so you might have to modify little bit'union' function to get the ans.
# like : 1) you may have to simply return or you have to return '0' in case we can't do union  
# 2) you may have to return True or return '1' in case union is possible.  
# 3) may be in little other way according to the Q.

# Note: in every Q, first convert the parameter(you want to do union) in an integer 
# because we have to find parent and all , and they can be found out using index only.

# Note: if given something which changes dynamically and we have to find and after each operation
#  and if we have to combine(dynamically) , then must think once of  'disjoint set'.

# Application of DSU:
# 1) used to detect cycle in undirected or directed graph.
# 2) Find the no of connected components.
# 3) Helps in connecting the components into one by 'union'.
# 4) when we have to connect something based on some property & have to find ans from them then, must think of union find.
# 5) find the size of the largest component based on some property.(just find the largest size among parent).

# Note: while doing union, must pass an integer value only. If given in any other thing like string or coordinates or matrix form
# first try to convert them into an integer. Because for finding parent and size we need only number.
