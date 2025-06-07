# Logic: 
# If car at lower position can catch the fleet just ahead of it then ,it will join that fleet.
# Else will run as new fleet.

# So to know whether lower position car can catch or not
# We will traverse in descending order of position.

# current car can only catch fleet ahead of it if time taken by him to reach target is <= fleet ahead of it.

# after sorting position in descending order we only need to compare the time with fleet ahead of it.

# why stack:
# We need to find the next fleet just ahead of it and compare the time.

# Note why not while loop ?
# Because: if stack_top(stcakc[-1]) is not able to catch the fleet ahead of it i.e stack[-2]
# then, no way we can current fleet can catch up the fleet stack[-2]. 
# current car can join the only fleet ahead of it i.e stack[-1] .

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            t = (target - pos) / vel   # time taken by current car to reach target.
            if not stack or t > stack[-1]:
                # if stack is empty or time taken is more then it won't be able to catch fleet 
                # running ahead of it. it will form new fleet
                stack.append(t)
            # else: # it will join the fleet infront of it
        return len(stack)
            


# Method 2:
# Optimising to O(1) space
    
# Just same logic as above.
# Reason: since we are comparing only with 1st fleet ahead of it, other fleet won't matter to current one.
# so there is no need to stack.
# we can one variable to keep tarck of pre_time.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pre_t = None
        ans = 0
        for pos, vel in sorted(zip(position, speed))[::-1]:
            t = (target - pos) / vel
            if not pre_t or t > pre_t:
                ans += 1
                pre_t = t
            # else:
                    # will join the fleet ahead of it
        return ans

# Java Code
"""
//Method 1
import java.util.Arrays;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] cars = new double[n][2]; // {position, time to reach target}

        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = (double) (target - position[i]) / speed[i];
        }

        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0])); // Sort by position descending

        int fleets = 0;
        double[] stack = new double[n];
        int index = 0;

        for (double[] car : cars) {
            double t = car[1];
            if (index == 0 || t > stack[index - 1]) {
                stack[index++] = t; // Form new fleet
                fleets++;
            }
        }
        return fleets;
    }
}
//Method 2
import java.util.Arrays;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] cars = new double[n][2];

        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = (double) (target - position[i]) / speed[i];
        }

        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0])); // Sort by position descending

        double pre_t = -1;
        int fleets = 0;
        for (double[] car : cars) {
            double t = car[1];
            if (t > pre_t) {
                fleets++;
                pre_t = t;
            }
        }
        return fleets;
    }
}
"""

# C++ Code
"""
//Method 1
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, double>> cars; // {position, time to reach target}
        for (int i = 0; i < position.size(); i++) {
            double t = (double)(target - position[i]) / speed[i]; // Compute time
            cars.push_back({position[i], t});
        }

        // Sort cars by position in descending order
        sort(cars.rbegin(), cars.rend());

        vector<double> stack;
        for (auto& [pos, t] : cars) {
            if (stack.empty() || t > stack.back()) {
                stack.push_back(t); // Form new fleet
            }
        }
        return stack.size();
    }
};
//Method 2
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, double>> cars;
        for (int i = 0; i < position.size(); i++) {
            double t = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], t});
        }

        sort(cars.rbegin(), cars.rend());

        double pre_t = -1;
        int fleets = 0;
        for (auto& [pos, t] : cars) {
            if (t > pre_t) {
                fleets++;
                pre_t = t;
            }
        }
        return fleets;
    }
};
"""