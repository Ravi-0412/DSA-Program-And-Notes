# Method 1: 

"""
Treat sequenc eif number in grid as starting(source) node. Then our question reduces to find the minimum moves
to reach from source to destination where destination = "123450".

For this we can use bfs. 
Why not Dijkastra?
Because cost is not associated with moves.
"""

from collections import deque
from typing import List

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Define the target state and the initial state
        target = "123450"
        start = ''.join(str(num) for row in board for num in row)
        
        # Neighbor mapping for each index in the 1D representation of the board
        neighbors = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        # Set up BFS
        queue = deque([(start, 0)])  # Each element is a tuple: (state, number of moves)
        visited = set()
        visited.add(start)
        
        while queue:
            state, moves = queue.popleft()
            
            # Check if the target state is reached
            if state == target:
                return moves
            
            # Find the index of the empty tile ('0')
            zero_index = state.index('0')
            
            # Generate new states by swapping '0' with its neighbors
            for neighbor in neighbors[zero_index]:
                # Convert state to a list to allow mutation
                new_state = list(state)
                # Swap '0' with its neighbor
                new_state[zero_index], new_state[neighbor] = new_state[neighbor], new_state[zero_index]
                # Convert the list back to a string
                new_state_str = ''.join(new_state)
                
                # If this new state hasn't been visited yet, add it to the queue
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))
        
        # If the target state is not reachable
        return -1


# Java
"""
import java.util.*;

class Solution {
    public int slidingPuzzle(int[][] board) {
        // Define the target state and the initial state
        String target = "123450";
        StringBuilder sb = new StringBuilder();
        for (int[] row : board) {
            for (int num : row) {
                sb.append(num);
            }
        }
        String start = sb.toString();

        // Neighbor mapping for each index in the 1D representation of the board
        int[][] neighbors = {
            {1, 3},        // index 0
            {0, 2, 4},     // index 1
            {1, 5},        // index 2
            {0, 4},        // index 3
            {1, 3, 5},     // index 4
            {2, 4}         // index 5
        };

        // Set up BFS
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        queue.offer(start);
        visited.add(start);
        int moves = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            // Process all nodes at the current level
            for (int i = 0; i < size; i++) {
                String state = queue.poll();

                // Check if the target state is reached
                if (state.equals(target)) return moves;

                // Find the index of the empty tile ('0')
                int zeroIndex = state.indexOf('0');

                // Generate new states by swapping '0' with its neighbors
                for (int neighbor : neighbors[zeroIndex]) {
                    char[] chars = state.toCharArray();
                    // Swap '0' with its neighbor
                    char temp = chars[zeroIndex];
                    chars[zeroIndex] = chars[neighbor];
                    chars[neighbor] = temp;
                    String newState = new String(chars);

                    // If this new state hasn't been visited yet, add it to the queue
                    if (!visited.contains(newState)) {
                        visited.add(newState);
                        queue.offer(newState);
                    }
                }
            }
            moves++;
        }

        // If the target state is not reachable
        return -1;
    }
}


"""


# C++
"""
#include <vector>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int slidingPuzzle(vector<vector<int>>& board) {
        // Define the target state and the initial state
        string target = "123450";
        string start;
        for (const auto& row : board) {
            for (int num : row) {
                start += to_string(num);
            }
        }

        // Neighbor mapping for each index in the 1D representation of the board
        vector<vector<int>> neighbors = {
            {1, 3},        // index 0
            {0, 2, 4},     // index 1
            {1, 5},        // index 2
            {0, 4},        // index 3
            {1, 3, 5},     // index 4
            {2, 4}         // index 5
        };

        // Set up BFS
        queue<string> q;
        unordered_set<string> visited;
        q.push(start);
        visited.insert(start);
        int moves = 0;

        while (!q.empty()) {
            int size = q.size();
            // Process all nodes at the current level
            for (int i = 0; i < size; ++i) {
                string state = q.front();
                q.pop();

                // Check if the target state is reached
                if (state == target) return moves;

                // Find the index of the empty tile ('0')
                int zeroIndex = state.find('0');

                // Generate new states by swapping '0' with its neighbors
                for (int neighbor : neighbors[zeroIndex]) {
                    string newState = state;
                    // Swap '0' with its neighbor
                    swap(newState[zeroIndex], newState[neighbor]);

                    // If this new state hasn't been visited yet, add it to the queue
                    if (!visited.count(newState)) {
                        visited.insert(newState);
                        q.push(newState);
                    }
                }
            }
            moves++;
        }

        // If the target state is not reachable
        return -1;
    }
};


"""


