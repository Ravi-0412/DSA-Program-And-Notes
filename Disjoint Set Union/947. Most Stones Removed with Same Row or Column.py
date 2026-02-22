# Method 2: 
"""
logic: we can remove any stone if it has either same row or same col with remaining stone.
Reducing: So we can combine all stones having same row or same col into components.
After that we can delete all stones from the all components except 1 i.e 
for each component (distinct parent or node is parent of itself), find the size of the node and if size is greater than >1
delete all stones equal to 'size-1'. 

One sentence to solve:
Connected stones can be reduced to 1 stone,
the maximum stones can be removed = stones number - islands number.
so just count the number of "islands".

Time Complexity : O(n^2 * alpha(n))
Space : O(n)
"""

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n= len(stones)
        dsu= DSU(n)    # passing 'n' only as we have to check only 'n' stones. so no need to take dimension and all.
        # first form components from stone.
        for i in range(n):
            x1, y1= stones[i]
            for j in range(n):
                x2, y2= stones[j]
                if x1== x2 or y1== y2 :
                    dsu.unionBySize(i, j)
        # Now delete stones from component.
        count= 0
        for p in range(n):
            if p== dsu.parent[p] and dsu.size[p] > 1:
                count+= dsu.size[p] - 1
        return count

# Method 2:
"""
Most optimised one
Logic: Instead of stones being nodes, think of Rows and Columns as nodes. If a stone is at (r, c), it connects Row r and Column c.

Total Removed = Total Stones - Total Components
Every connected component of stones will eventually be reduced to exactly 1 stone. 
So, if we have C components, C stones remain. The rest N - C are removed.

i)For a stone at (r, c), we "Union" the identifier for row r and column c.
ii) The Challenge: How to distinguish row 0 from column 0?
The Trick: Offset the columns. Since x_i, y_i  <= 10,000, we can treat column c as c + 10,001. Now, row 0 and column 0 have unique IDs.

Time : O(N * alpha(V)) , where N is stones and V is unique rows/cols.
Space : O(V), To store the parent pointers of active rows and columns.

Benefits of this on array and initialising early like method 1 or earlier way that i was doing n other Q:
"""
self.parent = {}
 # Tracks the number of separate "islands" (connected components).
 self.num_components = 0

Ans:
1. Handling Sparse Data (Memory Efficiency)
If the coordinate range is 0 to 10,000, an array requires 20,002 slots regardless of whether you have 2 stones or 2,000.
Array: Always O(Range}). If coordinates were 10^9 (like in some "Hard" variations), your program would crash or run out of memory.
Dictionary: Always O(N), where N is the number of actual rows and columns used. It only stores what it needs.

Feature:           Pre-allocated Array                       Dictionary (Lazy Init)
Space,             O(Max_Coordinate),                        O(Stones)
Setup Time         O(Max_Coordinate),                        O(1)
Flexibility        Rigid (Integers only),                    "Flexible (Strings, Large numbers)"
Performance        Slightly faster (Direct indexing)          Slightly slower (Hashing)


"""

class DSU:
    def __init__(self):
        # Maps node -> parent. Using a dict handles sparse coordinates efficiently.
        self.parent = {}
        # Tracks the number of separate "islands" (connected components).
        self.num_components = 0

    def find(self, n):
        # 1. Lazy Initialization: Create node on-the-fly when first seen.
        if n not in self.parent:
            self.parent[n] = n
            self.num_components += 1
            return n
        
        # 2. Base Case: If n is its own parent, it's the root.
        if n == self.parent[n]:
            return n
            
        # 3. Path Compression: Point node directly to root to flatten the tree.
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        # If they have different roots, they are in different components.
        if p1 != p2:
            # Merge one component into the other.
            self.parent[p1] = p2
            # One component disappears as it merges.
            self.num_components -= 1

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        uf = DSU()
        for r, c in stones:
            # A stone at (r, c) connects 'Row r' and 'Col c'.
            # Offset 'c' by 10001 so 'Row 0' and 'Col 0' are distinct nodes.
            uf.union(r, c + 10001)
        
        # Every component will leave exactly 1 stone behind.
        return len(stones) - uf.num_components
