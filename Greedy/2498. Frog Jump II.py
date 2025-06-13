
'''
the frog should make the journey from first stone to last, and last to first without touching any stone twice. (excpet the first and last stone). 
So, think of it like jornye from first to last stone twice, without touching any stone twice, exlcuding the first and last stone.

The maximum distance covered in this journey should be minimum 
Ahh, here we go binary search !!! - But wait, are we thinking in a dumb manner? We can greedily calculate the distance 
Ok, let's see both the approaches one by one. 

'''

# Method 1: 
# Binary Search Approach :
'''

initialise the boundaried to 0 and 10**9 for performing binary search - If you not aware of binary search, please learn it first.

The checking function will take mid as the input, as return True if teh frog can make the journey with the maximum distance of mid, otherwise return False.
According to the checking function, we will update the boundaries of the binary search.

🔍 Helper Function Intuition:
We want to check if the frog can cross the river with a maximum jump distance of mid.
To do this, we go through the stones in two steps:

Forward Pass (Left to Right):

Start from the first stone.
Try to jump to the next stone only if the distance is within the allowed mid.
If the gap is too big, we try skipping one stone (like jumping over it).
If we can't even skip (because we already skipped the last one), then it's not possible — return False.
We keep track of skipped stone positions in a set so we can avoid them later easily - directly removing from array takes O(n) time, so we use a set for O(1) lookups.

Backward Pass (Right to Left):

We do the same check, but in reverse.
This is just to make sure the skipped stones from the forward pass didn’t break the path when coming back.
If we find a jump that’s too far and can't be skipped, we return False.
If both directions are okay, it means the path is valid for the current mid.


"""
TIME COMPLEXITY ANALYSIS :

-> Binary search - 0(logn)
-> Iterating throught the array in helper function each time we make a call - O(n)
-> So, the overall time complexity is O(nlogn)

SPACE COMPLEXITY ANALYSIS :
 O(n) for the set used in the helper function.
"""
'''

# PYTHON :

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)

        def helper(mid):
            dels = set()
            prev = stones[0]
            idx = 0
            for i in range(1,n):
                if abs(stones[i]-prev) > mid :
                    if idx == i-1 :
                        return False
                    prev = stones[i-1]
                    dels.add(i-1)
            prev = stones[-1]
            for i in range(n-2,-1,-1):
                if i in dels :
                    continue 
                if abs(stones[i]-prev) > mid :
                    return False 
                prev = stones[i]
            return True 
        l,r = 0,10**9+1
        ans = -1
        while l <= r :
            mid = l + (r-l) // 2 
            if helper(mid):
                ans = mid 
                r = mid - 1 
            else:
                l = mid + 1 
        return ans

# java
"""
import java.util.*;

class Solution {
    int[] stones;
    int n;

    public int maxJump(int[] stones) {
        this.stones = stones;
        this.n = stones.length;

        int l = 0, r = 1000000000 + 1;
        int ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (helper(mid)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }

    // helper(mid)
    boolean helper(int mid) {
        Set<Integer> dels = new HashSet<>();
        int prev = stones[0];
        int idx = 0;
        for (int i = 1; i < n; i++) {
            if (Math.abs(stones[i] - prev) > mid) {
                if (idx == i - 1) {
                    return false;
                }
                prev = stones[i - 1];
                dels.add(i - 1);
            } else {
                prev = stones[i];
                idx = i;
            }
        }
        prev = stones[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (dels.contains(i)) {
                continue;
            }
            if (Math.abs(stones[i] - prev) > mid) {
                return false;
            }
            prev = stones[i];
        }
        return true;
    }
}
"""

# C++ 
"""
#include <vector>
#include <unordered_set>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> stones;
    int n;

    int maxJump(vector<int>& inputStones) {
        stones = inputStones;
        n = stones.size();

        int l = 0, r = 1000000000 + 1;
        int ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (helper(mid)) {
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return ans;
    }

    // helper(mid)
    bool helper(int mid) {
        unordered_set<int> dels;
        int prev = stones[0];
        int idx = 0;
        for (int i = 1; i < n; i++) {
            if (abs(stones[i] - prev) > mid) {
                if (idx == i - 1) {
                    return false;
                }
                prev = stones[i - 1];
                dels.insert(i - 1);
            } else {
                prev = stones[i];
                idx = i;
            }
        }
        prev = stones[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (dels.count(i)) {
                continue;
            }
            if (abs(stones[i] - prev) > mid) {
                return false;
            }
            prev = stones[i];
        }
        return true;
    }
};
"""


# Method 2: 
# Now, can we come up with a better solution, which is more intuitive and less complex?
# Yes, it is the greedy approach.

'''
The greedy approach is more intuitive and straightforward.
The frog needs to traverse through the array twice, once from the first stone to the last and then from the last stone to the first, without touching any stone twice, excpet the first and last stone 
So, an optimal way would be going from start to end like i,i+2,i+4 and coming back through stones of i+1,i+3,i+5, and so on.
You can think of it like a zig-zag pattern, where the frog jumps over stones in a way that minimizes the maximum distance it has to jump.
'''

# The elements at even indices represent the stones the frog jumps on while going from the first stone to the last, and the elements at odd indices represent the stones it jumps on while coming back.
# This is the exact intution behind the greedy approach.
# Look at the code now for deeper understanding.

# TIME COMPLEXITY ANALYSIS :
# -> The time complexity is O(n) as we are iterating through the array once.

# SPACE COMPLEXITY ANALYSIS :
# -> The space complexity is O(1) as we are not using any extra space except for a few variables.

# PYTHON : 

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n= len(stones)
        if n== 2:
            return stones[1] - stones[0]
        ans= 0
        # same num is used twice, one for going forward one for going backward.
        for i in range(2, n):  
            ans= max(ans, stones[i] - stones[i-2])
        return ans
    

# JAVA :

''''
class Solution {
    public int maxJump(int[] stones) {
        int n = stones.length;
        if (n == 2) {
            return stones[1] - stones[0];
        }

        int ans = 0;
        // Jump every two stones (zig-zag: forward + backward)
        // same num is used twice, one for going forward one for going backward.

        for (int i = 2; i < n; i++) {
            ans = Math.max(ans, stones[i] - stones[i - 2]);
        }

        return ans;
    }
}
'''

# C++ :

'''
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxJump(vector<int>& stones) {
        int n = stones.size();
        if (n == 2) {
            return stones[1] - stones[0];
        }

        int ans = 0;
        // Jump every two stones (zig-zag: forward + backward)
        // same num is used twice, one for going forward one for going backward.
        for (int i = 2; i < n; i++) {
            ans = max(ans, stones[i] - stones[i - 2]);
        }

        return ans;
    }
};
'''



