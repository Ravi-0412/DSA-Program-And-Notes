# Method 1: 

"""
Q meaning: you have to return all that grid in a 2D matrix from which water can flow to both pacific and atlantic ocean
we are going reverse i.e from ocean to the cells
so curr height of cell should be >= preHeight of the cell
logic: find the cell that can reach the pacific and atlantic respectively and 
at last find the cell that can reach both and add them into the ans

very better logic as we are going from ocean to the cell then for next adjacent node, 
we will have to check with height of preCell only, if height >= to  preCell than the curr cell can also reach the respective ocean
exactly  same as "No of island", only change in height checking condition

time: O(m*n), space: O(m*n)
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col= len(heights), len(heights[0])
        pac, atl= set(),set()
        
        def DFS(r,c,visited,preHeight):
            if r<0 or r>=row or c<0 or c>=col or (r,c) in visited or heights[r][c] < preHeight:
                return
            # now means this cell can reach the ocean so add in the visited 
            visited.add((r,c))
            directions= [[-1,0],[1,0],[0,-1],[0,1]]    # up,down,left,right
            for dr,dc in directions:
                r1,c1= r+dr, c+dc
                DFS(r1,c1,visited,heights[r][c])
        
        # code starts from here
        # cells that are in the 1st and last row can reach the pacific and atlantic respectively
        for c in range(col):
            DFS(0, c, pac, heights[0][c])  # 1st row. since equal distance is also allowed so passed the height of 1st cell as preHeight
            DFS(row-1, c, atl,heights[row-1][c])  # last row
            
        # cells that are in the 1st  and last col can reach the pacific and atlantic respectively   
        for r in range(row):
            DFS(r, 0, pac, heights[r][0])           # 1st column
            DFS(r, col-1, atl, heights[r][col-1])   # last column

        # now find out the cells that are present in both pacific and atlantic cell and them into ans
        return list(pac & atl)    # Take intersection of both sets



# Java
"""
import java.util.*;

class Solution {
    int row, col;
    int[][] heights;
    boolean[][] pac, atl;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        this.heights = heights;
        row = heights.length;
        col = heights[0].length;
        pac = new boolean[row][col];
        atl = new boolean[row][col];

        // cells that are in the 1st and last row can reach the pacific and atlantic respectively
        for (int c = 0; c < col; c++) {
            DFS(0, c, pac, heights[0][c]);         // 1st row
            DFS(row - 1, c, atl, heights[row - 1][c]);  // last row
        }

        // cells that are in the 1st and last col can reach the pacific and atlantic respectively
        for (int r = 0; r < row; r++) {
            DFS(r, 0, pac, heights[r][0]);         // 1st column
            DFS(r, col - 1, atl, heights[r][col - 1]); // last column
        }

        // now find out the cells that are present in both pacific and atlantic cell and them into ans
        List<List<Integer>> ans = new ArrayList<>();
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (pac[r][c] && atl[r][c]) {
                    ans.add(Arrays.asList(r, c));
                }
            }
        }
        return ans;
    }

    void DFS(int r, int c, boolean[][] visited, int preHeight) {
        if (r < 0 || r >= row || c < 0 || c >= col || visited[r][c] || heights[r][c] < preHeight) {
            return;
        }
        // now means this cell can reach the ocean so add in the visited
        visited[r][c] = true;
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}}; // up, down, left, right
        for (int[] d : directions) {
            int r1 = r + d[0], c1 = c + d[1];
            DFS(r1, c1, visited, heights[r][c]);
        }
    }
}


"""


# C++
"""
#include <vector>
using namespace std;

class Solution {
    int row, col;
    vector<vector<int>> heights;
    vector<vector<bool>> pac, atl;

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        this->heights = heights;
        row = heights.size();
        col = heights[0].size();
        pac = vector<vector<bool>>(row, vector<bool>(col, false));
        atl = vector<vector<bool>>(row, vector<bool>(col, false));

        // cells that are in the 1st and last row can reach the pacific and atlantic respectively
        for (int c = 0; c < col; ++c) {
            DFS(0, c, pac, heights[0][c]);         // 1st row
            DFS(row - 1, c, atl, heights[row - 1][c]); // last row
        }

        // cells that are in the 1st and last col can reach the pacific and atlantic respectively
        for (int r = 0; r < row; ++r) {
            DFS(r, 0, pac, heights[r][0]);         // 1st column
            DFS(r, col - 1, atl, heights[r][col - 1]); // last column
        }

        // now find out the cells that are present in both pacific and atlantic cell and them into ans
        vector<vector<int>> ans;
        for (int r = 0; r < row; ++r) {
            for (int c = 0; c < col; ++c) {
                if (pac[r][c] && atl[r][c]) {
                    ans.push_back({r, c});
                }
            }
        }
        return ans;
    }

private:
    void DFS(int r, int c, vector<vector<bool>>& visited, int preHeight) {
        if (r < 0 || r >= row || c < 0 || c >= col || visited[r][c] || heights[r][c] < preHeight) {
            return;
        }
        // now means this cell can reach the ocean so add in the visited
        visited[r][c] = true;
        vector<pair<int, int>> directions = {{-1,0},{1,0},{0,-1},{0,1}}; // up, down, left, right
        for (auto [dr, dc] : directions) {
            int r1 = r + dr, c1 = c + dc;
            DFS(r1, c1, visited, heights[r][c]);
        }
    }
};


"""