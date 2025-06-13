# Method 1
# Brute force

# We don't care the original elements order, We only care about minimum and maximum element in subsequence.
# So we can sort the original array, and the result won't change.

"""
Approach :
1) We have to take 2 pointer one is from starting index and one is from last index of the list 
2) Sort the list
3) if the sum of the values of the elements according to the index is less than equal to the target then we can include all the possibilities.

 Time = O(n*logn)
 Space = O(1)
"""

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        mod = 10**9 + 7
        ans = 0
        i, j = 0, n -1
        while i <= j:
            if nums[i] + nums[j] <= target:
                # means this much ele we can include on right of 'i' and each will have 2 possibility.
                ans += 2 ** (j - i)
                i += 1
            else:
                j -= 1
        return ans % mod

#Java
"""
import java.util.Arrays;

class Solution {
    public int numSubseq(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        int mod = 1000000007;
        int ans = 0;
        int i = 0, j = n - 1;

        while (i <= j) {
            if (nums[i] + nums[j] <= target) {
                // means this much ele we can include on right of 'i' and each will have 2 possibility.
                ans = (ans + power(2, j - i, mod)) % mod;
                i++;
            } else {
                j--;
            }
        }
        return ans;
    }

    // Fast modular exponentiation
    private int power(int base, int exp, int mod) {
        long result = 1;
        long b = base;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return (int) result;
    }
}
"""

# C++
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int mod = 1e9 + 7;
        int ans = 0;
        int i = 0, j = n - 1;

        while (i <= j) {
            if (nums[i] + nums[j] <= target) {
                // means this much ele we can include on right of 'i' and each will have 2 possibility.
                ans = (ans + power(2, j - i, mod)) % mod;
                i++;
            } else {
                j--;
            }
        }
        return ans;
    }

private:
    // Fast modular exponentiation
    int power(int base, int exp, int mod) {
        long long result = 1;
        long long b = base;
        while (exp > 0) {
            if (exp & 1) {
                result = (result * b) % mod;
            }
            b = (b * b) % mod;
            exp >>= 1;
        }
        return result;
    }
};
"""