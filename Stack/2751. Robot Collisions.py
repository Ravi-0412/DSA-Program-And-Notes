# method 1: 

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

public class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        List<int[]> positionHealth = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (directions.charAt(i) == 'L') {
                positionHealth.add(new int[]{positions[i], -1 * healths[i], i}); // adding index also to return ans at last in given order
            } else {
                positionHealth.add(new int[]{positions[i], healths[i], i});
            }
        }

        // sort based on positions
        positionHealth.sort(Comparator.comparingInt(a -> a[0]));

        List<int[]> sortedHealth = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            sortedHealth.add(new int[]{positionHealth.get(i)[2], positionHealth.get(i)[1]});
        }

        Stack<int[]> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            int ind = sortedHealth.get(i)[0];
            int num = sortedHealth.get(i)[1];

            if (num > 0) {
                stack.push(new int[]{ind, num});
            } else {
                // keep on popping as the curr one will cancel the stack top.
                while (!stack.isEmpty() && stack.peek()[1] > 0 && stack.peek()[1] < Math.abs(num)) {
                    stack.pop();
                    num += 1; // because health of stronger robot decreases by '1' when they collide with weaker robot
                              // for decrement adding '+1' because 'num is negative'
                }

                // stack top is of same sign i.e -ve only, so append in stack
                if (stack.isEmpty() || stack.peek()[1] < 0) {
                    stack.push(new int[]{ind, num});
                }
                // if magnitude of both equal then both will get cancelled, so pop from stack.
                else if (stack.peek()[1] == Math.abs(num)) {
                    stack.pop();
                }
                // stack top is stronger, just decrement its health
                else if (stack.peek()[1] > Math.abs(num)) {
                    stack.peek()[1] -= 1;
                }
            }
        }

        // sort stack by index to return answer in input order
        List<int[]> remaining = new ArrayList<>(stack);
        remaining.sort(Comparator.comparingInt(a -> a[0]));
        List<Integer> ans = new ArrayList<>();
        for (int[] item : remaining) {
            ans.add(Math.abs(item[1]));
        }
        return ans;
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <stack>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<tuple<int, int, int>> positionHealth;

        for (int i = 0; i < n; i++) {
            if (directions[i] == 'L') {
                positionHealth.push_back({positions[i], -1 * healths[i], i}); // adding index also to return ans at last in given order
            } else {
                positionHealth.push_back({positions[i], healths[i], i});
            }
        }

        // sort based on positions
        sort(positionHealth.begin(), positionHealth.end());

        vector<pair<int, int>> sortedHealth;
        for (int i = 0; i < n; i++) {
            int idx = get<2>(positionHealth[i]);
            int val = get<1>(positionHealth[i]);
            sortedHealth.push_back({idx, val});
        }

        stack<pair<int, int>> stk;
        for (int i = 0; i < n; i++) {
            int ind = sortedHealth[i].first;
            int num = sortedHealth[i].second;

            if (num > 0) {
                stk.push({ind, num});
            } else {
                // keep on popping as the curr one will cancel the stack top.
                while (!stk.empty() && stk.top().second > 0 && stk.top().second < abs(num)) {
                    stk.pop();
                    num += 1; // because health of stronger robot decreases by '1' when they collide with weaker robot
                              // for decrement adding '+1' because 'num is negative'
                }

                // stack top is of same sign i.e -ve only, so append in stack
                if (stk.empty() || stk.top().second < 0) {
                    stk.push({ind, num});
                }
                // if magnitude of both equal then both will get cancelled, so pop from stack.
                else if (stk.top().second == abs(num)) {
                    stk.pop();
                }
                // stack top is stronger, just decrement its health
                else if (stk.top().second > abs(num)) {
                    auto temp = stk.top(); stk.pop();
                    temp.second -= 1;
                    stk.push(temp);
                }
            }
        }

        // move stack to vector and sort by index
        vector<pair<int, int>> remaining;
        while (!stk.empty()) {
            remaining.push_back(stk.top());
            stk.pop();
        }
        sort(remaining.begin(), remaining.end());

        vector<int> ans;
        for (auto& it : remaining) {
            ans.push_back(abs(it.second));
        }

        return ans;
    }
};

"""