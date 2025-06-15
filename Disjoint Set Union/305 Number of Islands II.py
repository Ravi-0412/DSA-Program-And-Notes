# Method 1: 

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
    def numIslands2(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        n= rows * cols   # total no of cell 
        dsu = DSU(n)
        count = 0  # har operation se phle 'ans' btayega. 
        # Har operator ke bad 'count' ko incement karnenge for 'given cell' and then adjacent wale ko check karenge, 
        # agar wala bhi ek island h then uske saath merge hoga and count to ek decrease karenge. 
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


# Java
"""
import java.util.*;

class DSU {
    int[] parent, size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]);  // path compression
    }

    public boolean unionBySize(int n1, int n2) {
        int p1 = findUPar(n1), p2 = findUPar(n2);
        if (p1 == p2) return false;  // we can't do union since they belong to the same component.
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;  // means we can merge the lands
    }
}

class Solution {
    public List<Integer> numIslands2(int rows, int cols, int[][] operators) {
        int[][] matrix = new int[rows][cols];
        int n = rows * cols;  // total number of cells
        DSU dsu = new DSU(n);
        int count = 0;
        List<Integer> ans = new ArrayList<>();

        for (int[] op : operators) {
            int r = op[0], c = op[1];
            int ind = r * cols + c;

            // first check if this cell has already been visited
            if (matrix[r][c] == 1) {
                ans.add(count);
                continue;  // no need to check directions in this case
            }

            // now check if we can merge this current land with any of the four adjacent lands
            // and keep reducing the count by 1 wherever we can merge
            count++;

            // 1) going left
            if (c - 1 >= 0 && matrix[r][c - 1] == 1 && dsu.unionBySize(ind, ind - 1)) {
                count--;
            }
            // 2) going right
            if (c + 1 < cols && matrix[r][c + 1] == 1 && dsu.unionBySize(ind, ind + 1)) {
                count--;
            }
            // 3) going up
            if (r - 1 >= 0 && matrix[r - 1][c] == 1 && dsu.unionBySize(ind, ind - cols)) {
                count--;
            }
            // 4) going down
            if (r + 1 < rows && matrix[r + 1][c] == 1 && dsu.unionBySize(ind, ind + cols)) {
                count--;
            }

            ans.add(count);
            matrix[r][c] = 1;  // update the cell as visited (land)
        }

        return ans;
    }
}
"""


# C++
"""
#include <vector>
using namespace std;

class DSU {
public:
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }

    int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]);  // path compression
    }

    bool unionBySize(int n1, int n2) {
        int p1 = findUPar(n1), p2 = findUPar(n2);
        if (p1 == p2) return false;  // we can't do union since they belong to the same component.
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;  // means we can merge the lands
    }
};

class Solution {
public:
    vector<int> numIslands2(int rows, int cols, vector<vector<int>>& operators) {
        vector<vector<int>> matrix(rows, vector<int>(cols, 0));
        int n = rows * cols;
        DSU dsu(n);
        int count = 0;
        vector<int> ans;

        for (auto& op : operators) {
            int r = op[0], c = op[1];
            int ind = r * cols + c;

            // first check if this cell has already been visited
            if (matrix[r][c] == 1) {
                ans.push_back(count);
                continue;  // no need to check directions in this case
            }

            // now check if we can merge this current land with any of the four adjacent lands
            // and keep reducing the count by 1 wherever we can merge
            count++;

            // 1) going left
            if (c - 1 >= 0 && matrix[r][c - 1] == 1 && dsu.unionBySize(ind, ind - 1)) {
                count--;
            }
            // 2) going right
            if (c + 1 < cols && matrix[r][c + 1] == 1 && dsu.unionBySize(ind, ind + 1)) {
                count--;
            }
            // 3) going up
            if (r - 1 >= 0 && matrix[r - 1][c] == 1 && dsu.unionBySize(ind, ind - cols)) {
                count--;
            }
            // 4) going down
            if (r + 1 < rows && matrix[r + 1][c] == 1 && dsu.unionBySize(ind, ind + cols)) {
                count--;
            }

            ans.push_back(count);
            matrix[r][c] = 1;  // mark the land
        }

        return ans;
    }
};
"""
    

# Method 2: 
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
    def numIslands2(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        
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
    

# Java
"""
import java.util.*;

class DSU {
    int[] parent, size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]);  // path compression
    }

    public boolean unionBySize(int n1, int n2) {
        int p1 = findUPar(n1), p2 = findUPar(n2);
        if (p1 == p2) return false;  // we can't do union since they belong to the same component.
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;  // means we can merge the lands
    }
}

class Solution {
    private boolean isValid(int r, int c, int rows, int cols) {
        if (r >= 0 && r < rows && c >= 0 && c < cols)
            return true;
        return false;
    }

    public List<Integer> numIslands2(int rows, int cols, int[][] operators) {
        int n = rows * cols;  // total number of cells
        DSU dsu = new DSU(n);
        int count = 0;
        List<Integer> ans = new ArrayList<>();
        Set<String> visited = new HashSet<>();  // land we have visited till now

        for (int[] op : operators) {
            int r = op[0], c = op[1];
            int ind = r * cols + c;  // index number

            // first check if this land is already visited
            String key = r + "," + c;
            if (visited.contains(key)) {
                ans.add(count);
                continue;
            }

            count++;

            // now check in all four directions
            int[][] directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}};  // left, right, up, down
            for (int[] dir : directions) {
                int dr = dir[0], dc = dir[1];
                int ind1 = dr * cols + dc;  // calculating the index number

                String neighborKey = dr + "," + dc;
                if (isValid(dr, dc, rows, cols) && visited.contains(neighborKey) && dsu.unionBySize(ind, ind1)) {
                    count--;
                }
            }

            ans.add(count);
            visited.add(key);
        }

        return ans;
    }
}


"""


# C++
"""
#include <vector>
#include <set>
#include <string>
#include <sstream>
using namespace std;

class DSU {
public:
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n);
        size.assign(n, 1);
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }

    int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]);  // path compression
    }

    bool unionBySize(int n1, int n2) {
        int p1 = findUPar(n1), p2 = findUPar(n2);
        if (p1 == p2) return false;  // we can't do union since they belong to the same component.
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;  // means we can merge the lands
    }
};

class Solution {
    bool isValid(int r, int c, int rows, int cols) {
        if (r >= 0 && r < rows && c >= 0 && c < cols)
            return true;
        return false;
    }

    string key(int r, int c) {
        return to_string(r) + "," + to_string(c);
    }

public:
    vector<int> numIslands2(int rows, int cols, vector<vector<int>>& operators) {
        int n = rows * cols;  // total number of cells
        DSU dsu(n);
        int count = 0;
        vector<int> ans;
        set<string> visited;  // land we have visited till now

        for (auto& op : operators) {
            int r = op[0], c = op[1];
            int ind = r * cols + c;  // index number

            string currKey = key(r, c);
            // first check if this land is already visited
            if (visited.count(currKey)) {
                ans.push_back(count);
                continue;
            }

            count++;

            // now check in all four directions
            vector<pair<int, int>> directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}};  // left, right, up, down
            for (auto& dir : directions) {
                int dr = dir.first, dc = dir.second;
                int ind1 = dr * cols + dc;  // calculating the index number

                string neighborKey = key(dr, dc);
                if (isValid(dr, dc, rows, cols) && visited.count(neighborKey) && dsu.unionBySize(ind, ind1)) {
                    count--;
                }
            }

            ans.push_back(count);
            visited.insert(currKey);
        }

        return ans;
    }
};


"""