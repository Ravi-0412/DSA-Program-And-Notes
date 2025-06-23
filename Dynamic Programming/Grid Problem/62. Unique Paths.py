# Recursive way:
# Time Complexity: O(2m*n)
# Note: No need to check for 'out of range' condition since it will get returned for m== 1 or n ==1 ' only.

# for base case, you can do like :
# if m == 1 and n ==1:
#     return 1

# if we write this as base case then we need to check for invalid condition.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m== 1 or n== 1: 
            # After reaching 1st row or 1st col there will be only one possible way i.e either go up or left.  
            return 1
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)

# Java Code 
"""
public class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 || n == 1)
            // After reaching 1st row or 1st col there will be only one possible way i.e either go up or left.
            return 1;
        return uniquePaths(m, n - 1) + uniquePaths(m - 1, n);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 1 || n == 1)
            // After reaching 1st row or 1st col there will be only one possible way i.e either go up or left.
            return 1;
        return uniquePaths(m, n - 1) + uniquePaths(m - 1, n);
    }
};
"""
# # method 2 : DP(memoization)
# time= space= O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0 for j in range(n+1)] for i in range(m+1)]  # will give no of ways to go from (i,j) to (0,0)
        return self.Paths(m, n, dp)  # we are starting from bottom-right(m, n) and trying to reach the starting grid(1,1)
    
    def Paths(self, m, n, dp):
        if n==1 or m==1:  # since we are starting from m and n so we will have to stop at 1,1
            dp[m][n]= 1
        if dp[m][n] != 0:
            return dp[m][n]
        dp[m][n]= self.Paths(m-1, n, dp) + self.Paths(m, n-1, dp)  # when you take left or when you take up
        return dp[m][n]

# Java Code 
"""
public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m + 1][n + 1];  // will give no of ways to go from (i,j) to (0,0)
        return paths(m, n, dp);  // we are starting from bottom-right(m, n) and trying to reach the starting grid(1,1)
    }

    private int paths(int m, int n, int[][] dp) {
        if (n == 1 || m == 1)  // since we are starting from m and n so we will have to stop at 1,1
            dp[m][n] = 1;
        if (dp[m][n] != 0)
            return dp[m][n];
        dp[m][n] = paths(m - 1, n, dp) + paths(m, n - 1, dp);  // when you take left or when you take up
        return dp[m][n];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));  // will give no of ways to go from (i,j) to (0,0)
        return paths(m, n, dp);  // we are starting from bottom-right(m, n) and trying to reach the starting grid(1,1)
    }

private:
    int paths(int m, int n, std::vector<std::vector<int>>& dp) {
        if (n == 1 || m == 1)  // since we are starting from m and n so we will have to stop at 1,1
            dp[m][n] = 1;
        if (dp[m][n] != 0)
            return dp[m][n];
        dp[m][n] = paths(m - 1, n, dp) + paths(m, n - 1, dp);  // when you take left or when you take up
        return dp[m][n];
    }
};
"""
# Tabulation
# Note vvi if m==n then : when you will make all sub-problems (n*n) as matrix , put the value in matrix.
# After that you will find that the ans matrix is a transpose matrix.

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0 for j in range(n+1)] for i in range(m+1)]
        for c in range(n+1):   # to mark '1' in row '1'
            dp[1][c]= 1
        for r in range(m+1):   # to mark '1' in col '1'
            dp[r][1]= 1
        for r in range(2, m+1):
            for c in range(2, n+1):
                dp[r][c]= dp[r][c-1] + dp[r-1][c]
        return dp[m][n]


# Java Code 
"""
public class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m + 1][n + 1];
        for (int c = 0; c <= n; c++)   // to mark '1' in row '1'
            dp[1][c] = 1;
        for (int r = 0; r <= m; r++)   // to mark '1' in col '1'
            dp[r][1] = 1;
        for (int r = 2; r <= m; r++) {
            for (int c = 2; c <= n; c++) {
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c];
            }
        }
        return dp[m][n];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));
        for (int c = 0; c <= n; ++c)   // to mark '1' in row '1'
            dp[1][c] = 1;
        for (int r = 0; r <= m; ++r)   // to mark '1' in col '1'
            dp[r][1] = 1;
        for (int r = 2; r <= m; ++r) {
            for (int c = 2; c <= n; ++c) {
                dp[r][c] = dp[r][c - 1] + dp[r - 1][c];
            }
        }
        return dp[m][n];
    }
};
"""
# optimising space complexity

# Note; Whenever you see like this : 'dp[r][c]= dp[r][c-1] + dp[r-1][c]'
# Means you can optmimise the space because we only need current and previous row value for 
# calculating value for current one. No need of whole 1d array.

# How to do?
# Just make 1d array where length = range of 2nd varibale , here range of 'c'.

# Note vvi:Whenever we create a new row ( say cur), 
# we need to explicitly set its first element or few elements according to our base condition.
# More in depth: Basically value of base for current row either only 1st ele or few ele whatever & how many 
# you have written in base case.

# note : In same way you can reduce 1D array to few variables.
# e.g: Fibonacci patterns questions

# time: O(m*n), space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre= [1 for i in range(n+1)]   # filling the 1st row value with '1'.
        for r in range(2, m+1):
            cur= [0]*(n+1)
            cur[1]= 1    # marking '1' in col no '1'.  
            for c in range(2, n+1):
                cur[c]= cur[c-1] + pre[c]
            pre= cur.copy()
        return pre[n]


# Java Code 
"""
public class Solution {
    public int uniquePaths(int m, int n) {
        int[] pre = new int[n + 1];   // filling the 1st row value with '1'.
        for (int i = 0; i <= n; i++)
            pre[i] = 1;

        for (int r = 2; r <= m; r++) {
            int[] cur = new int[n + 1];
            cur[1] = 1;    // marking '1' in col no '1'.
            for (int c = 2; c <= n; c++) {
                cur[c] = cur[c - 1] + pre[c];
            }
            pre = cur.clone();
        }

        return pre[n];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<int> pre(n + 1, 1);   // filling the 1st row value with '1'.

        for (int r = 2; r <= m; ++r) {
            std::vector<int> cur(n + 1, 0);
            cur[1] = 1;    // marking '1' in col no '1'.
            for (int c = 2; c <= n; ++c) {
                cur[c] = cur[c - 1] + pre[c];
            }
            pre = cur;
        }

        return pre[n];
    }
};
"""
# Now print all the paths also
# in case of string you don't have to push or pop like array because string is immutable i.e 
# it can't be changed auto when you will change in nay other function call.
def ways2(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1
    right,down= 0,0
    if c<=m:
        right= ways2(r,c+1,m,n,path+"R")    # R: Right
    if r<=n:
        down= ways2(r+1,c,m,n,path+"D")     # D: down
    return right + down

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,""))


# concise way of writing the above code.
# write all the invalid cases as base case then after that simply call the next function.
def ways2(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1  # telling the no of ways
    if r >m or c > n:  # invalid case
        return 0
    return ways2(r,c+1,m,n,path+"R") + ways2(r+1,c,m,n,path+"D")   # Right and Down

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,""))

# my mistakes
def ways2(r,c,m,n,path):
    if r==m or c==n:  # my mistake: you have to reach end point for printing the path
        print("".join(path))
        return 1
    path.append('R')
    # r= ways2(r,c+1,m,n,path)   # my mistake, i was storing ans in same var name as passes in parameter by mistake
    right= ways2(r,c+1,m,n,path)
    path.pop()
    path.append('D')
    down= ways2(r+1,c,m,n,path)  
    return right + down

# print("path :")
# print("path no of ways: ",ways2(0,0,2,2,[]))

# Q: you are allowed to go diagonally also
def ways4(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1
    diagonal,right,down= 0,0,0
    if r<=m and c<=n: #   D:diagonal, incr row and col both by 1
        diagonal= ways4(r+1,c+1,m,n,path+"D")   
    if c<=n:
        right= ways4(r,c+1,m,n,path+"H")       # H: horizonatl
    if r<=m:
        down= ways4(r+1,c,m,n,path+"V")       # V: vertical
    return diagonal+ right + down

# print("path :")
# print("path no of ways: ",ways4(0,0,2,2,""))
# print("path no of ways: ",ways4(0,0,1,1,""))

# concise way of writing above code.
def ways4(r,c,m,n,path):
    if r==m and c==n:
        print(path)
        return 1
    if r > m or c > n:
        return 0
    return ways4(r+1,c+1,m,n,path+"D")  + ways4(r,c+1,m,n,path+"H") + ways4(r+1,c,m,n,path+"V") # Diagonal, Horizontal, Verical

print("path :")
print("path no of ways: ",ways4(0,0,2,2,""))
# print("path no of ways: ",ways4(0,0,1,1,""))



# Java Code 
"""
public class GridPath1 {
    // Now print all the paths also
    // in case of string you don't have to push or pop like array because string is immutable i.e 
    // it can't be changed auto when you will change in any other function call.
    public static int ways2(int r, int c, int m, int n, String path) {
        if (r == m && c == n) {
            System.out.println(path);
            return 1;
        }
        int right = 0, down = 0;
        if (c <= m) {
            right = ways2(r, c + 1, m, n, path + "R");  // R: Right
        }
        if (r <= n) {
            down = ways2(r + 1, c, m, n, path + "D");   // D: down
        }
        return right + down;
    }
}
// concise way of writing the above code.
// write all the invalid cases as base case then after that simply call the next function.
public class GridPath2 {
    public static int ways2(int r, int c, int m, int n, String path) {
        if (r == m && c == n) {
            System.out.println(path);
            return 1;  // telling the no of ways
        }
        if (r > m || c > n) {  // invalid case
            return 0;
        }
        return ways2(r, c + 1, m, n, path + "R") + ways2(r + 1, c, m, n, path + "D"); // Right and Down
    }
}
// my mistakes
import java.util.*;

public class GridPath3 {
    public static int ways2(int r, int c, int m, int n, List<Character> path) {
        if (r == m || c == n) {  // my mistake: you have to reach end point for printing the path
            for (char ch : path) {
                System.out.print(ch);
            }
            System.out.println();
            return 1;
        }
        path.add('R');
        int right = ways2(r, c + 1, m, n, path);
        path.remove(path.size() - 1);
        path.add('D');
        int down = ways2(r + 1, c, m, n, path);
        path.remove(path.size() - 1);
        return right + down;
    }
}
// Q: you are allowed to go diagonally also
//concise way 
public class GridPath4 {
    // Q: you are allowed to go diagonally also
    public static int ways4(int r, int c, int m, int n, String path) {
        if (r == m && c == n) {
            System.out.println(path);
            return 1;
        }
        if (r > m || c > n) {
            return 0;
        }
        return ways4(r + 1, c + 1, m, n, path + "D") +  // Diagonal
               ways4(r, c + 1, m, n, path + "H") +     // Horizontal
               ways4(r + 1, c, m, n, path + "V");       // Vertical
    }
}

"""
# C++ Code 
"""
#include <iostream>
using namespace std;

// Now print all the paths also
// in case of string you don't have to push or pop like array because string is immutable i.e 
// it can't be changed auto when you will change in any other function call.
int ways2(int r, int c, int m, int n, string path) {
    if (r == m && c == n) {
        cout << path << endl;
        return 1;
    }
    int right = 0, down = 0;
    if (c <= m) {
        right = ways2(r, c + 1, m, n, path + "R");  // R: Right
    }
    if (r <= n) {
        down = ways2(r + 1, c, m, n, path + "D");   // D: down
    }
    return right + down;
}
// concise way of writing the above code.
// write all the invalid cases as base case then after that simply call the next function.
int ways2(int r, int c, int m, int n, string path) {
    if (r == m && c == n) {
        cout << path << endl;
        return 1;  // telling the no of ways
    }
    if (r > m || c > n) {  // invalid case
        return 0;
    }
    return ways2(r, c + 1, m, n, path + "R") + ways2(r + 1, c, m, n, path + "D"); // Right and Down
}
// my mistakes
#include <iostream>
#include <vector>
using namespace std;

int ways2(int r, int c, int m, int n, vector<char>& path) {
    if (r == m || c == n) {  // my mistake: you have to reach end point for printing the path
        for (char ch : path) {
            cout << ch;
        }
        cout << endl;
        return 1;
    }
    path.push_back('R');
    int right = ways2(r, c + 1, m, n, path);
    path.pop_back();
    path.push_back('D');
    int down = ways2(r + 1, c, m, n, path);
    path.pop_back();
    return right + down;
}
// Q: you are allowed to go diagonally also
//concise way
int ways4(int r, int c, int m, int n, string path) {
    if (r == m && c == n) {
        cout << path << endl;
        return 1;
    }
    if (r > m || c > n) {
        return 0;
    }
    return ways4(r + 1, c + 1, m, n, path + "D") +  // Diagonal
           ways4(r, c + 1, m, n, path + "H") +     // Horizontal
           ways4(r + 1, c, m, n, path + "V");       // Vertical
}

"""