# Method 1: 

# logic: Exactly same as "1503. Last Moment Before All Ants Fall Out of a Plank" . just and extension

# Note: How to find sum of difference of all pairs in O(n*logn) than O(n^2).

# Now imagine finding distance of 'a4' with all elements before it:
# (a4-a1)+(a4-a2)+(a4-a3)---> (a4+a4+a4)-(a1+a2+3)---->i*a4-prefixsum[i-1], let index of a4= 'i'.

# No need to check for element on right side of it because 
# this will get automatically counted when we traverse further element on right.

# vvi: this formula can be used only if the positions are sorted.

# So sort the array and find the prefixSum where prefix[i]= sum till index 'i-1'.
# then find the total sum.

# Time : O(n*logn), space: O(1)

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod= 10**9 + 7
        n= len(nums)
        for i in range(n):
            if s[i]== 'R':
                nums[i]= nums[i] + d 
            else:
                nums[i]= nums[i] - d
        # nums[i] won't give the actual position of ith Robots but last position of all robots must in nums at some position.
        # Now we have to find the sum of distances between all pairs
        nums.sort()  # to get in O(n*logn)
        prefixSum= 0  # will store the sum till index 'i-1'. No need to store in array
        ans= 0
        for i in range(1, n):
            prefixSum += nums[i-1]
            ans = (ans + i* nums[i] - prefixSum) % mod
        return ans % mod

# Java Code 
"""
import java.util.*;

class Solution {
    public int sumDistance(int[] nums, String s, int d) {
        int mod = 1_000_000_007;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'R') {
                nums[i] = nums[i] + d;
            } else {
                nums[i] = nums[i] - d;
            }
        }

        // nums[i] won't give the actual position of ith Robot, but last position of all robots must in nums at some position.
        // Now we have to find the sum of distances between all pairs
        Arrays.sort(nums);  // to get in O(n * logn)

        long prefixSum = 0;  // will store the sum till index 'i - 1'. No need to store in array
        long ans = 0;

        for (int i = 1; i < n; i++) {
            prefixSum += nums[i - 1];
            ans = (ans + (long) i * nums[i] - prefixSum) % mod;
        }

        return (int) (ans % mod);
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int sumDistance(vector<int>& nums, string s, int d) {
        const int mod = 1e9 + 7;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            if (s[i] == 'R') {
                nums[i] += d;
            } else {
                nums[i] -= d;
            }
        }

        // nums[i] won't give the actual position of ith Robots but last position of all robots must in nums at some position.
        // Now we have to find the sum of distances between all pairs
        sort(nums.begin(), nums.end());  // to get in O(n*logn)

        long long prefixSum = 0;  // will store the sum till index 'i-1'. No need to store in array
        long long ans = 0;

        for (int i = 1; i < n; i++) {
            prefixSum += nums[i - 1];
            ans = (ans + 1LL * i * nums[i] - prefixSum) % mod;
        }

        return (ans + mod) % mod;
    }
};
"""

# Extension :

# 1) "2615. Sum of Distances"
# In this Q, we need to replace all values with pairwise sum.
# So in this we also need to do find sum from 'right' like 'left'.
# But in current Q, we need to find sum so no need to do from right.



