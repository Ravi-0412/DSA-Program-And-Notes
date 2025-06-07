"""
Logic: 
You have 4 wheels, each can move forward or backward (clockwise or anticlockwise).From one lock state, you can reach 8 new states (4 wheels × 2 directions).
We use BFS to explore these states level by level until we reach the target.

There are 10,000 possible states (0000 to 9999), so BFS is efficient here. This is like a multi-source BFS where each state leads to neighbors.

Time complexity

Time: 10**4 * 8
Because for each 4 wheel , we will have 10 choices (0 to 9) and for for each 10**4 state there 
will be 8 neighbours. (4 wheels can rotate either in clockwise or anticlockwise s0 4*2 = 8).

"""



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
    private List<String> neighbors(String code) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            char[] chars = code.toCharArray();
            char original = chars[i];
            
            chars[i] = original == '0' ? '9' : (char)(original - 1);
            result.add(new String(chars));

            chars[i] = original == '9' ? '0' : (char)(original + 1);
            result.add(new String(chars));
        }
        return result;
    }

    public int openLock(String[] deadends, String target) {
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));
        if (deadSet.contains("0000")) return -1;

        Queue<String> queue = new LinkedList<>();
        queue.offer("0000");
        deadSet.add("0000");
        int steps = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String curr = queue.poll();
                if (curr.equals(target)) return steps;

                for (String neighbor : neighbors(curr)) {
                    if (deadSet.contains(neighbor)) continue;
                    deadSet.add(neighbor);
                    queue.offer(neighbor);
                }
            }
            steps++;
        }
        return -1;
    }
}

"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
private:
    vector<string> neighbors(const string& code) {
        vector<string> result;
        for (int i = 0; i < 4; i++) {
            string s = code;
            s[i] = (s[i] == '0') ? '9' : s[i] - 1;
            result.push_back(s);

            s[i] = (code[i] == '9') ? '0' : code[i] + 1;
            result.push_back(s);
        }
        return result;
    }

public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> deadSet(deadends.begin(), deadends.end());
        if (deadSet.count("0000")) return -1;

        queue<string> q;
        q.push("0000");
        deadSet.insert("0000");
        int steps = 0;

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                if (curr == target) return steps;

                for (const string& neighbor : neighbors(curr)) {
                    if (deadSet.count(neighbor)) continue;
                    deadSet.insert(neighbor);
                    q.push(neighbor);
                }
            }
            steps++;
        }
        return -1;
    }
};


"""
