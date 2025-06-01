# Intution first, Codes next (in Python,Java,C++) and Time complexity at the last. 

# Intution :

# Our goal is to reach the (n-1)th index of the array, starting from the 0th index. If reach, return True, else return False.
# To find if we can do that , we have 2 methods - Greedy and Dp 

# Greedy Approach:

# We will keep track of the maximum index we can reach at each step.
# If at any point, the maximum index we can reach is less than the current index, we cannot proceed further and we break out of the loop.

# The maximum index that can be reached from the current index is calculated as `i + nums[i]`, where `i` is the current index and `nums[i]` is the value at that index.
# We keep updating the maximum index we can reach as we iterate through the array.

# If we reach the (n-1)th index, we return True.
# If we finish the loop without reaching the (n-1)th index, we return False.

# CODE 


# PYTHON


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr = nums[0]
        i = 0
        while i <= curr and i < n:
            curr = max(curr,i+nums[i])
            i += 1 
        return i >= n


        
# JAVA

'''
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int curr = nums[0];
        int i = 0;
        while (i <= curr && i < n) {
            curr = Math.max(curr, i + nums[i]);
            i++;
        }
        return i >= n;
    }
}
'''



# C++ 


'''
include <vector>
include <algorithm>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int curr = nums[0];
        int i = 0;

        while (i <= curr && i < n) {
            curr = max(curr, i + nums[i]);
            i++;
        }

        return i >= n;
    }
};
'''




# TIME COMPLEXITY :
# -> The time complexity of this algorithm is O(n), where n is the length of the input array nums.
# -> This is because we iterate through the array at most once, updating the current maximum reachable index.

# SPACE COMPLEXITY :
# -> The space complexity is O(1) since we are using a constant amount of extra space (only a few variables) regardless of the input size.




# Dynamic Programming Approach: (1d DP)

'''
We initialize a dp array where each value represents whether you can jump to the end from that index.

Start from the second last index (n-2) and go backward.

For each index i, check if you can jump to an index j such that dp[j] is True.
If yes, set dp[i] = True.

Finally, return dp[0] — it tells us whether we can reach the end from the beginning.
'''


# CODE:

# PYTHON


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[-1] = True  # The last index can always reach itself

        for i in range(n - 2, -1, -1):
            furthest_jump = min(i + nums[i], n - 1)
            for j in range(i + 1, furthest_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]



# JAVA

'''
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n];
        dp[n - 1] = true; // Last index can always reach itself
        for (int i = n - 2; i >= 0; i--) {
            int furthestJump = Math.min(i + nums[i], n - 1);
            for (int j = i + 1; j <= furthestJump; j++) {
                if (dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
}
'''





# C++




'''
include <vector>
include <algorithm>
using namespace std;
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<bool> dp(n, false);
        dp[n - 1] = true; // Last index can reach itself
        for (int i = n - 2; i >= 0; i--) {
            int furthestJump = min(i + nums[i], n - 1);
            for (int j = i + 1; j <= furthestJump; j++) {
                if (dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};
'''




# TIME COMPLEXITY :

# -> The time complexity of this algorithm is O(n^2) in the worst case, where n is the length of the input array nums.
# -> This is because for each index, we may need to check all possible jumps to the end, leading to a nested loop.



# SPACE COMPLEXITY :

# -> The space complexity is O(n) due to the dp array used to store whether each index can reach the end.
# -> This is necessary to keep track of the reachable indices from each position in the array.




# -> If we want to optimize space, we can use a single variable to keep track of the furthest reachable index, reducing the space complexity to O(1).
# -> However, this would not be a dynamic programming approach anymore, as we would not be storing intermediate results.
# -> Instead, it would be a greedy approach similar to the first solution.
# -> The greedy approach is more efficient in terms of time complexity (O(n)) and space complexity (O(1)).







