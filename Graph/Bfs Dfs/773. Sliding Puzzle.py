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

public class Solution {
    public int slidingPuzzle(int[][] board) {
        // Define the target and initial state
        String target = "123450";
        StringBuilder startBuilder = new StringBuilder();
        for (int[] row : board) {
            for (int num : row) {
                startBuilder.append(num);
            }
        }
        String start = startBuilder.toString();

        // Neighbor indices for each position in the 1D board representation
        int[][] neighbors = {
            {1, 3},       // 0
            {0, 2, 4},    // 1
            {1, 5},       // 2
            {0, 4},       // 3
            {1, 3, 5},    // 4
            {2, 4}        // 5
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
                if (state.equals(target)) {
                    return moves;
                }

                // Find the index of '0'
                int zeroIndex = state.indexOf('0');

                // Try swapping '0' with all of its neighbors
                for (int neighbor : neighbors[zeroIndex]) {
                    char[] newStateChars = state.toCharArray();
                    // Swap characters
                    char temp = newStateChars[zeroIndex];
                    newStateChars[zeroIndex] = newStateChars[neighbor];
                    newStateChars[neighbor] = temp;

                    String newState = new String(newStateChars);

                    // Add the new state to the queue if it hasn't been visited
                    if (!visited.contains(newState)) {
                        visited.add(newState);
                        queue.offer(newState);
                    }
                }
            }
            moves++;
        }

        // If the target state is unreachable
        return -1;
    }
}
"""
