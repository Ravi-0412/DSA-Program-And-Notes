# Basic: 

# logic: from cur stone move to next stone we can reach by taking the possible jump.

# note: we can reach the same stone by taking the same number of jump many times.
# That's why it will give TLE by Recursion.

"""
The goal is to determine whether the frog can reach the last stone.
Use map/set to represent a mapping from the stone.
Notice that no need to calculate the last stone.
On each step, we look if any other stone can be reached from it, 
if so, we update that stone's steps by adding step, step + 1, step - 1. 
If we can reach the final stone, we return true
"""


# method 1: 
# Recursive

class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)

        # will tell the cur stone where we are, and last jump we took.
        def solve(stone, jump):
            if stone== self.target:
                return True
            for j in (jump-1, jump, jump +1):
                # we can only go forward and the stone to whcih we will go must be in our stoneSet.
                if j >0 and (stone + j) in stoneSet:  
                    if solve(stone + j, j):
                        return True
            return False

        return solve(0, 0)

# Java Code 
"""
import java.util.*;

public class Solution {
    private int target;
    private Set<Integer> stoneSet;

    public boolean canCross(int[] stones) {
        target = stones[stones.length - 1];
        stoneSet = new HashSet<>();
        for (int stone : stones)
            stoneSet.add(stone);

        return solve(0, 0);
    }

    private boolean solve(int stone, int jump) {
        if (stone == target)
            return true;

        // will tell the cur stone where we are, and last jump we took.
        for (int j = jump - 1; j <= jump + 1; j++) {
            // we can only go forward and the stone to which we will go must be in our stoneSet.
            if (j > 0 && stoneSet.contains(stone + j)) {
                if (solve(stone + j, j))
                    return true;
            }
        }
        return false;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_set>

class Solution {
    int target;
    std::unordered_set<int> stoneSet;

public:
    bool canCross(std::vector<int>& stones) {
        target = stones.back();
        for (int stone : stones)
            stoneSet.insert(stone);

        return solve(0, 0);
    }

private:
    bool solve(int stone, int jump) {
        if (stone == target)
            return true;

        // will tell the cur stone where we are, and last jump we took.
        for (int j = jump - 1; j <= jump + 1; ++j) {
            // we can only go forward and the stone to which we will go must be in our stoneSet.
            if (j > 0 && stoneSet.count(stone + j)) {
                if (solve(stone + j, j))
                    return true;
            }
        }
        return false;
    }
};
"""

# method 2: 
# memoising 
# logic: store the (stone, jump) in set so that we can skip when we will reach that stone with same jump again.

class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)
        stoneToLastJump= set()

        # will tell the cur stone where we are, and last jump we took.
        def solve(stone, jump):
            if stone== self.target:
                return True
            # simply skip 
            if (stone, jump) in stoneToLastJump:
                return 
            for j in (jump-1, jump, jump +1): 
                # first move should be of '1' will be automatically handled by 'j > 0'.
                if j >0 and (stone + j) in stoneSet:
                    if solve(stone + j, j):
                        return True
            stoneToLastJump.add((stone, jump))
            return False

        return solve(0, 0)

# Java Code 
"""
import java.util.*;

public class Solution {
    private int target;
    private Set<Integer> stoneSet;
    private Set<String> stoneToLastJump;

    public boolean canCross(int[] stones) {
        target = stones[stones.length - 1];
        stoneSet = new HashSet<>();
        for (int stone : stones)
            stoneSet.add(stone);
        stoneToLastJump = new HashSet<>();

        // will tell the cur stone where we are, and last jump we took.
        return solve(0, 0);
    }

    private boolean solve(int stone, int jump) {
        if (stone == target)
            return true;
        // simply skip 
        String key = stone + "," + jump;
        if (stoneToLastJump.contains(key))
            return false;

        for (int j = jump - 1; j <= jump + 1; j++) {
            // first move should be of '1' will be automatically handled by 'j > 0'.
            if (j > 0 && stoneSet.contains(stone + j)) {
                if (solve(stone + j, j))
                    return true;
            }
        }

        stoneToLastJump.add(key);
        return false;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_set>
#include <string>

class Solution {
    int target;
    std::unordered_set<int> stoneSet;
    std::unordered_set<std::string> stoneToLastJump;

public:
    bool canCross(std::vector<int>& stones) {
        target = stones.back();
        for (int stone : stones)
            stoneSet.insert(stone);

        // will tell the cur stone where we are, and last jump we took.
        return solve(0, 0);
    }

private:
    bool solve(int stone, int jump) {
        if (stone == target)
            return true;
        // simply skip 
        std::string key = std::to_string(stone) + "," + std::to_string(jump);
        if (stoneToLastJump.count(key))
            return false;

        for (int j = jump - 1; j <= jump + 1; ++j) {
            // first move should be of '1' will be automatically handled by 'j > 0'.
            if (j > 0 && stoneSet.count(stone + j)) {
                if (solve(stone + j, j))
                    return true;
            }
        }

        stoneToLastJump.insert(key);
        return false;
    }
};
"""
# Method 3: 
#Tabulation
#time: O(n^2), space : O(n^2)
class Solution(object):
    def canCross(self, stones):
        self.target = stones[-1]
        stoneSet = set(stones)

        # key = current stone, value = set of all jump sizes we can use to reach that stone
        dp = {stone: set() for stone in stones}
        dp[0].add(0)  # start at stone 0 with jump 0

        for stone in stones:
            for jump in dp[stone]:
                for j in (jump - 1, jump, jump + 1):
                    if j > 0 and (stone + j) in stoneSet:
                        dp[stone + j].add(j)
                        if (stone + j) == self.target:
                            return True  # early exit if target is reached

        return False
   

# Java Code 
"""
import java.util.*;

public class Solution {
    private int target;
    private Set<Integer> stoneSet;
    private Map<Integer, Set<Integer>> dp;

    public boolean canCross(int[] stones) {
        target = stones[stones.length - 1];
        stoneSet = new HashSet<>();
        for (int stone : stones)
            stoneSet.add(stone);

        // key = current stone, value = set of all jump sizes we can use to reach that stone
        dp = new HashMap<>();
        for (int stone : stones)
            dp.put(stone, new HashSet<>());
        dp.get(0).add(0);  // start at stone 0 with jump 0

        for (int stone : stones) {
            for (int jump : dp.get(stone)) {
                for (int j = jump - 1; j <= jump + 1; j++) {
                    if (j > 0 && stoneSet.contains(stone + j)) {
                        dp.get(stone + j).add(j);
                        if (stone + j == target)
                            return true;  // early exit if target is reached
                    }
                }
            }
        }

        return false;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_set>
#include <unordered_map>

class Solution {
public:
    bool canCross(std::vector<int>& stones) {
        int target = stones.back();
        std::unordered_set<int> stoneSet(stones.begin(), stones.end());

        // key = current stone, value = set of all jump sizes we can use to reach that stone
        std::unordered_map<int, std::unordered_set<int>> dp;
        for (int stone : stones)
            dp[stone] = {};
        dp[0].insert(0);  // start at stone 0 with jump 0

        for (int stone : stones) {
            for (int jump : dp[stone]) {
                for (int j = jump - 1; j <= jump + 1; ++j) {
                    if (j > 0 && stoneSet.count(stone + j)) {
                        dp[stone + j].insert(j);
                        if (stone + j == target)
                            return true;  // early exit if target is reached
                    }
                }
            }
        }

        return false;
    }
};
"""

# method 4: 
# itertaive
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # first jump must be of one unit only.
        if stones[1] - stones[0] > 1:
            return False
        stonesSet= set(stones)
        visited= set()  # to avoid repition when we will reach anh stone with same jump.
        stack= [(0, 0)]  # [(stone, lastJump)]
        visited.add((0, 0)) 
        while stack:
            stone, jump= stack.pop()
            # visited.add((stone, jump))
            # possible jumps we can take from this stone
            for j in (jump -1, jump, jump + 1):
                # stone(s) to which we will reach after taking the jump 'j'
                s= stone + j
                # can only go forward and s must be in set and (s, j) must not be in visited
                if j > 0 and s in stonesSet and (s, j) not in visited:
                    if s== stones[-1]:
                        return True
                    stack.append((s, j))
                    visited.add((s, j))
        return False


# Java Code 
"""
import java.util.*;

public class Solution {
    public boolean canCross(int[] stones) {
        // first jump must be of one unit only.
        if (stones[1] - stones[0] > 1)
            return false;

        Set<Integer> stonesSet = new HashSet<>();
        for (int stone : stones)
            stonesSet.add(stone);

        Set<String> visited = new HashSet<>();  // to avoid repition when we will reach any stone with same jump.
        Deque<int[]> stack = new ArrayDeque<>();  // [(stone, lastJump)]
        stack.push(new int[]{0, 0});
        visited.add("0,0");

        while (!stack.isEmpty()) {
            int[] current = stack.pop();
            int stone = current[0], jump = current[1];

            // possible jumps we can take from this stone
            for (int j = jump - 1; j <= jump + 1; j++) {
                // stone(s) to which we will reach after taking the jump 'j'
                int s = stone + j;
                // can only go forward and s must be in set and (s, j) must not be in visited
                String key = s + "," + j;
                if (j > 0 && stonesSet.contains(s) && !visited.contains(key)) {
                    if (s == stones[stones.length - 1])
                        return true;
                    stack.push(new int[]{s, j});
                    visited.add(key);
                }
            }
        }

        return false;
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <unordered_set>
#include <stack>
#include <string>

class Solution {
public:
    bool canCross(std::vector<int>& stones) {
        // first jump must be of one unit only.
        if (stones[1] - stones[0] > 1)
            return false;

        std::unordered_set<int> stonesSet(stones.begin(), stones.end());
        std::unordered_set<std::string> visited;  // to avoid repition when we will reach any stone with same jump.
        std::stack<std::pair<int, int>> stack;  // [(stone, lastJump)]
        stack.push({0, 0});
        visited.insert("0,0");

        while (!stack.empty()) {
            auto [stone, jump] = stack.top();
            stack.pop();

            // possible jumps we can take from this stone
            for (int j = jump - 1; j <= jump + 1; ++j) {
                // stone(s) to which we will reach after taking the jump 'j'
                int s = stone + j;
                // can only go forward and s must be in set and (s, j) must not be in visited
                std::string key = std::to_string(s) + "," + std::to_string(j);
                if (j > 0 && stonesSet.count(s) && !visited.count(key)) {
                    if (s == stones.back())
                        return true;
                    stack.push({s, j});
                    visited.insert(key);
                }
            }
        }

        return false;
    }
};
"""
