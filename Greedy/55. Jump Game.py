# Method 1:
# Dynamic Programming Approach: (1d DP)

'''
We initialize a dp array where each value represents whether you can jump to the end from that index.

Start from the second last index (n-2) and go backward.

For each index i, check if you can jump to an index j such that dp[j] is True.
If yes, set dp[i] = True.

Finally, return dp[0] — it tells us whether we can reach the end from the beginning.

"""
TIME COMPLEXITY :
-> The time complexity of this algorithm is O(n^2) in the worst case, where n is the length of the input array nums.
-> This is because for each index, we may need to check all possible jumps to the end, leading to a nested loop.

SPACE COMPLEXITY :

-> The space complexity is O(n) due to the dp array used to store whether each index can reach the end.
-> This is necessary to keep track of the reachable indices from each position in the array.

"""
'''


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

# Method 2: 

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

# Time: O(n), space: O(1)

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



# Method 3:
# Time : O(N) 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # 'reached' represents the closest checkpoint that we know 
        # can successfully make it to the very last index.
        # Initially, the last index itself is our destination.
        reached = n - 1
        
        # Traverse the array backwards, starting from the second-to-last element
        # down to the first element (index 0).
        for i in range(n - 2, -1, -1):
            
            # Check if the current index 'i' plus its maximum jump length 'nums[i]'
            # can meet or overshoot our target checkpoint ('reached').
            if i + nums[i] >= reached:
                # If yes, 'i' is a valid stepping stone. 
                # We update our target checkpoint to be 'i'.
                reached = i
                
            # Note on your commented 'else': We do NOT return False here.
            # Just because index 'i' cannot reach the checkpoint doesn't mean 
            # the problem is impossible; an earlier index (like i-1) might have 
            # a massive jump that completely leaps over index 'i'.
            # e.g ; [2, 0, 0] 
            
        # If our target checkpoint successfully rolled all the way back to the 
        # starting index (0), it means a valid path exists from start to end.
        return reached == 0












