# Method 1: 
# Similar code as 'Spiral 1 and spiral 2'

# Logic : 
"""
Take steps one by one.
If the location is inside of grid, add it to res.
But how to simulate the path?

Observation: 

move right 1 step, turn right
move down 1 step, turn right
move left 2 steps, turn right
move top 2 steps, turn right,
move right 3 steps, turn right
move down 3 steps, turn right
move left 4 steps, turn right
move top 4 steps, turn right,

we can find the sequence of steps: 1,1,2,2,3,3,4,4,5,5....

Note: We will start with steps = 1 and we will increase the step when we will start going west or
When we will complete a spiral i.e after going all directions.
"""
# Time O(max(R,C)^2)
# Space O(R*C) for output


class Solution(object):
    
    def spiralMatrixIII(self, R, C, r0, c0):
        # Initialize result list with the starting position
        res = [(r0, c0)] 
        
        # Function to check if a cell is within bounds
        def is_valid(row, col):
            return 0 <= row < R and 0 <= col < C 
        
        # Set initial values for steps and position
        steps = 1 
        r, c = r0, c0 
        
        # Continue until all cells are visited
        while len(res) < R * C: 
            # Go east
            for _ in range(steps):
                c += 1 
                if is_valid(r, c): 
                    res.append((r, c))
                    
            # Go south
            for _ in range(steps):
                r += 1
                if is_valid(r, c): 
                    res.append((r, c))
                    
            steps += 1   # increase step since we are going west
                    
            # Go west
            for _ in range(steps):
                c -= 1
                if is_valid(r, c): 
                    res.append((r, c))           
            
            # Go north
            for _ in range(steps):
                r -= 1
                if is_valid(r, c): 
                    res.append((r, c))           
                    
            steps += 1    # increase step after each spiral
            
        return res

# Method 2: 
# Concise one of method 1
# Time O(max(R,C)^2)
# Space O(R*C) for output
class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        directions =  [[0, 1], [1, 0], [0, -1], [-1, 0]] # east, south, west, north
        res= [] 
        length, d = 0, 0 # move <length> steps in the <d> direction
        res.append([rStart, cStart])
        while len(res) < rows*cols:
            if d == 0 or d == 2:
                length += 1 # when move east or west, the length of path need plus 1 (this makes the outer circle each time)
            for i in range(length):
                rStart += directions[d][0]
                cStart += directions[d][1]
                if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols: # check valid
                    res.append([rStart, cStart])
            d = (d + 1) % 4 # turn to next direction
        return res
        
# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    public List<List<Integer>> spiralMatrixIII(int R, int C, int r0, int c0) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(Arrays.asList(r0, c0));

        // Function to check if a cell is within bounds
        boolean isValid(int row, int col) {
            return row >= 0 && row < R && col >= 0 && col < C;
        }

        int steps = 1;
        int r = r0, c = c0;

        while (res.size() < R * C) {
            // Go east
            for (int i = 0; i < steps; i++) {
                c++;
                if (isValid(r, c)) res.add(Arrays.asList(r, c));
            }

            // Go south
            for (int i = 0; i < steps; i++) {
                r++;
                if (isValid(r, c)) res.add(Arrays.asList(r, c));
            }

            steps++;  // Increase step since we are going west

            // Go west
            for (int i = 0; i < steps; i++) {
                c--;
                if (isValid(r, c)) res.add(Arrays.asList(r, c));
            }

            // Go north
            for (int i = 0; i < steps; i++) {
                r--;
                if (isValid(r, c)) res.add(Arrays.asList(r, c));
            }

            steps++;  // Increase step after each spiral
        }

        return res;
    }
}
//Method 2
import java.util.*;

class Solution {
    public List<List<Integer>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        List<List<Integer>> res = new ArrayList<>();
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // east, south, west, north
        int length = 0, d = 0;  // Move <length> steps in the <d> direction

        res.add(Arrays.asList(rStart, cStart));

        while (res.size() < rows * cols) {
            if (d == 0 || d == 2) {
                length++;  // Increase length when moving east or west (expanding outward)
            }

            for (int i = 0; i < length; i++) {
                rStart += directions[d][0];
                cStart += directions[d][1];
                if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) { // Check validity
                    res.add(Arrays.asList(rStart, cStart));
                }
            }

            d = (d + 1) % 4;  // Turn to the next direction
        }

        return res;
    }
}
"""
# C++ Code 
"""
//Method 1
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r0, int c0) {
        // Initialize result list with the starting position
        vector<vector<int>> res = {{r0, c0}};

        // Function to check if a cell is within bounds
        auto is_valid = [&](int row, int col) {
            return row >= 0 && row < R && col >= 0 && col < C;
        };

        // Set initial values for steps and position
        int steps = 1;
        int r = r0, c = c0;

        // Continue until all cells are visited
        while (res.size() < R * C) {
            // Go east
            for (int i = 0; i < steps; i++) {
                c++;
                if (is_valid(r, c)) res.push_back({r, c});
            }

            // Go south
            for (int i = 0; i < steps; i++) {
                r++;
                if (is_valid(r, c)) res.push_back({r, c});
            }

            steps++;  // Increase step since we are going west

            // Go west
            for (int i = 0; i < steps; i++) {
                c--;
                if (is_valid(r, c)) res.push_back({r, c});
            }

            // Go north
            for (int i = 0; i < steps; i++) {
                r--;
                if (is_valid(r, c)) res.push_back({r, c});
            }

            steps++;  // Increase step after each spiral
        }

        return res;
    }
};
//Method 2
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int rows, int cols, int rStart, int cStart) {
        vector<vector<int>> res;
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // east, south, west, north
        int length = 0, d = 0;  // Move <length> steps in the <d> direction

        res.push_back({rStart, cStart});

        while (res.size() < rows * cols) {
            if (d == 0 || d == 2) {
                length++;  // Increase length when moving east or west (expanding outward)
            }

            for (int i = 0; i < length; i++) {
                rStart += directions[d][0];
                cStart += directions[d][1];
                if (rStart >= 0 && rStart < rows && cStart >= 0 && cStart < cols) { // Check validity
                    res.push_back({rStart, cStart});
                }
            }

            d = (d + 1) % 4;  // Turn to the next direction
        }

        return res;
    }
};
"""