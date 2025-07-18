# Method 1: 

# Simplifying rules
"""
i) Each digit in the pattern must be adjacent to the previous digit, either vertically, horizontally, or diagonally.
ii) Some digit pairs cannot be used unless the digit in between them has already been used.
"""

# Logic: 
"""
We can count answer starting from each number.
But (1, 3, 7, 9) : symmetric , (2, 4, 6, 8) : symmetric
Means finding answer for any of these number (1, 3, 7, 9)  will be same.
So just find for one and then multiply by '4' to get answer of whole set (1, 3, 7, 9).
Here we will call function for num = 1

And same for set (2, 4, 6, 8)

And then we need to call separately for pattern starting with 5.

Note: We need to take care of pair that we can't visit directly unless we visit the number between them.
e.g: You can't go to '7' from '1' without visiting '4'.
For this we will maintain a dictionary/10*10 2- d array that will tell we must need to visit
the number in between this pair to visit the given pair.

 For example, (1,7): 4 means that you cannot use the digits 1 and 7 in the pattern unless 4 has already been visited.

 dfs(visited, last): 
 visited: A set of visited digits.
last: The last digit used in the current pattern.

How dfs(visited, last ) will be implemented?
i) For each digit from 1 to 9, check if the digit is not in the visited set.
ii) For the digit pair (last, i), ensure that it either does not need any intermediate digit 
(i.e., (last, i) is not in skip) or if it does, the intermediate digit must be in visited.
iii) Recursively call dfs with the new visited set (including the new digit) and the new last digit.

"""
# Time: O(9^9 * 3)  , 3 time we are callig and after each number we have 9 choices and 9 number are there.
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {}
        skip[(1,7)] = 4
        skip[(1,3)] = 2
        skip[(1,9)] = 5
        skip[(2,8)] = 5
        skip[(3,7)] = 5
        skip[(3,9)] = 6
        skip[(4,6)] = 5
        skip[(7,9)] = 8
        self.ans = 0

        def dfs(visited, last):
            if len(visited) >= m:
                self.ans += 1
            if len(visited) == n:
                return
            for i in range(1, 10):
                if i not in visited:
                  # if i not in visited
                    pair = (min(last, i), max(last, i))
                    if pair not in skip or skip[pair] in visited: 
                      # For the digit pair (last, i), ensure that it either does not need any intermediate digit 
                      # (i.e., (last, i) is not in skip) or if it does, the intermediate digit must be in visited.
                        dfs(visited | set([i]), i)

        dfs({1}, 1)
        dfs({2}, 2)
        self.ans *= 4
        dfs({5}, 5)
        return self.ans

# Java Code 
"""
import java.util.*;

public class Solution {
    private int ans = 0;
    private final Map<String, Integer> skip = new HashMap<>();

    public int numberOfPatterns(int m, int n) {
        // Mapping the required intermediate digit between pairs
        skip.put("1,3", 2);
        skip.put("1,7", 4);
        skip.put("1,9", 5);
        skip.put("2,8", 5);
        skip.put("3,7", 5);
        skip.put("3,9", 6);
        skip.put("4,6", 5);
        skip.put("7,9", 8);

        dfs(new HashSet<>(List.of(1)), 1, m, n);
        dfs(new HashSet<>(List.of(2)), 2, m, n);
        ans *= 4;
        dfs(new HashSet<>(List.of(5)), 5, m, n);
        return ans;
    }

    private void dfs(Set<Integer> visited, int last, int m, int n) {
        if (visited.size() >= m) {
            ans++;
        }
        if (visited.size() == n) return;

        for (int i = 1; i <= 9; i++) {
            if (!visited.contains(i)) {
                String pair = Math.min(i, last) + "," + Math.max(i, last);
                if (!skip.containsKey(pair) || visited.contains(skip.get(pair))) {
                    Set<Integer> newSet = new HashSet<>(visited);
                    newSet.add(i);
                    dfs(newSet, i, m, n);
                }
            }
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <string>
using namespace std;

class Solution {
    int ans = 0;
    unordered_map<string, int> skip;

public:
    int numberOfPatterns(int m, int n) {
        // Mapping the required intermediate digit between pairs
        skip["1,3"] = 2;
        skip["1,7"] = 4;
        skip["1,9"] = 5;
        skip["2,8"] = 5;
        skip["3,7"] = 5;
        skip["3,9"] = 6;
        skip["4,6"] = 5;
        skip["7,9"] = 8;

        dfs({1}, 1, m, n);
        dfs({2}, 2, m, n);
        ans *= 4;
        dfs({5}, 5, m, n);
        return ans;
    }

private:
    void dfs(unordered_set<int> visited, int last, int m, int n) {
        if (visited.size() >= m) {
            ans++;
        }
        if (visited.size() == n) return;

        for (int i = 1; i <= 9; ++i) {
            if (!visited.count(i)) {
                string key = to_string(min(i, last)) + "," + to_string(max(i, last));
                if (!skip.count(key) || visited.count(skip[key])) {
                    unordered_set<int> newVisited = visited;
                    newVisited.insert(i);
                    dfs(newVisited, i, m, n);
                }
            }
        }
    }
};
"""