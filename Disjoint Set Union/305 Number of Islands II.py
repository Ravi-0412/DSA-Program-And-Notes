# my mistake: I thought correct but made some minor mistakes like:
# 1.1)  i was thinking that count will increase or will be same as previous operation always..(what the fuck)..
# if we are putting the nodes in between land then it will decrease also.
# it may increase or decrease, it depends on position we are inserting.

# 1.2) was checking if in any of four direction we can merge.And for all combined together i was decr the count by '1'.
# but in every possible direction if we can merge then we should decr the count by '1'.

# 2) cell could have repeat in the input, but i was not considering that.
# 3) was changing the land value(input) to '1' at start itself.

# Difference from 'No of island 1': We have count after each operation

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n] = self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1 == p2:   # we can't do union since they belong to the same component.
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2  
            self.size[p2] += self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2] = p1   
            self.size[p1] += self.size[p2]
        return True  # means we can merge the lands

class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        n= rows * cols   # total no of cell 
        dsu = DSU(n)
        count = 0
        ans = []
        for r,c in operators:
            # matrix[r][c]= 1
            ind = r* cols + c
        
            # first check if there is already this cell has value == 1(already occured before)
            if matrix[r][c] == 1:
                ans.append(count)
                continue   # no need to check directions in this case.

            # now check if we can merge this curr land with any of the four adjacent land.
            # and keep reducing the count by '1' wherever you can merge.
            count+= 1
            # 1) going left
            if c -1 >=0 and  matrix[r][c-1]== 1 and dsu.unionBySize(ind, ind -1):
                count -= 1
            # 2) going right
            if c+1 < cols and  matrix[r][c+1]== 1 and  dsu.unionBySize(ind, ind +1):
                count -= 1
            # 3) going up
            if r-1 >= 0 and  matrix[r-1][c]== 1 and dsu.unionBySize(ind, ind - cols):
                count -= 1
            # 3) going down
            if r+1 < rows and  matrix[r+1][c]== 1 and dsu.unionBySize(ind, ind + cols):
                count -= 1 
            ans.append(count)
            matrix[r][c]= 1    # update the value for input
        return ans

# concise and better way of writing above code.
# logic: no need to create the matrix, just store the input in a set say visited.

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
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        return True  # means we can merge the lands

from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        
        def isValid(r, c):
            if r >= 0 and r < rows and c >= 0 and c< cols:
                return True
            return False
        
        n= rows * cols   # total no of cell 
        dsu= DSU(n)
        count= 0
        ans= []
        visited= set()  # land we have till now visited will be stored here
        for r,c in operators:
            ind= r* cols + c   # index number
            # print(ind, "index")
            
            # first check if this land is already visited.
            if (r,c) in visited:
                ans.append(count)
                continue
            count+= 1
            # now check in all four directions
            directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left, right, up, down
            for dr, dc in directions:
                ind1 = dr * cols + dc   # calculating the index number
                if isValid(dr, dc) and (dr, dc) in visited and dsu.unionBySize(ind, ind1):
                    count-= 1
                    
            ans.append(count)
            visited.add((r,c))
        return ans
    