# Method 1: 

# Think value of matric = color
# Logic: Just you have to make value of cells = given color if that cell is directly or indirectly connected to given cell and image_value of those cells are same.
# i.e they are are forming a connected components with same value then make value of those cells = given color.
# Can do by single source bfs and dfs also.

# Time complexity: O(m*n), space complexity: O(m*n)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        src_color = image[sr][sc]
        q= deque([(sr,sc)])
        while q:
            for i in range(len(q)):
                r, c = q.popleft()  # clr= pixel at that (r,c)
                image[r][c]= color  # can update when we will see for 1st time also
                directions= [[-1,0],[1,0],[0,-1],[0,1]]  # up,down,left,right
                for dr,dc in directions:
                    row,col= r+ dr, c+ dc
                    # if in range and image_of_cur_cell = source image value and already not colored with given color(just working as visited)
                    if 0 <=row < len(image) and 0<= col < len(image[0]) and image[row][col] == src_color and image[row][col]!=color:
                        q.append((row, col))
        return image
    

# Java
"""
import java.util.*;

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int srcColor = image[sr][sc];
        if (srcColor == color) return image; // optimization to avoid infinite loop

        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{sr, sc});

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] pixel = q.poll();  // clr= pixel at that (r,c)
                int r = pixel[0], c = pixel[1];
                image[r][c] = color;  // can update when we will see for 1st time also

                // directions: up, down, left, right
                int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
                for (int[] dir : directions) {
                    int row = r + dir[0];
                    int col = c + dir[1];

                    // if in range and image_of_cur_cell == source image value and not already colored (working as visited)
                    if (row >= 0 && row < image.length &&
                        col >= 0 && col < image[0].length &&
                        image[row][col] == srcColor && image[row][col] != color) {
                        q.offer(new int[]{row, col});
                    }
                }
            }
        }
        return image;
    }
}
"""


# C++
"""
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int srcColor = image[sr][sc];
        if (srcColor == color) return image; // optimization to avoid infinite loop

        queue<pair<int, int>> q;
        q.push({sr, sc});

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                auto [r, c] = q.front(); q.pop();  // clr= pixel at that (r,c)
                image[r][c] = color;  // can update when we will see for 1st time also

                // directions: up, down, left, right
                vector<pair<int, int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};
                for (auto [dr, dc] : directions) {
                    int row = r + dr;
                    int col = c + dc;

                    // if in range and image_of_cur_cell == source image value and not already colored (working as visited)
                    if (row >= 0 && row < image.size() &&
                        col >= 0 && col < image[0].size() &&
                        image[row][col] == srcColor && image[row][col] != color) {
                        q.push({row, col});
                    }
                }
            }
        }
        return image;
    }
};
"""


# Method 2:
# we can directly modify the image matrix and use it as a visited tracker by only checking color changes.
"""
Time Complexity: O(m * n)
You may potentially visit every pixel in the worst case (all pixels are the same color).

Space Complexity:
Best case (non-recursive area): O(1)
Worst case (fully connected area): O(m * n) stack space due to recursion
"""

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # If starting pixel already has the new color, avoid infinite recursion
        if image[sr][sc] == newColor:
            return image

        def fill(r, c, color):
            # Base case: check bounds and original color match
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color:
                return

            # Change the pixel color
            image[r][c] = newColor

            # Recursive calls in 4 directions
            fill(r + 1, c, color)  # down
            fill(r - 1, c, color)  # up
            fill(r, c + 1, color)  # right
            fill(r, c - 1, color)  # left

        original_color = image[sr][sc]
        fill(sr, sc, original_color)
        return image


# Java
"""
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        // If the starting pixel is already the new color, nothing to do
        if (image[sr][sc] == newColor) return image;

        // Start recursive DFS fill
        fill(image, sr, sc, image[sr][sc], newColor);
        return image;
    }

    // Recursive function to flood-fill
    private void fill(int[][] image, int sr, int sc, int color, int newColor) {
        // Base case: out of bounds or color mismatch
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != color)
            return;

        // Change current pixel's color
        image[sr][sc] = newColor;

        // Recurse in all 4 directions
        fill(image, sr + 1, sc, color, newColor);  // down
        fill(image, sr - 1, sc, color, newColor);  // up
        fill(image, sr, sc + 1, color, newColor);  // right
        fill(image, sr, sc - 1, color, newColor);  // left
    }
}
"""

# C++
"""
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;

        fill(image, sr, sc, image[sr][sc], newColor);
        return image;
    }

private:
    void fill(vector<vector<int>>& image, int sr, int sc, int color, int newColor) {
        // Base case: out of bounds or color mismatch
        if (sr < 0 || sr >= image.size() || sc < 0 || sc >= image[0].size() || image[sr][sc] != color)
            return;

        // Change current pixel's color
        image[sr][sc] = newColor;

        // Recurse in all 4 directions
        fill(image, sr + 1, sc, color, newColor); // down
        fill(image, sr - 1, sc, color, newColor); // up
        fill(image, sr, sc + 1, color, newColor); // right
        fill(image, sr, sc - 1, color, newColor); // left
    }
};
"""