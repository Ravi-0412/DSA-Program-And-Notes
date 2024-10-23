# Logic: 
"""
You can move(change) any of four wheels in two direction either clockwise or anti-clockwise.

It's like multisource bfs like one level you can reach to these states and using next you can
reach to some other states and so on.
"""

# Time: 10**4 * 8
# Because for each 4 wheel , we will have 10 choices (0 to 9) and for for each 10**4 state there 
# will be 8 neighbours. (4 wheels can rotate either in clockwise or anticlockwise s0 4*2 = 8).

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Helper function to find all possible lock combinations by changing
        # one digit up or down by 1 from the current code
        def neighbors(code):
            result = []
            # Iterate through each of the 4 digits in the lock code
            for i in range(4):
                x = int(code[i])  # Get the integer value of the current digit
                # Try moving the digit up and down (with wrap-around between 0 and 9)
                for diff in (-1, 1):
                    # Calculate new digit with wrap-around using modulo 10
                    y = (x + diff + 10) % 10
                    # Form the new lock code with the changed digit
                    result.append(code[:i] + str(y) + code[i + 1:])
            # Return the list of all neighboring lock combinations
            return result

        # Convert the list of deadends to a set for O(1) lookups
        deadSet = set(deadends)

        # If the initial lock "0000" is a deadend, we can't start, so return -1
        if "0000" in deadSet:
            return -1

        # Use a queue to perform a breadth-first search (BFS) starting from "0000"
        q = deque(["0000"])
        steps = 0  # Track the number of moves made (BFS levels)

        # BFS loop to explore all possible combinations level by level
        while q:
            # For each level in the BFS, we process all nodes (lock combinations) at this depth
            for _ in range(len(q)):
                curr = q.popleft()  # Get the current lock combination from the queue

                # If the current lock combination matches the target, return the step count
                if curr == target:
                    return steps

                # Explore all possible lock combinations by changing one digit
                for nei in neighbors(curr):
                    # If the neighbor lock is a deadend or already visited, skip it
                    if nei in deadSet:
                        continue
                    # Mark the neighbor as visited by adding it to the deadSet
                    deadSet.add(nei)
                    # Add the valid neighbor to the queue to be explored in the next step
                    q.append(nei)

            # After processing one level, increment the step count (move count)
            steps += 1

        # If we exhaust all possibilities and don't reach the target, return -1
        return -1

# Java
"""
import java.util.*;

class Solution {
    // Define the neighbors method outside of the openLock method
    private List<String> neighbors(String code) {
        List<String> result = new ArrayList<>();
        // Iterate through each of the 4 digits in the lock code
        for (int i = 0; i < 4; i++) {
            char[] chars = code.toCharArray();  // Convert string to character array
            char original = chars[i];  // Store the original digit at position i
            
            // Change the digit at position i by -1 (decrement) with wrap-around
            chars[i] = original == '0' ? '9' : (char)(original - 1);
            result.add(new String(chars));  // Add the new combination to the result

            // Change the digit at position i by +1 (increment) with wrap-around
            chars[i] = original == '9' ? '0' : (char)(original + 1);
            result.add(new String(chars));  // Add the new combination to the result
        }
        return result;  // Return all possible neighboring combinations
    }

    // The main openLock method
    public int openLock(String[] deadends, String target) {
        // Convert deadends array to a set for fast lookup and to use as the visited set
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));

        // If the initial lock "0000" is a deadend, return -1 immediately
        if (deadSet.contains("0000")) {
            return -1;
        }

        // Queue for BFS starting from "0000"
        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");

        // Mark "0000" as visited by adding it to the deadSet
        deadSet.add("0000");

        int steps = 0;  // Track the number of moves (steps)

        // BFS loop
        while (!queue.isEmpty()) {
            int size = queue.size();
            // Process all nodes (lock combinations) at the current BFS level
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();  // Get the current lock combination

                // If we reach the target lock combination, return the number of steps
                if (curr.equals(target)) {
                    return steps;
                }

                // Get all neighbors of the current lock combination
                for (String neighbor : neighbors(curr)) {
                    // If the neighbor is a deadend or has been visited, skip it
                    if (deadSet.contains(neighbor)) {
                        continue;
                    }
                    // Mark the neighbor as visited by adding it to the deadSet
                    deadSet.add(neighbor);
                    // Add the valid neighbor to the queue for future exploration
                    queue.offer(neighbor);
                }
            }
            // After processing one level, increment the step count
            steps++;
        }

        // If we exhaust all possibilities and don't find the target, return -1
        return -1;
    }
}

"""
