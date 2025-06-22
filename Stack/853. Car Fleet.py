# Method 1: 

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
            
# Java Code 
"""
import java.util.*;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        double[][] cars = new double[n][2];
        
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        // Sort cars by starting position in descending order
        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));

        Stack<Double> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            double pos = cars[i][0], vel = cars[i][1];
            double t = (target - pos) / vel;  // time taken by current car to reach target
            if (stack.isEmpty() || t > stack.peek()) {
                // if stack is empty or time taken is more then it won't be able to catch fleet 
                // running ahead of it. it will form new fleet
                stack.push(t);
            }
            // else: it will join the fleet in front of it
        }

        return stack.size();
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<int, int>> cars(n);
        for (int i = 0; i < n; ++i) {
            cars[i] = {position[i], speed[i]};
        }

        // Sort cars by starting position in descending order
        sort(cars.rbegin(), cars.rend());

        stack<double> st;
        for (int i = 0; i < n; ++i) {
            double pos = cars[i].first, vel = cars[i].second;
            double t = (target - pos) / vel;  // time taken by current car to reach target
            if (st.empty() || t > st.top()) {
                // if stack is empty or time taken is more then it won't be able to catch fleet 
                // running ahead of it. it will form new fleet
                st.push(t);
            }
            // else: it will join the fleet in front of it
        }

        return st.size();
    }
};

"""

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
import java.util.*;

public class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        int ans = 0;
        Double pre_t = null;

        double[][] cars = new double[n][2];
        for (int i = 0; i < n; i++) {
            cars[i][0] = position[i];
            cars[i][1] = speed[i];
        }

        // Sort by position descending
        Arrays.sort(cars, (a, b) -> Double.compare(b[0], a[0]));

        for (int i = 0; i < n; i++) {
            double pos = cars[i][0], vel = cars[i][1];
            double t = (target - pos) / vel;
            if (pre_t == null || t > pre_t) {
                ans++;
                pre_t = t;
            }
            // else:
            //     will join the fleet ahead of it
        }

        return ans;
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        int ans = 0;
        double pre_t = -1.0;

        // Pair of (position, speed)
        vector<pair<int, int>> cars(n);
        for (int i = 0; i < n; ++i) {
            cars[i] = {position[i], speed[i]};
        }

        // Sort by position descending
        sort(cars.rbegin(), cars.rend());

        for (int i = 0; i < n; ++i) {
            double pos = cars[i].first, vel = cars[i].second;
            double t = (target - pos) / vel;
            if (pre_t < 0 || t > pre_t) {
                ans++;
                pre_t = t;
            }
            // else:
            //     will join the fleet ahead of it
        }

        return ans;
    }
};

"""
