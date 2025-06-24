# Method 1: 

# Q) You are allowed to move left, right, up, down. False means 'obstacle is there' and True means 'no obstacle'
# will count and print the path as well
# same approach if obstacles are also there

class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        if not maze or maze[0][0] == 0 or maze[-1][-1] == 0:
            return []  # no possible path if start or end is blocked

        n = len(maze)
        res = []

        def Paths(ans, maze, row, col):
            if row == n - 1 and col == n - 1:  # corner most will be only the base condition in this case
                res.append(ans)
                return 1

            # writing all the invalid case together
            if row < 0 or row >= n or col < 0 or col >= n or maze[row][col] == 0:
                return 0

            # if not false, make it 'false' 
            # since i am considering this cell for my paths
            maze[row][col] = 0  # made it false so again we don't repeat this cell in same path

            # Try all four directions
            Paths(ans + 'D', maze, row + 1, col)   # Down
            Paths(ans + 'R', maze, row, col + 1)   # Right
            Paths(ans + 'U', maze, row - 1, col)   # Up
            Paths(ans + 'L', maze, row, col - 1)   # Left

            # since now the function is returning back so restore the changes made by the this
            # function call while going down
            maze[row][col] = 1
            return 0

        Paths("", maze, 0, 0)
        return sorted(res)

# Java Code 
"""
import java.util.*;

public class Solution {
    // Function to find all possible paths
    public List<String> ratInMaze(int[][] maze) {
        if (maze == null || maze.length == 0 || maze[0][0] == 0 || maze[maze.length - 1][maze[0].length - 1] == 0)
            return new ArrayList<>();  // no possible path if start or end is blocked

        int n = maze.length;
        List<String> res = new ArrayList<>();
        paths("", maze, 0, 0, res, n);
        Collections.sort(res);
        return res;
    }

    public int paths(String ans, int[][] maze, int row, int col, List<String> res, int n) {
        if (row == n - 1 && col == n - 1) {  // corner most will be only the base condition in this case
            res.add(ans);
            return 1;
        }

        // writing all the invalid case together
        if (row < 0 || row >= n || col < 0 || col >= n || maze[row][col] == 0)
            return 0;

        // if not false, make it 'false' 
        // since i am considering this cell for my paths
        maze[row][col] = 0;  // made it false so again we don't repeat this cell in same path

        // Try all four directions
        paths(ans + "D", maze, row + 1, col, res, n);   // Down
        paths(ans + "R", maze, row, col + 1, res, n);   // Right
        paths(ans + "U", maze, row - 1, col, res, n);   // Up
        paths(ans + "L", maze, row, col - 1, res, n);   // Left

        // since now the function is returning back so restore the changes made by the this
        // function call while going down
        maze[row][col] = 1;
        return 0;
    }

    public static void main(String[] args) {
        int[][] maze = {
            {1, 0, 0},
            {1, 1, 0},
            {1, 1, 1}
        };
        Solution sol = new Solution();
        System.out.println(sol.ratInMaze(maze));
    }
}
"""

# C++ Code
"""
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Function to find all possible paths
void paths(string ans, vector<vector<int>>& maze, int row, int col, vector<string>& res, int n) {
    if (row == n - 1 && col == n - 1) {  // corner most will be only the base condition in this case
        res.push_back(ans);
        return;
    }

    // writing all the invalid case together
    if (row < 0 || row >= n || col < 0 || col >= n || maze[row][col] == 0)
        return;

    // if not false, make it 'false' 
    // since i am considering this cell for my paths
    maze[row][col] = 0;  // made it false so again we don't repeat this cell in same path

    // Try all four directions
    paths(ans + "D", maze, row + 1, col, res, n);   // Down
    paths(ans + "R", maze, row, col + 1, res, n);   // Right
    paths(ans + "U", maze, row - 1, col, res, n);   // Up
    paths(ans + "L", maze, row, col - 1, res, n);   // Left

    // since now the function is returning back so restore the changes made by the this
    // function call while going down
    maze[row][col] = 1;
}

vector<string> ratInMaze(vector<vector<int>> maze) {
    int n = maze.size();
    vector<string> res;
    if (n == 0 || maze[0][0] == 0 || maze[n - 1][n - 1] == 0)
        return res;  // no possible path if start or end is blocked

    paths("", maze, 0, 0, res, n);
    sort(res.begin(), res.end());
    return res;
}

int main() {
    vector<vector<int>> maze = {
        {1, 0, 0},
        {1, 1, 0},
        {1, 1, 1}
    };
    vector<string> result = ratInMaze(maze);
    for (const auto& path : result) cout << path << endl;
}
"""
# Extension

# Q)   print all the separate path in a matrix for same Q i.e:
# mark the no 1,2,3,4.... as you traverse the path to reach the destination
def Paths_Matrix(ans, maze, row, col,matrix,step):  # step will increase in each rec call
    if row== len(maze)-1 and col== len(maze[0])-1:  # after reaching the base condition just print the matrix
        matrix[row][col]= step  # last step will be also a step
        for num in matrix:
            print(num)
        print(ans)
        print()
        return     
    if not maze[row][col]:  # if false then simply return
        return 
    # if not false, make it 'false' 
    # since i am considering this cell for my paths
    maze[row][col]= False
    temp = matrix[row][col]
    matrix[row][col]= step  # means you are now using the cell,so write the value of step in that cell

    if row< len(maze)-1:  # then only you can go down
        Paths_Matrix(ans+ 'D', maze, row+1, col,matrix,step+1)
    if col< len(maze[0])-1:  # then only you can go right
        Paths_Matrix(ans+ 'R', maze, row, col+1,matrix,step+1)
    if row >0:  # Then only you can go up
        Paths_Matrix(ans+ 'U', maze, row-1, col,matrix,step+1)
    if col>0:  # Then only you can go left
        Paths_Matrix(ans+ 'L', maze, row, col-1,matrix,step+1)

    # since now the function is returning back so restore the changes made by the this
    # function call while going down

    maze[row][col]= True
    matrix[row][col]= temp  # when you traverse back restore the value of step like pre Q
                        # So that for another function get the original matrix(back tracking)
    

maze= [[True,True,True],[True,True,True],[True,True,True]]
path_matrix= [[0 for j in range(len(maze[0]))] for i in range(len(maze))]  # make a matrix same size as input
print(path_matrix)
Paths_Matrix("",maze,0,0,path_matrix,1)   #step will be initially 1

# Java Code 
"""
import java.util.*;

public class MazePathsMatrix {

    // step will increase in each rec call
    public static void Paths_Matrix(String ans, boolean[][] maze, int row, int col, int[][] matrix, int step) {
        if (row == maze.length - 1 && col == maze[0].length - 1) {  // after reaching the base condition just print the matrix
            matrix[row][col] = step;  // last step will be also a step
            for (int[] arr : matrix)
                System.out.println(Arrays.toString(arr));
            System.out.println(ans + "\n");
            return;
        }

        if (!maze[row][col])  // if false then simply return
            return;

        // if not false, make it 'false' 
        // since i am considering this cell for my paths
        maze[row][col] = false;
        int temp = matrix[row][col];
        matrix[row][col] = step;  // means you are now using the cell, so write the value of step in that cell

        if (row < maze.length - 1)  // then only you can go down
            Paths_Matrix(ans + 'D', maze, row + 1, col, matrix, step + 1);
        if (col < maze[0].length - 1)  // then only you can go right
            Paths_Matrix(ans + 'R', maze, row, col + 1, matrix, step + 1);
        if (row > 0)  // Then only you can go up
            Paths_Matrix(ans + 'U', maze, row - 1, col, matrix, step + 1);
        if (col > 0)  // Then only you can go left
            Paths_Matrix(ans + 'L', maze, row, col - 1, matrix, step + 1);

        // since now the function is returning back so restore the changes made by this
        // function call while going down
        maze[row][col] = true;
        matrix[row][col] = temp;  // restore the value of step like pre Q for backtracking
    }

    public static void main(String[] args) {
        boolean[][] maze = {
            {true, true, true},
            {true, true, true},
            {true, true, true}
        };
        int[][] matrix = new int[maze.length][maze[0].length];  // make a matrix same size as input
        System.out.println(Arrays.deepToString(matrix));
        Paths_Matrix("", maze, 0, 0, matrix, 1);  // step will be initially 1
    }
}
"""

# C++ Code
"""
#include <iostream>
#include <vector>
using namespace std;

// step will increase in each rec call
void Paths_Matrix(string ans, vector<vector<bool>>& maze, int row, int col, vector<vector<int>>& matrix, int step) {
    int n = maze.size(), m = maze[0].size();

    if (row == n - 1 && col == m - 1) {  // after reaching the base condition just print the matrix
        matrix[row][col] = step;  // last step will be also a step
        for (const auto& rowVec : matrix) {
            for (int val : rowVec) cout << val << " ";
            cout << endl;
        }
        cout << ans << "\n\n";
        return;
    }

    if (!maze[row][col])  // if false then simply return
        return;

    // if not false, make it 'false' 
    // since i am considering this cell for my paths
    maze[row][col] = false;
    int temp = matrix[row][col];
    matrix[row][col] = step;  // means you are now using the cell, so write the value of step in that cell

    if (row < n - 1)  // then only you can go down
        Paths_Matrix(ans + 'D', maze, row + 1, col, matrix, step + 1);
    if (col < m - 1)  // then only you can go right
        Paths_Matrix(ans + 'R', maze, row, col + 1, matrix, step + 1);
    if (row > 0)  // Then only you can go up
        Paths_Matrix(ans + 'U', maze, row - 1, col, matrix, step + 1);
    if (col > 0)  // Then only you can go left
        Paths_Matrix(ans + 'L', maze, row, col - 1, matrix, step + 1);

    // since now the function is returning back so restore the changes made by this
    // function call while going down
    maze[row][col] = true;
    matrix[row][col] = temp;  // restore the value of step like pre Q for backtracking
}

int main() {
    vector<vector<bool>> maze(3, vector<bool>(3, true));
    vector<vector<int>> matrix(3, vector<int>(3, 0));  // make a matrix same size as input

    for (const auto& row : matrix) {
        for (int val : row) cout << val << " ";
        cout << endl;
    }

    Paths_Matrix("", maze, 0, 0, matrix, 1);  // step will be initially 1
}
"""
