# Just extended version of: "735. Asteroid Collision".

# lOgic: for checking whether they will collide or not, we need to sort according to position.
# Note: Now position has no meaning because in case of "R(+), L(-1)" they will collide for sure i.e
# just same as "735. Asteroid Collision".

# so 1) sort according to position 
# 2) then reduce convert this question to ""735. Asteroid Collision" by adding '-' to health of robots going left
# and apply same logic.

# Difference from q: "735. Asteroid Collision"
# Note: i) Also we need to return answer in given initial order so we need to keep track of 'index' also.
# ii) also we need to decrase energy of stronger robot in collision.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        position_health = []
        for i in range(n):
            if directions[i] == "L":
                position_health.append([positions[i] , -1* healths[i], i])   # adding index also to return ans at last in given order
            else:
                position_health.append([positions[i] , healths[i], i])

        position_health.sort()
        sorted_health = [[position_health[i][2], position_health[i][1]] for i in range(n)]
        stack = []
        for i in range(n):
            ind , num = sorted_health[i][0], sorted_health[i][1]
            if num > 0:
                stack.append([ind, num])
            else:
                # keep on poping as the curr one will cancel the stack top.
                while stack and stack[-1][1] > 0 and stack[-1][1] < abs(num):
                    stack.pop()
                    num += 1  # because health of stronger robot decreases by '1' when they collide with weaker robot
                              # for decrement adding '+1' because 'num is negative'

                # stack top is of same sign i.e -ve only, so append in stack
                if not stack or stack[-1][1] < 0:  
                    stack.append([ind, num])
                # if magnitude of both equal then both will get cancelled, so pop from stack.
                elif stack[-1][1]== abs(num):
                    stack.pop()
                elif stack[-1][1] >  abs(num):
                    # here we need to decrease th health of stack top by '1'
                    # because health of stronger robot decreases by '1'.
                    stack[-1][1] -= 1
    
        stack.sort()  # sort according to index to return ans in given order
        ans = []
        for ind, health in stack:
            ans.append(abs(health))
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public int[] survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        List<int[]> positionHealth = new ArrayList<>();

        // Store positions, health with direction conversion
        for (int i = 0; i < n; i++) {
            if (directions.charAt(i) == 'L') {
                positionHealth.add(new int[]{positions[i], -healths[i], i}); // Add index for final ordering
            } else {
                positionHealth.add(new int[]{positions[i], healths[i], i});
            }
        }

        // Sort by position
        positionHealth.sort(Comparator.comparingInt(a -> a[0]));

        List<int[]> sortedHealth = new ArrayList<>();
        for (int[] ph : positionHealth) {
            sortedHealth.add(new int[]{ph[2], ph[1]});
        }

        Stack<int[]> stack = new Stack<>();

        // Process robots
        for (int[] sh : sortedHealth) {
            int ind = sh[0], num = sh[1];

            if (num > 0) {
                stack.push(new int[]{ind, num});
            } else {
                // Handle collision logic
                while (!stack.isEmpty() && stack.peek()[1] > 0 && stack.peek()[1] < Math.abs(num)) {
                    stack.pop();
                    num += 1; // Health of stronger robot decreases by 1
                }

                if (stack.isEmpty() || stack.peek()[1] < 0) {
                    stack.push(new int[]{ind, num});
                } else if (stack.peek()[1] == Math.abs(num)) {
                    stack.pop();
                } else if (stack.peek()[1] > Math.abs(num)) {
                    stack.peek()[1] -= 1;
                }
            }
        }

        // Sort according to index for final answer
        List<int[]> sortedStack = new ArrayList<>(stack);
        sortedStack.sort(Comparator.comparingInt(a -> a[0]));

        int[] ans = new int[sortedStack.size()];
        for (int i = 0; i < sortedStack.size(); i++) {
            ans[i] = Math.abs(sortedStack.get(i)[1]);
        }

        return ans;
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<vector<int>> position_health;

        // Store positions, health with direction conversion
        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') {
                position_health.push_back({positions[i], -healths[i], i}); // Add index for final ordering
            } else {
                position_health.push_back({positions[i], healths[i], i});
            }
        }

        // Sort by position
        sort(position_health.begin(), position_health.end());

        vector<vector<int>> sorted_health;
        for (int i = 0; i < n; i++) {
            sorted_health.push_back({position_health[i][2], position_health[i][1]});
        }

        stack<vector<int>> st;

        // Process robots
        for (int i = 0; i < n; i++) {
            int ind = sorted_health[i][0], num = sorted_health[i][1];

            if (num > 0) {
                st.push({ind, num});
            } else {
                // Handle collision logic
                while (!st.empty() && st.top()[1] > 0 && st.top()[1] < abs(num)) {
                    st.pop();
                    num += 1; // Health of stronger robot decreases by 1
                }

                if (st.empty() || st.top()[1] < 0) {
                    st.push({ind, num});
                } else if (st.top()[1] == abs(num)) {
                    st.pop();
                } else if (st.top()[1] > abs(num)) {
                    st.top()[1] -= 1;
                }
            }
        }

        // Sort according to index for final answer
        vector<vector<int>> sorted_stack;
        while (!st.empty()) {
            sorted_stack.push_back(st.top());
            st.pop();
        }

        sort(sorted_stack.begin(), sorted_stack.end());

        vector<int> ans;
        for (auto& elem : sorted_stack) {
            ans.push_back(abs(elem[1]));
        }

        return ans;
    }
};
"""