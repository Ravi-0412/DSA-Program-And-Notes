"""

Flood fill replaces the color of a starting pixel and all connected pixels (4-directionally)
with the same original color with a new color.

Example Image (2D grid):
    1 1 1
    1 1 0
    1 0 1

Start pixel: (1,1)
New color: 2

Result after flood fill:
    2 2 2
    2 2 0
    2 0 1

Note:
- Only pixels connected 4-directionally (up, down, left, right) with the original color are filled.
- Diagonal connections are NOT considered.

"""
from collections import deque
from copy import deepcopy
def flood_fill_dfs(image, sr, sc, newColor):
    """
    Perform flood fill using DFS (Depth First Search).

    Args:
        image (List[List[int]]): 2D grid representing the image.
        sr (int): Starting pixel row.
        sc (int): Starting pixel column.
        newColor (int): New color to fill.

    Returns:
        List[List[int]]: Modified image after flood fill.
    """
    ans = deepcopy(image)
    n, m = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == newColor:
        return ans

    def dfs(row, col):
        ans[row][col] = newColor
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] != newColor and image[nr][nc] == original_color:
                dfs(nr, nc)

    dfs(sr, sc)
    return ans

def flood_fill_bfs(image, sr, sc, newColor):
    """
    Perform flood fill using BFS (Breadth First Search).

    Args:
        image (List[List[int]]): 2D grid representing the image.
        sr (int): Starting pixel row.
        sc (int): Starting pixel column.
        newColor (int): New color to fill.

    Returns:
        List[List[int]]: Modified image after flood fill.
    """
    ans = deepcopy(image)
    n, m = len(image), len(image[0])
    original_color = image[sr][sc]

    if original_color == newColor:
        return ans

    queue = deque()
    queue.append((sr, sc))
    ans[sr][sc] = newColor
    directions = [(-1,0), (0,1), (1,0), (0,-1)]

    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m and ans[nr][nc] != newColor and image[nr][nc] == original_color:
                ans[nr][nc] = newColor
                queue.append((nr, nc))

    return ans

def print_image(image):
    """Helper function to print 2D image grid nicely."""
    for row in image:
        print(" ".join(map(str, row)))
    print()

if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr, sc = 1, 1
    newColor = 2

    print("Original Image:")
    print_image(image)

    print("Flood Fill using DFS:")
    result_dfs = flood_fill_dfs(image, sr, sc, newColor)
    print_image(result_dfs)

    print("Flood Fill using BFS:")
    result_bfs = flood_fill_bfs(image, sr, sc, newColor)
    print_image(result_bfs)

# ================== C++ Code ==================

cpp_code_dfs:
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
private:
    void dfs(int row, int col, vector<vector<int>>& ans,
             vector<vector<int>>& image, int newColor,
             int delRow[], int delCol[], int originalColor) {
        ans[row][col] = newColor;
        int n = image.size();
        int m = image[0].size();
        for(int i = 0; i < 4; i++) {
            int nrow = row + delRow[i];
            int ncol = col + delCol[i];
            if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
               image[nrow][ncol] == originalColor && ans[nrow][ncol] != newColor) {
                dfs(nrow, ncol, ans, image, newColor, delRow, delCol, originalColor);
            }
        }
    }
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int originalColor = image[sr][sc];
        if(originalColor == newColor) return image;
        vector<vector<int>> ans = image;
        int delRow[] = {-1, 0, 1, 0};
        int delCol[] = {0, 1, 0, -1};
        dfs(sr, sc, ans, image, newColor, delRow, delCol, originalColor);
        return ans;
    }
};

int main() {
    vector<vector<int>> image = {
        {1,1,1},
        {1,1,0},
        {1,0,1}
    };
    Solution sol;
    vector<vector<int>> ans = sol.floodFill(image, 1, 1, 2);
    for(auto row : ans) {
        for(auto pixel : row)
            cout << pixel << " ";
        cout << endl;
    }
    return 0;
}
"""

cpp_code_bfs:
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int n = image.size();
        int m = image[0].size();
        int originalColor = image[sr][sc];
        if(originalColor == newColor) return image;

        vector<vector<int>> ans = image;
        queue<pair<int,int>> q;
        q.push({sr, sc});
        ans[sr][sc] = newColor;

        int delRow[] = {-1, 0, 1, 0};
        int delCol[] = {0, 1, 0, -1};

        while(!q.empty()) {
            int row = q.front().first;
            int col = q.front().second;
            q.pop();

            for(int i = 0; i < 4; i++) {
                int nrow = row + delRow[i];
                int ncol = col + delCol[i];
                if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
                   ans[nrow][ncol] != newColor && image[nrow][ncol] == originalColor) {
                    ans[nrow][ncol] = newColor;
                    q.push({nrow, ncol});
                }
            }
        }
        return ans;
    }
};

int main() {
    vector<vector<int>> image = {
        {1,1,1},
        {1,1,0},
        {1,0,1}
    };
    Solution sol;
    vector<vector<int>> ans = sol.floodFill(image, 1, 1, 2);
    for(auto row : ans) {
        for(auto pixel : row)
            cout << pixel << " ";
        cout << endl;
    }
    return 0;
}
"""

# ================== Java Code ==================

java_code_dfs :
"""
import java.util.*;

class Solution {
    private void dfs(int row, int col, int[][] ans, int[][] image,
                     int newColor, int[] delRow, int[] delCol, int originalColor) {
        ans[row][col] = newColor;
        int n = image.length;
        int m = image[0].length;

        for(int i = 0; i < 4; i++) {
            int nrow = row + delRow[i];
            int ncol = col + delCol[i];
            if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
               image[nrow][ncol] == originalColor && ans[nrow][ncol] != newColor) {
                dfs(nrow, ncol, ans, image, newColor, delRow, delCol, originalColor);
            }
        }
    }

    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originalColor = image[sr][sc];
        if(originalColor == newColor) return image;
        int n = image.length;
        int m = image[0].length;
        int[][] ans = new int[n][m];
        for(int i = 0; i < n; i++)
            ans[i] = Arrays.copyOf(image[i], m);

        int[] delRow = {-1, 0, 1, 0};
        int[] delCol = {0, 1, 0, -1};
        dfs(sr, sc, ans, image, newColor, delRow, delCol, originalColor);
        return ans;
    }

    public static void main(String[] args) {
        int[][] image = {
            {1,1,1},
            {1,1,0},
            {1,0,1}
        };
        Solution sol = new Solution();
        int[][] ans = sol.floodFill(image, 1, 1, 2);
        for(int[] row : ans) {
            for(int pixel : row) {
                System.out.print(pixel + " ");
            }
            System.out.println();
        }
    }
}
"""

java_code_bfs:
"""
import java.util.*;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int originalColor = image[sr][sc];
        if(originalColor == newColor) return image;
        int n = image.length;
        int m = image[0].length;
        int[][] ans = new int[n][m];
        for(int i = 0; i < n; i++)
            ans[i] = Arrays.copyOf(image[i], m);

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sr, sc});
        ans[sr][sc] = newColor;

        int[] delRow = {-1, 0, 1, 0};
        int[] delCol = {0, 1, 0, -1};

        while(!queue.isEmpty()) {
            int[] curr = queue.poll();
            int row = curr[0], col = curr[1];
            for(int i = 0; i < 4; i++) {
                int nrow = row + delRow[i];
                int ncol = col + delCol[i];
                if(nrow >= 0 && nrow < n && ncol >= 0 && ncol < m &&
                   ans[nrow][ncol] != newColor && image[nrow][ncol] == originalColor) {
                    ans[nrow][ncol] = newColor;
                    queue.offer(new int[]{nrow, ncol});
                }
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        int[][] image = {
            {1,1,1},
            {1,1,0},
            {1,0,1}
        };
        Solution sol = new Solution();
        int[][] ans = sol.floodFill(image, 1, 1, 2);
        for(int[] row : ans) {
            for(int pixel : row) {
                System.out.print(pixel + " ");
            }
            System.out.println();
        }
    }
}
"""
