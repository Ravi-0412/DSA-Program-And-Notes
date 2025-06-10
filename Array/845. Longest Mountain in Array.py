# Method 1:
# Take each element as peak and find number that we can include
# on its left and right && take max.

# Time = space = O(n) and we are doing 3 traversal.

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        up, down = [0] * n , [0]*n
        # finding the no of elements smaller while going up
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up[i] = up[i-1] + 1
        # finding the no of elements smaller while coming down
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1
        ans = 0
        for i in range(n):
            if up[i] > 0 and down[i] > 0:
                ans = max(ans, up[i] + down[i] + 1) 
        return ans

# Method 2:
# In one pass an in O(1) space

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        maxMnt = 0
        i = 1
        n = len(arr)
        
        while i < n:
          # skip the equal element
            while i < n and arr[i-1] == arr[i]:
                i += 1
            # find the length of upHill
            up = 0
            while i < n and arr[i-1] < arr[i]:
                up += 1
                i += 1
            # find the length of downHill
            down = 0
            while i < n and arr[i-1] > arr[i]:
                down += 1
                i += 1
            # update the ans if there exist element both side
            if up > 0 and down > 0:
                maxMnt = max(maxMnt, up + down + 1)
        
        return maxMnt

# Java Code 
"""
//Method 1
import java.util.*;

class Solution {
    // Method 1: Take each element as peak and find numbers that can be included on its left and right && take max.
    // Time = space = O(n) and we are doing 3 traversals.
    public int longestMountain(int[] arr) {
        int n = arr.length;
        if (n < 3) return 0;

        int[] up = new int[n], down = new int[n];

        // finding the number of elements smaller while going up
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) {
                up[i] = up[i - 1] + 1;
            }
        }

        // finding the number of elements smaller while coming down
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > arr[i + 1]) {
                down[i] = down[i + 1] + 1;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (up[i] > 0 && down[i] > 0) {
                ans = Math.max(ans, up[i] + down[i] + 1);
            }
        }

        return ans;
    }
}
//Method 2
class Solution {
    // Method 2: In one pass and in O(1) space
    public int longestMountain(int[] arr) {
        int maxMnt = 0;
        int i = 1, n = arr.length;

        while (i < n) {
            // skip the equal element
            while (i < n && arr[i - 1] == arr[i]) {
                i++;
            }

            // find the length of uphill
            int up = 0;
            while (i < n && arr[i - 1] < arr[i]) {
                up++;
                i++;
            }

            // find the length of downhill
            int down = 0;
            while (i < n && arr[i - 1] > arr[i]) {
                down++;
                i++;
            }

            // update the answer if there exist elements on both sides
            if (up > 0 && down > 0) {
                maxMnt = Math.max(maxMnt, up + down + 1);
            }
        }

        return maxMnt;
    }
}
"""

# C++ Code 
"""
//Method 1
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Method 1: Take each element as peak and find numbers that can be included on its left and right && take max.
    // Time = space = O(n) and we are doing 3 traversals.
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        if (n < 3) return 0;

        vector<int> up(n, 0), down(n, 0);

        // finding the number of elements smaller while going up
        for (int i = 1; i < n; i++) {
            if (arr[i] > arr[i - 1]) {
                up[i] = up[i - 1] + 1;
            }
        }

        // finding the number of elements smaller while coming down
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i] > arr[i + 1]) {
                down[i] = down[i + 1] + 1;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (up[i] > 0 && down[i] > 0) {
                ans = max(ans, up[i] + down[i] + 1);
            }
        }

        return ans;
    }
};
//Method 2
class Solution {
public:
    // Method 2: In one pass and in O(1) space
    int longestMountain(vector<int>& arr) {
        int maxMnt = 0;
        int i = 1, n = arr.size();

        while (i < n) {
            // skip the equal element
            while (i < n && arr[i - 1] == arr[i]) {
                i++;
            }

            // find the length of uphill
            int up = 0;
            while (i < n && arr[i - 1] < arr[i]) {
                up++;
                i++;
            }

            // find the length of downhill
            int down = 0;
            while (i < n && arr[i - 1] > arr[i]) {
                down++;
                i++;
            }

            // update the answer if there exist elements on both sides
            if (up > 0 && down > 0) {
                maxMnt = max(maxMnt, up + down + 1);
            }
        }

        return maxMnt;
    }
};
"""